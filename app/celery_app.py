from celery import Celery
import settings

app = Celery(
    settings.SERVICE_NAME,
    broker='redis://' + settings.REDIS_NODE,
    backend='redis://' + settings.REDIS_NODE,
    include=[
        'tasks.send_line_msg_tasks',
    ]
)

app.conf.update(
    result_expires=600,
)

if __name__ == '__main__':
    app.start()