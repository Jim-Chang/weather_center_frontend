from celery_app import app
from tasks.send_line_msg_tasks import send_text_message

from infrastructure.service.weather_service import OpenWeatherService

# get_forcast_and_send_weather_message_task 的包裝
def async_get_forcast_and_send_weather_message_task(user_id: str, place_name: str = None, lat: float = None, lon: float = None):
    get_forcast_and_send_weather_message_task.apply_async(args=(user_id, place_name, lat, lon,))

@app.task
def get_forcast_and_send_weather_message_task(user_id: str, place_name: str, lat: float, lon: float):
    svc = OpenWeatherService()
    weathers = svc.get_forcast(place_name=place_name, lat=lat, lon=lon)

    for weather in weathers:
        send_text_message(user_id, weathers.format_to_message())