from celery_app import app
from tasks.send_line_msg_tasks import send_text_message

from infrastructure.service.stock_service import YfStockService

# get_stock_price_task 的包裝
def async_get_stock_price_task(user_id: str, stock_name: str):
    get_stock_price_task.apply_async(args=(user_id, stock_name,))


@app.task
def get_stock_price_task(user_id: str, stock_name: str):
    svc = YfStockService()
    stock = svc.get_stock(stock_name)

    if stock:
        send_text_message(stock.format_to_message())
    else:
        send_text_message('抓股票資訊出問題了！')