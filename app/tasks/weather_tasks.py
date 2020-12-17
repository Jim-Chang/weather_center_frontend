from celery_app import app
from tasks.send_line_msg_tasks import send_reply_text_message

from infrastructure.service.weather_service import OpenWeatherService

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