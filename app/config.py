import os

# use k8s config-maps to override this file
DEBUG = bool(os.environ.get('DEBUG', False))
TEST = bool(os.environ.get('TEST', False))

SERVICE_NAME = 'chatbot-service'

HTTP_PORT = 8080
REDIS_NODE = os.environ.get('REDIS_NODE', '')

# celery queue names，依照任務區分不同的 queue
CELERY_CHATBOT_QUEUE_NAME = os.environ.get('CELERY_CHATBOT_QUEUE_NAME', '')
CELERY_DOWNLOAD_QUEUE_NAME = os.environ.get('CELERY_DOWNLOAD_QUEUE_NAME', '')
# 儲存這個 celery 目前正在聽哪個 queue，主要設定會再 entrypoint 啟動 celery 就設定進去
CELERY_LISTEN_QUEUE_NAME = os.environ.get('CELERY_LISTEN_QUEUE_NAME', '')


DOWNLOAD_FOLDER_PATH = '/download/{}'
RCLONE_CONFIG_NAME = 'chatbot-upload'