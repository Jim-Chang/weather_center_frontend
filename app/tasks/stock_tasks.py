from celery_app import app
from tasks.send_line_msg_tasks import send_text_message, send_reply_text_message

from infrastructure.service.stock_service import YfStockService

# get_stock_price_task 的包裝
def async_get_stock_price_task(reply_token: str, stock_name: str):
    get_stock_price_task.apply_async(args=(reply_token, stock_name,))


@app.task
def get_stock_price_task(reply_token: str, stock_name: str):
    svc = YfStockService()
    stock = svc.get_stock(stock_name)

    if stock:
        send_reply_text_message(reply_token, stock.format_to_message())
    else:
        send_reply_text_message(reply_token, '抓股票資訊出問題了！')

@app.task
def send_0050tw_price_after_close_periodic_task():
    subscribe_user_ids = [
        'Uebaac5edfee64f6b934a4d27b937cead'
    ]

    svc = YfStockService()
    stock = svc.get_stock('0050.tw')

    if stock:
        for user_id in subscribe_user_ids:
            send_text_message(user_id, stock.format_to_message())