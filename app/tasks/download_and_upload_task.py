from typing import Tuple
import settings
from celery_app import app
from tasks import send_line_msg_tasks

from application.downloader.youtubedl_downloader import YoutubedlDownloader
from application.uploader.rclone_uploader import RcloneUploader


@app.task
def do_download_and_upload_task(reply_token: str, url: str):
    DownloadAndUploadTask(reply_token, url).execute()

class DownloadAndUploadTask:

    def __init__(self, reply_token: str, url: str):
        self._reply_token = reply_token
        self._url = url

    def execute(self):
        self._send_text_message('收到！開始下載！')
        download_result, filename = self._start_download()

        if download_result:
            self._send_text_message('下載完成！開始上傳 Google Drive')
            upload_result = self._start_upload(filename)
            self._send_text_message('上傳成功！' if upload_result else '上傳失敗...')

        else:
            self._send_text_message('下載失敗哭哭')

    def _start_download(self) -> Tuple[bool, str]:
        downloader = YoutubedlDownloader()
        return downloader.download(self._url)

    def _start_upload(self, filename: str) -> bool:
        uploader = RcloneUploader()
        return uploader.upload(filename)

    def _send_text_message(self, message: str):
        send_line_msg_tasks.send_text_message.apply_async(args=(self._reply_token, message,), queue=settings.CHATBOT_SERVICE_CELERY_QUEUE)