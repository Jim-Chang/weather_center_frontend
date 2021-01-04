from celery_app import app
from tasks.send_line_msg_tasks import send_reply_text_message

from domain.enums.status import MotionDetectionStatus
from infrastructure.service.motion_service import RealMotionService

def async_start_detection_task(reply_token: str, camera_id: int):
    start_detection_task.apply_async(args=(reply_token, camera_id,))

@app.task
def start_detection_task(reply_token: str, camera_id: int):
    svc = RealMotionService()
    result = svc.set_detection_status(camera_id, MotionDetectionStatus.enable)

    if result:
        msg = '啟動動態偵測完成！'
    else:
        msg = '啟動動態偵測`失敗`！'

    send_reply_text_message(reply_token, msg)

def async_stop_detection_task(reply_token: str, camera_id: int):
    stop_detection_task.apply_async(args=(reply_token, camera_id,))

@app.task
def stop_detection_task(reply_token: str, camera_id: int):
    svc = RealMotionService()
    result = svc.set_detection_status(camera_id, MotionDetectionStatus.enabl)

    if result:
        msg = '關閉動態偵測完成！'
    else:
        msg = '關閉動態偵測`失敗`！'

    send_reply_text_message(reply_token, msg)

def async_get_detection_status_task(reply_token: str, camera_id: int):
    get_detection_status_task.apply_async(args=(reply_token, camera_id,))

@app.task
def get_detection_status_task(reply_token: str, camera_id: int):
    svc = RealMotionService()
    result = svc.get_detection_status(camera_id)

    if result == MotionDetectionStatus.enable:
        msg = '動態偵測有啟動哦！'

    else:
        msg = '動態偵測`沒有`啟動'

    send_reply_text_message(reply_token, msg)