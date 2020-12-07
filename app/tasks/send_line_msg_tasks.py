from typing import List
import settings
from celery_app import app

from linebot import LineBotApi
from linebot.models import TextSendMessage

# send_text_message 的包裝
def async_send_text_message(user_id: str, text_message: str):
    send_text_message.apply_async(args=(user_id, text_message,))

@app.task
def send_text_message(user_id: str, text_message: str):
    line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
    line_bot_api.push_message(
        user_id,
        TextSendMessage(text=text_message)
    )

# send_text_message 的包裝
def async_send_multi_text_message(user_id: str, text_messages: List[str]):
    send_multi_text_message.apply_async(args=(user_id, text_messages,))

@app.task
def send_multi_text_message(user_id: str, text_messages: List[str]):
    line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

    messages = [TextSendMessage(text=text_message) for text_message in text_messages]

    line_bot_api.push_message(
        user_id,
        messages
    )