from typing import List, Tuple
from subprocess import check_output, CalledProcessError
import os
from utils.log import logging
import settings

class YoutubedlDownloader:

    # returns: (task result, file name, file size in MB)
    def download(self, url: str) -> Tuple[bool, str, int]:
        logging.info('Start fetch filename...')
        try:
            filename = self._get_filename(url)

        except CalledProcessError:
            logging.error('Fetch filename fail', exc_info=True)
            return False, None, 0

        logging.info('Find filename: {}, start to download...'.format(filename))
        try:
            shell_logs = self._run_download(filename, url)

        except CalledProcessError:
            logging.error('Download file error', exc_info=True)
            return False, None, 0

        logging.info('Download finish. Follows are log of youtube-dl')
        for shell_log in shell_logs:
            if shell_log:
                logging.info(shell_log)

        return True, filename, self._get_filesize(filename)

    def _get_filename(self, url: str) -> str:
        result = check_output(['youtube-dl', '--get-filename', url])
        # return result.decode().replace('\n', '')
        # 因為 ffmpeg 4.1.2 merge 的時候只能下 mkv，所以我們將副檔名改為 mkv
        # 4.3 以後就可以了
        filename = result.decode().replace('\n', '').split('.')[0]
        return filename + '.mkv'

    def _get_filesize(self, filename: str) -> int:
        return int(os.path.getsize(settings.DOWNLOAD_FOLDER_PATH.format(filename)) / 1024 / 1024)

    def _run_download(self, filename: str, url: str) -> List[str]:
        result = check_output([
            'youtube-dl',
            '-f', 'bestvideo+bestaudio',
            '--merge-output-format', 'mkv',  # 因應 ffmpeg 4.1.2 所以改成 mkv
            '-o', settings.DOWNLOAD_FOLDER_PATH.format(filename),
            url])
        return result.decode().split('\n')