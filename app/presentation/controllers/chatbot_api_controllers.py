from typing import List
import settings

from presentation.translator.text_command_translator import TextCommandTranslator
from tasks.send_line_msg_tasks import async_send_text_message

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
        self._translator = TextCommandTranslator()

    def handle(self) -> bool:
        events = self._extract_events(self._request_body, self._signature)

        for event in events:
            if isinstance(event.message, TextMessage):
                self._dispatch_command(event)
            
            else:
                print('in')
                async_send_text_message(event.source.user_id, '這個我還看不懂所以略過哦')

        return True

    def _extract_events(self, request_body: dict, signature: str) -> List[Event]:
        parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
        
        try:
            return parser.parse(request_body, signature)

        except InvalidSignatureError:
            raise

    def _dispatch_command(self, event: Event):
        command_func = self._translator.decode_command(event.message.text)
        if command_func:
            command_func(event)

        else:
            async_send_text_message(event.source.user_id, '不是指令清單裡，所以略過～')
