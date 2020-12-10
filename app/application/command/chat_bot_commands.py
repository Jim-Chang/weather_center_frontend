from linebot.models import Event
from utils.permission import check_permission
from domain.enums.type import FeatureType

@check_permission(FeatureType.youtubedl)
def run_download_and_upload_task_command(event: Event):
    from tasks.download_and_upload_task import async_do_download_and_upload_task

    async_do_download_and_upload_task(event.source.user_id, event.message.text)

@check_permission(FeatureType.wordpress)
def run_refresh_cache_for_wp_command(event: Event):
    from tasks.refresh_cache_for_wp_task import async_refresh_cache_for_wp_task

    async_refresh_cache_for_wp_task(event.source.user_id)

@check_permission(FeatureType.stock)
def run_get_stock_price_command(event: Event):
    from tasks.stock_tasks import async_get_stock_price_task
    from tasks.send_line_msg_tasks import async_send_text_message

    commands = event.message.text.split(' ')
    # 指令範例 '股票 0050.tw' 
    if len(commands) == 2:
        async_get_stock_price_task(event.source.user_id, commands[1])
    else:
        async_send_text_message(event.source.user_id, '股票的指令有誤哦！範例如下：\n股票 0050.tw')

@check_permission(FeatureType.weather)
def run_get_forecast_and_send_weather_message_command(event: Event):
    from tasks.weather_tasks import async_get_forecast_and_send_weather_message_task

    async_get_forecast_and_send_weather_message_task(
        user_id=event.source.user_id,
        lat=event.message.latitude,
        lon=event.message.longitude
    )