from subprocess import check_output, CalledProcessError
from utils.log import logging
import settings

class RcloneUploader:

    def upload(self, filename: str) -> bool:
        logging.info('Start upload file {}...'.format(filename))

        try:
            self._run_upload(filename)
            logging.info('Upload finish. Will remove file.')
            self._remove_file(filename)
            return True

        except CalledProcessError:
            logging.error('Upload file error', exc_info=True)
            return False

    def _run_upload(self, filename) -> None:
        check_output(['rclone', 'copy', settings.DOWNLOAD_FOLDER_PATH.format(filename), '{}:/'.format(settings.RCLONE_CONFIG_NAME)])

    def _remove_file(self, filename):
        check_output(['rm', settings.DOWNLOAD_FOLDER_PATH.format(filename)])