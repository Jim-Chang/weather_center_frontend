from typing import Tuple
import settings
from celery_app import app
from tasks.send_line_msg_tasks import async_send_text_message

from application.downloader.youtubedl_downloader import YoutubedlDownloader
from application.uploader.rclone_uploader import RcloneUploader

# do_download_and_upload_task 的包裝
def async_do_download_and_upload_task(reply_token: str, url: str):
    do_download_and_upload_task.apply_async(args=(reply_token, url,), queue=settings.CHATBOT_SERVICE_CELERY_QUEUE)

@app.task
def do_download_and_upload_task(reply_token: str, url: str):
    DownloadAndUploadTask(reply_token, url).execute()

class DownloadAndUploadTask:

    def __init__(self, reply_token: str, url: str):
        self._reply_token = reply_token
        self._url = url

    def execute(self):
        async_send_text_message(self._reply_token, '開始下載！')
        download_result, filename = self._start_download()

        if download_result:
            async_send_text_message(self._reply_token, '下載完成！開始上傳 Google Drive')
            upload_result = self._start_upload(filename)
            async_send_text_message(self._reply_token, '上傳成功！' if upload_result else '上傳失敗...')

        else:
            async_send_text_message(self._reply_token, '下載失敗哭哭')

    def _start_download(self) -> Tuple[bool, str]:
        downloader = YoutubedlDownloader()
        return downloader.download(self._url)

    def _start_upload(self, filename: str) -> bool:
        uploader = RcloneUploader()
        return uploader.upload(filename)
