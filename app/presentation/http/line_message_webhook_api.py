from flask import Blueprint, request, current_app, abort
from utils.log import logging

from presentation.controllers.chatbot_api_controllers import (
    LineCallbackController,
)

from linebot.exceptions import InvalidSignatureError

line_message_webhook_api = Blueprint('line_message_webhook_api', __name__)

@line_message_webhook_api.route("/callback", methods=['POST'])
def receive_callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    logging.debug(body)

    try:
        controller = LineCallbackController(body, signature)
        controller.handle()

    except InvalidSignatureError:
        logging.error("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'