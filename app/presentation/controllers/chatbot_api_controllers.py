from typing import List
import settings

from presentation.translator.text_command_translator import TextCommandTranslator
from tasks.send_line_msg_tasks import async_send_text_message
from tasks import weather_tasks

from linebot import WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    TextMessage,
    LocationMessage,
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

            elif isinstance(event.message, LocationMessage):
                self._dispatch_location(event)
            
            else:
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
            hint_msg = '不是指令清單裡，所以略過～\n\n可用指令如下：\n{}'.format(
                '\n'.join(TextCommandTranslator.command_map.keys())
            )
            async_send_text_message(event.source.user_id, hint_msg)

    def _dispatch_location(self, event: Event):
        weather_tasks.async_get_forcast_and_send_weather_message_task(
            user_id=event.source.user_id,
            lat=event.message.latitude,
            lon=event.message.longitude
        )
