from src.utils.order_processor import process_order_file

# Обработка заказов
process_order_file("data/orders.txt", "data/processed_orders_report.txt")