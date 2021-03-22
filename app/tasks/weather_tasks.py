from celery_app import app
from tasks.send_line_msg_tasks import send_reply_text_message

from infrastructure.service.weather_service import OpenWeatherService
from infrastructure.service.weather_center_service import WeatherCenterService

# get_forecast_and_send_weather_message_task 的包裝
def async_get_forecast_and_send_weather_message_task(reply_token: str, place_name: str = None, lat: float = None, lon: float = None):
    get_forecast_and_send_weather_message_task.apply_async(args=(reply_token, place_name, lat, lon,))

@app.task
def get_forecast_and_send_weather_message_task(reply_token: str, place_name: str, lat: float, lon: float):
    svc = OpenWeatherService()
    weathers = svc.get_forecast(place_name=place_name, lat=lat, lon=lon)

    # 節省 line 訊息數，將多個預測結合成一組字串
    message = '\n\n'.join([w.format_to_message() for w in weathers])
    send_reply_text_message(reply_token, message)

def async_get_last_weather_from_weather_center_task(reply_token: str):
    get_last_weather_from_weather_center_task.apply_async(args=(reply_token,))

@app.task
def get_last_weather_from_weather_center_task(reply_token: str):
    svc = WeatherCenterService()
    result = svc.get_latest()

    if result:
        send_reply_text_message(reply_token, result.format_to_weather_center_message())

    else:
        send_reply_text_message(reply_token, '氣象站資料取得失敗')

@app.task
def send_weather_periodic_task():
    subscribe_user_ids = [
        'Uebaac5edfee64f6b934a4d27b937cead'
    ]

    # get data from weather center service
    svc = WeatherCenterService()
    result = svc.get_latest()

    if result:
        center_msg = result.format_to_weather_center_message()
    else:
        center_msg = '氣象站資料取得失敗'

    # get data from open weather service
    svc = OpenWeatherService()
    weathers = svc.get_forecast(place_name='taipei')

    # 節省 line 訊息數，將多個預測結合成一組字串
    forecast_msg = '\n\n'.join([w.format_to_message() for w in weathers])
    
    # send msg
    message = '{}\n\n{}'.format(center_msg, forecast_msg)    
    for user_id in subscribe_user_ids:
        send_text_message(user_id, message)