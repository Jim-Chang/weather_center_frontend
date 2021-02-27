from linebot.models import Event
from utils.permission import check_permission
from domain.enums.type import FeatureType

@check_permission(FeatureType.youtubedl)
def run_download_and_upload_task_command(event: Event):
    from tasks.download_and_upload_task import async_do_download_and_upload_task

    async_do_download_and_upload_task(event.source.user_id, event.reply_token, event.message.text)

@check_permission(FeatureType.wordpress)
def run_refresh_cache_for_wp_command(event: Event):
    from tasks.refresh_cache_for_wp_task import async_refresh_cache_for_wp_task

    async_refresh_cache_for_wp_task(event.source.user_id, event.reply_token)

@check_permission(FeatureType.stock)
def run_get_stock_price_command(event: Event):
    from tasks.stock_tasks import async_get_stock_price_task
    from tasks.send_line_msg_tasks import async_send_reply_text_message

    commands = event.message.text.split(' ')
    # 指令範例 '股票 0050.tw' 
    if len(commands) == 2:
        async_get_stock_price_task(event.reply_token, commands[1])
    else:
        async_send_reply_text_message(event.reply_token, '股票的指令有誤哦！範例如下：\n股票 0050.tw')

@check_permission(FeatureType.weather)
def run_get_forecast_and_send_weather_message_command(event: Event):
    from tasks.weather_tasks import async_get_forecast_and_send_weather_message_task

    async_get_forecast_and_send_weather_message_task(
        reply_token=event.reply_token,
        lat=event.message.latitude,
        lon=event.message.longitude
    )

@check_permission(FeatureType.weather)
def run_get_last_weather_from_weather_center(event: Event):
    from tasks.weather_tasks import async_get_last_weather_from_weather_center_task

    async_get_last_weather_from_weather_center_task(event.reply_token)

# 回傳 user_id，不需要權限控制
def run_get_user_id_command(event: Event):
    from tasks.send_line_msg_tasks import async_send_reply_text_message
    async_send_reply_text_message(event.reply_token, event.source.user_id)

@check_permission(FeatureType.motion)
def run_motion_start_detection_command(event: Event):
    from tasks.motion_tasks import async_start_detection_task
    async_start_detection_task(
        user_id=event.source.user_id,
        reply_token=event.reply_token,
        camera_id=1   # 目前只有一個 直接 hard code
    )

@check_permission(FeatureType.motion)
def run_motion_stop_detection_command(event: Event):
    from tasks.motion_tasks import async_stop_detection_task
    async_stop_detection_task(
        user_id=event.source.user_id,
        reply_token=event.reply_token,
        camera_id=1   # 目前只有一個 直接 hard code
    )

@check_permission(FeatureType.motion)
def run_motion_get_detection_status_command(event: Event):
    from tasks.motion_tasks import async_get_detection_status_task
    async_get_detection_status_task(
        user_id=event.source.user_id,
        reply_token=event.reply_token,
        camera_id=1   # 目前只有一個 直接 hard code
    )