from abc import ABC, abstractmethod
from domain.enums.status import MotionDetectionStatus

class IMotionService(ABC):

    @abstractmethod
    def set_detection_start(self, camera_id: int) -> bool:
        pass

    @abstractmethod
    def set_detection_stop(self, camera_id: int) -> bool:
        pass

    @abstractmethod
    def get_detection_status(self, camera_id: int) -> MotionDetectionStatus:
        pass