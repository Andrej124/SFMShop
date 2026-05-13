def load_orders_from_file(filename):
    """Загружает заказы из файла"""
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
        orders = []
        for line in lines:
            cleaned_line = line.strip()
            if cleaned_line:  # Пропускаем пустые строки
                orders.append(cleaned_line)
        return orders
    except FileNotFoundError:
        print("Ошибка: файл", filename, "не найден")
        return []


def calculate_order_total(price, discount_rate):
    """Вычисляет итоговую стоимость со скидкой"""
    total = price * (1 - discount_rate)
    return round(total, 2)


def get_discount_by_total(total):
    """Определяет размер скидки в зависимости от суммы"""
    if total <= 0:
        return 0
    elif total > 10000:
        return 0.15
    elif total > 5000:
        return 0.10
    else:
        return 0.05


def process_orders(orders_data):
    """Обрабатывает список заказов"""
    processed = []
    for order_line in orders_data:
        try:
            parts = order_line.split(":")
            if len(parts) == 4:
                order_id = parts[0].strip()
                order_sum = int(parts[1].strip())
                order_status = parts[2].strip()
                order_user = parts[3].strip()

                discount_rate = get_discount_by_total(order_sum)
                final_total = calculate_order_total(order_sum, discount_rate)

                processed.append({
                    "order_id": order_id,
                    "total": final_total,
                    "status": order_status,
                    "user": order_user
                })
            else:
                print("Ошибка: неверный формат строки:", order_line)
        except ValueError:
            print("Ошибка: неверный формат числа в строке:", order_line)

    return processed


def analyze_orders(processed_orders):
    """Анализирует обработанные заказы и собирает статистику"""
    stats = {
        "total_orders": 0,
        "total_sum": 0,
        "by_status": {},
        "unique_users": set()
    }

    for order in processed_orders:
        stats["total_orders"] = stats["total_orders"] + 1
        stats["total_sum"] = stats["total_sum"] + order["total"]

        status = order["status"]
        if status in stats["by_status"]:
            stats["by_status"][status] = stats["by_status"][status] + 1
        else:
            stats["by_status"][status] = 1

        stats["unique_users"].add(order["user"])

    # Преобразуем множество в список
    stats["unique_users"] = list(stats["unique_users"])

    return stats


def process_order_file(input_file, output_file):
    """Обрабатывает файл с заказами и создает отчет"""
    # Загружаем заказы
    orders_data = load_orders_from_file(input_file)

    if not orders_data:
        print("Нет данных для обработки")
        return

    # Обрабатываем заказы
    processed_orders = process_orders(orders_data)

    # Анализируем статистику
    stats = analyze_orders(processed_orders)

    # Формируем строку со статусами
    status_lines = []
    for status, count in stats["by_status"].items():
        status_lines.append(status + ": " + str(count))
    status_string = ", ".join(status_lines)

    # Записываем результаты
    try:
        with open(output_file, "w") as file:
            file.write(f"Обработано заказов: {stats['total_orders']}\n")
            file.write(f"Общая сумма: {stats['total_sum']} руб.\n")
            file.write(f"По статусам: {status_string}\n")
            file.write(f"Уникальных пользователей: {len(stats['unique_users'])}\n")
        print("Отчет создан:", output_file)
    except Exception as e:
        print("Ошибка при записи файла:", e)