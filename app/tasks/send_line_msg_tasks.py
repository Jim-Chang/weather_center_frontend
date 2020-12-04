import settings
from celery_app import app

from linebot import LineBotApi
from linebot.models import TextSendMessage

# send_text_message 的包裝
def async_send_text_message(reply_token: str, text_message: str):
    send_text_message.apply_async(args=(reply_token, text_message,), queue=settings.CHATBOT_SERVICE_CELERY_QUEUE)

@app.task
def send_text_message(user_id: str, text_message: str):
    line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
    line_bot_api.push_message(
        user_id,
        TextSendMessage(text=text_message)
    )