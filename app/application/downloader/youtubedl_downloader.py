from typing import List, Tuple
from subprocess import check_output, CalledProcessError
from utils.log import logging
import settings

class YoutubedlDownloader:

    def download(self, url: str) -> Tuple[bool, str]:
        logging.info('Start fetch filename...')
        try:
            filename = self._get_filename(url)

        except CalledProcessError:
            logging.error('Fetch filename fail', exc_info=True)
            return False, None

        logging.info('Find filename: {}, start to download...'.format(filename))
        try:
            shell_logs = self._run_download(filename, url)

        except CalledProcessError:
            logging.error('Download file error', exc_info=True)
            return False, None

        logging.info('Download finish. Follows are log of youtube-dl')
        for shell_log in shell_logs:
            if shell_log:
                logging.info(shell_log)

        return True, filename

    def _get_filename(self, url: str) -> str:
        result = check_output(['youtube-dl', '--get-filename', url])
        return result.decode().replace('\n', '')

    def _run_download(self, filename: str, url: str) -> List[str]:
        result = check_output(['youtube-dl', '-o', settings.DOWNLOAD_FOLDER_PATH.format(filename), url])
        return result.decode().split('\n')