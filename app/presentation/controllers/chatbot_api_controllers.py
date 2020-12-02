from typing import List
import settings
import validators
from tasks import send_line_msg_tasks
from tasks.download_and_upload_task import do_download_and_upload_task

from linebot import WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    TextMessage,
    Event,
)
# line doc of message event: https://developers.line.biz/zh-hant/reference/messaging-api/#message-event

class LineCallbackController:

    def __init__(self, request_body: dict, signature: str):
        self._request_body = request_body
        self._signature = signature

    def handle(self) -> bool:
        events = self._extract_events(self._request_body, self._signature)

        for event in events:
            if isinstance(event.message, TextMessage):
                self._dispatch_command(event)
            
            else:
                self._send_sorry_msg(event)

        return True

    def _extract_events(self, request_body: dict, signature: str) -> List[Event]:
        parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
        
        try:
            return parser.parse(request_body, signature)

        except InvalidSignatureError:
            raise

    def _send_sorry_msg(self, event: Event):
        message = '收到 {} 但我看不懂所以略過'.format(type(event))
        self._send_text_message(event.reply_token, message)

    def _dispatch_command(self, event: Event):
        if validators.url(event.message.text):
            self._send_text_message(event.reply_token, '收到網址，啟動 youtube-dl')
            do_download_and_upload_task.apply_async(args=(event.reply_token, event.message.text,), queue=settings.CHATBOT_SERVICE_CELERY_QUEUE)

        else:
            self._send_text_message(event.reply_token, '不是網址，所以略過～')

    def _send_text_message(self, reply_token: str, message: str):
        send_line_msg_tasks.send_text_message.apply_async(args=(reply_token, message,), queue=settings.CHATBOT_SERVICE_CELERY_QUEUE)