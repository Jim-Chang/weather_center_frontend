from celery import Celery
import settings

app = Celery(
    settings.SERVICE_NAME,
    broker='redis://' + settings.REDIS_NODE,
    backend='redis://' + settings.REDIS_NODE,
    include=[
        'tasks.send_line_msg_tasks',
        'tasks.download_and_upload_task',
        'tasks.refresh_cache_for_wp_task',
    ]
)

app.conf.update(
    result_expires=600,
)

if __name__ == '__main__':
    app.start()