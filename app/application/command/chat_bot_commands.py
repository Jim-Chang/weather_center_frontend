from linebot.models import Event
from tasks.download_and_upload_task import async_do_download_and_upload_task
from tasks.send_line_msg_tasks import async_send_text_message

def run_download_and_upload_task_command(event: Event):
    async_send_text_message(event.reply_token, '收到網址，啟動 youtube-dl')
    async_do_download_and_upload_task(event.reply_token, event.message.text)