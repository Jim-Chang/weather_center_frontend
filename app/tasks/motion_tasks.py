from typing import Optional
from celery_app import app
from tasks.send_line_msg_tasks import send_reply_text_message, send_text_message

from domain.enums.type import RoleType
from domain.enums.status import MotionDetectionStatus
from infrastructure.service.motion_service import RealMotionService

from utils import permission

def async_start_detection_task(user_id: str, reply_token: str, camera_id: int):
    start_detection_task.apply_async(args=(user_id, reply_token, camera_id))

# 提供給 celery beat 呼叫使用
@app.task
def cron_start_detection_task():
    notify_user_id = permission._role_user_list_map.get(RoleType.admin)[0]
    start_detection_task(notify_user_id, None, 1)  # 目前只有一個 直接 hard code

@app.task
def start_detection_task(user_id: str, reply_token: Optional[str], camera_id: int):
    svc = RealMotionService()
    result = svc.set_detection_status(camera_id, MotionDetectionStatus.enable)

    if result:
        msg = '啟動動態偵測完成！'
    else:
        msg = '啟動動態偵測 `失敗` ！'

    if reply_token:
        send_reply_text_message(reply_token, msg)
    else:
        send_text_message(user_id, msg)

def async_stop_detection_task(user_id: str, reply_token: str, camera_id: int):
    stop_detection_task.apply_async(args=(user_id, reply_token, camera_id,))

# 提供給 celery beat 呼叫使用
@app.task
def cron_stop_detection_task():
    notify_user_id = permission._role_user_list_map.get(RoleType.admin)[0]
    stop_detection_task(notify_user_id, None, 1)  # 目前只有一個 直接 hard code

@app.task
def stop_detection_task(user_id: str, reply_token: Optional[str], camera_id: int):
    svc = RealMotionService()
    result = svc.set_detection_status(camera_id, MotionDetectionStatus.disable)

    if result:
        msg = '關閉動態偵測完成！'
    else:
        msg = '關閉動態偵測 `失敗` ！'

    if reply_token:
        send_reply_text_message(reply_token, msg)
    else:
        send_text_message(user_id, msg)

def async_get_detection_status_task(user_id: str, reply_token: str, camera_id: int):
    get_detection_status_task.apply_async(args=(user_id, reply_token, camera_id,))

@app.task
def get_detection_status_task(user_id: str, reply_token: Optional[str], camera_id: int):
    svc = RealMotionService()
    result = svc.get_detection_status(camera_id)

    if result == MotionDetectionStatus.enable:
        msg = '動態偵測有啟動哦！'

    else:
        msg = '動態偵測 `沒有` 啟動'

    if reply_token:
        send_reply_text_message(reply_token, msg)
    else:
        send_text_message(user_id, msg)