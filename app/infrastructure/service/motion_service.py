import requests
import settings
from utils.log import logging

from domain.service.motion_service import IMotionService
from domain.enums.status import MotionDetectionStatus

class RealMotionService(IMotionService):

    def __init__(self):
        self._host = 'http://{}:7999'.format(settings.MOTION_SERVER_IP)

    def set_detection_start(self, camera_id: int) -> bool:
        # 'http://192.168.68.58:7999/0/detection/start'
        r = requests.get('{host}/{camera_id}/detection/start'.format(
            host=self._host,
            camera_id=camera_id
        ))

        # Camera 1 Detection resumed\nDone \n'
        if 'resumed' in r.text:
            return True
        else:
            logging.warning('[Motion] set detection start fail: {}'.format(r.text))
            return False

    def set_detection_stop(self, camera_id: int) -> bool:
        # 'http://192.168.68.58:7999/0/detection/pause'
        r = requests.get('{host}/{camera_id}/detection/pause'.format(
            host=self._host,
            camera_id=camera_id
        ))

        # Camera 1 Detection paused\nDone \n'
        if 'paused' in r.text:
            return True
        else:
            logging.warning('[Motion] set detection stop fail: {}'.format(r.text))
            return False

    def get_detection_status(self, camera_id: int) -> MotionDetectionStatus:
        # 'http://192.168.68.58:7999/0/detection/status'
        r = requests.get('{host}/{camera_id}/detection/status'.format(
            host=self._host,
            camera_id=camera_id
        ))

        # Camera 1 Detection status ACTIVE \n
        if 'ACTIVE' in r.text:
            return MotionDetectionStatus.enable

        # Camera 1 Detection status PAUSE \n
        else:
            return MotionDetectionStatus.disable
