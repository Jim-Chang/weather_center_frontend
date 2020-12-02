import settings
from celery_app import app

from linebot import LineBotApi
from linebot.models import TextSendMessage

@app.task
def send_text_message(reply_token: str, text_message: str):
    line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
    line_bot_api.reply_message(
        reply_token,
        TextSendMessage(text=text_message)
    )