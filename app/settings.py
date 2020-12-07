import secret as sc
import config as cf

# configs
DEBUG = cf.DEBUG
TEST = cf.TEST

SERVICE_NAME = cf.SERVICE_NAME

HTTP_PORT = cf.HTTP_PORT
REDIS_NODE = cf.REDIS_NODE

# celery queue names，依照任務區分不同的 queue
CELERY_CHATBOT_QUEUE_NAME = cf.CELERY_CHATBOT_QUEUE_NAME
CELERY_DOWNLOAD_QUEUE_NAME = cf.CELERY_DOWNLOAD_QUEUE_NAME
# 儲存這個 celery 目前正在聽哪個 queue，主要設定會再 entrypoint 啟動 celery 就設定進去
CELERY_LISTEN_QUEUE_NAME = cf.CELERY_LISTEN_QUEUE_NAME

DOWNLOAD_FOLDER_PATH = cf.DOWNLOAD_FOLDER_PATH
RCLONE_CONFIG_NAME = cf.RCLONE_CONFIG_NAME

# secrets
LINE_CHANNEL_ACCESS_TOKEN = sc.LINE_CHANNEL_ACCESS_TOKEN
LINE_CHANNEL_SECRET = sc.LINE_CHANNEL_SECRET

OPEN_WEATHER_APPID = sc.OPEN_WEATHER_APPID

# MAIN_DB_URL = 'postgresql+psycopg2://{username}:{password}@{ip}/{db}'.format(
#     username=sc.MAIN_DB['username'],
#     password=sc.MAIN_DB['password'],
#     ip=sc.MAIN_DB['ip'],
#     db=sc.MAIN_DB['db']
# )

# SLAVE_DB_URL = 'postgresql+psycopg2://{username}:{password}@{ip}/{db}'.format(
#     username=sc.SLAVE_DB['username'],
#     password=sc.SLAVE_DB['password'],
#     ip=sc.SLAVE_DB['ip'],
#     db=sc.SLAVE_DB['db']
# )

# TEST_DB_URL = 'postgresql+psycopg2://{username}:{password}@{ip}/{db}'.format(
#     username=sc.TEST_DB['username'],
#     password=sc.TEST_DB['password'],
#     ip=sc.TEST_DB['ip'],
#     db=sc.TEST_DB['db']
# )
