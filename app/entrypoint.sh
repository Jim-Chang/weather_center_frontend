#!/bin/sh

# http_adapter mode
if [ "$SERVE_MODE" = "http_adapter" ]
then
	echo "SERVE MODE: http_adapter"
	uwsgi --ini uwsgi.ini

# celery worker mode
elif [ "$SERVE_MODE" = "celery_worker" ]
then
	echo "SERVE MODE: celery_worker"
	celery --app celery_app worker --concurrency $CELERY_WORKER_NUM --queues $CELERY_LISTEN_QUEUE_NAME --loglevel INFO

# celery beat mode
elif [ "$SERVE_MODE" = "celery_beat" ]
then
	echo "SERVE MODE: celery_beat"
	celery --app celery_app beat --loglevel INFO

# container only run migrate
elif [ "$SERVE_MODE" = "run_migrate" ]
then
	echo "SERVE MODE: run_migrate"
	alembic -c /app/db/migrations/alembic.ini upgrade head

# all mode (for develop use. 如果沒有設定環境變數，預設也跑這裡)
else
	echo "SERVE MODE: all"
	uwsgi --ini uwsgi.ini
fi