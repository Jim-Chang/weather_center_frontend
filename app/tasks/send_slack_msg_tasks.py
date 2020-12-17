import requests
import settings
from celery_app import app

slack_webhook_api = 'https://hooks.slack.com/services{}'

# send_message 的包裝
def async_send_message(text_message: str):
    send_message.apply_async(args=(text_message,))

@app.task
def send_message(text_message: str):
    requests.post(
        slack_webhook_api.format(settings.SLACK_WEBHOOK),
        json={
            'text': text_message
        }
    )