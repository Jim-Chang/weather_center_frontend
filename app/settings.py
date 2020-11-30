import secret as sc
import config as cf

# configs
DEBUG = cf.DEBUG
TEST = cf.TEST

SERVICE_NAME = cf.SERVICE_NAME

HTTP_PORT = cf.HTTP_PORT
REDIS_NODE = cf.REDIS_NODE

# celery queue names
CHATBOT_SERVICE_CELERY_QUEUE = cf.CHATBOT_SERVICE_CELERY_QUEUE

DOWNLOAD_FOLDER_PATH = cf.DOWNLOAD_FOLDER_PATH

# secrets
LINE_CHANNEL_ACCESS_TOKEN = sc.LINE_CHANNEL_ACCESS_TOKEN
LINE_CHANNEL_SECRET = sc.LINE_CHANNEL_SECRET

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
