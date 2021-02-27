from celery import Celery
from celery.schedules import crontab
import settings

# 增加 celery task 時注意
# Celery task 宣告 
# 和
# task_routes 宣告
# 都要補上！

app = Celery(
    settings.SERVICE_NAME,
    broker='redis://' + settings.REDIS_NODE,
    backend='redis://' + settings.REDIS_NODE,
    include=[
        'tasks.send_line_msg_tasks',
        'tasks.send_slack_msg_tasks',
        'tasks.download_and_upload_task',
        'tasks.refresh_cache_for_wp_task',
        'tasks.weather_tasks',
        'tasks.stock_tasks',
        'tasks.motion_tasks',
    ]
)

app.conf.update(
    result_expires=600,
)

app.conf.task_routes = {
    'tasks.send_line_msg_tasks.*': {'queue': settings.CELERY_CHATBOT_QUEUE_NAME},
    'tasks.send_slack_msg_tasks.*': {'queue': settings.CELERY_CHATBOT_QUEUE_NAME},
    'tasks.weather_tasks.*': {'queue': settings.CELERY_CHATBOT_QUEUE_NAME},
    'tasks.stock_tasks.*': {'queue': settings.CELERY_CHATBOT_QUEUE_NAME},
    'tasks.motion_tasks.*': {'queue': settings.CELERY_CHATBOT_QUEUE_NAME},

    'tasks.refresh_cache_for_wp_task.*': {'queue': settings.CELERY_DOWNLOAD_QUEUE_NAME},
    'tasks.download_and_upload_task.*': {'queue': settings.CELERY_DOWNLOAD_QUEUE_NAME},
}

app.conf.beat_schedule = {
    'send-0050tw-price': {
        'task': 'tasks.stock_tasks.send_0050tw_price_after_close_periodic_task',
        'schedule': crontab(minute='30', hour='9,10', day_of_week='mon,tue,wed,thu,fri'),
    },
    'send-0050tw-price-after-close': {
        'task': 'tasks.stock_tasks.send_0050tw_price_after_close_periodic_task',
        'schedule': crontab(minute='10', hour='14', day_of_week='mon,tue,wed,thu,fri'),
    },
    'weekday-start-motion-detection': {
        'task': 'tasks.motion_tasks.cron_start_detection_task',
        'schedule': crontab(minute='0', hour='8', day_of_week='mon,tue,wed,thu,fri'),
    },
    'weekday-stop-motion-detection': {
        'task': 'tasks.motion_tasks.cron_stop_detection_task',
        'schedule': crontab(minute='0', hour='20', day_of_week='mon,tue,wed,thu,fri'),
    }
}
app.conf.timezone = 'Asia/Taipei'

if __name__ == '__main__':
    app.start()