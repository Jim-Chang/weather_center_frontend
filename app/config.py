import os

# use k8s config-maps to override this file
DEBUG = bool(os.environ.get('DEBUG', False))
TEST = bool(os.environ.get('TEST', False))

SERVICE_NAME = 'chatbot-service'

HTTP_PORT = 8080
REDIS_NODE = os.environ.get('REDIS_NODE', '')

# celery queue names
CHATBOT_SERVICE_CELERY_QUEUE = 'chatbot-service'

DOWNLOAD_FOLDER_PATH = '/app/download/{}'
