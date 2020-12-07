from typing import Tuple
from celery_app import app
from tasks.send_line_msg_tasks import send_text_message

from application.downloader.youtubedl_downloader import YoutubedlDownloader
from application.uploader.rclone_uploader import RcloneUploader

# do_download_and_upload_task 的包裝
def async_do_download_and_upload_task(user_id: str, url: str):
    do_download_and_upload_task.apply_async(args=(user_id, url,))

@app.task
def do_download_and_upload_task(user_id: str, url: str):
    DownloadAndUploadTask(user_id, url).execute()

class DownloadAndUploadTask:

    def __init__(self, user_id: str, url: str):
        self._user_id = user_id
        self._url = url

    def execute(self):
        send_text_message(self._user_id, '收到網址，啟動 youtube-dl，開始下載！')
        download_result, filename, filesize = self._start_download()

        if download_result:
            send_text_message(self._user_id, '下載完成！共 {} MB\n\n檔案名稱為：{}\n\n開始上傳 Google Drive'.format(filesize, filename))
            upload_result = self._start_upload(filename)
            send_text_message(self._user_id, '上傳成功！\n\n{}'.format(filename) if upload_result else '上傳失敗...\n\n{}'.format(filename))

        else:
            send_text_message(self._user_id, '下載失敗哭哭')

    def _start_download(self) -> Tuple[bool, str]:
        downloader = YoutubedlDownloader()
        return downloader.download(self._url)

    def _start_upload(self, filename: str) -> bool:
        uploader = RcloneUploader()
        return uploader.upload(filename)
