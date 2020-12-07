import os

# use k8s secrets to override this file

LINE_CHANNEL_ACCESS_TOKEN = os.environ.get('LINE_CHANNEL_ACCESS_TOKEN')
LINE_CHANNEL_SECRET = os.environ.get('LINE_CHANNEL_SECRET')

OPEN_WEATHER_APPID = os.environ.get('OPEN_WEATHER_APPID')


# db settings
# MAIN_DB = {
#     'username': param_helper.get('DB_USERNAME', '/microservice/pm-service/db/user_name'),
#     'password': param_helper.get('DB_PASSWORD', '/microservice/pm-service/db/password'),
#     'ip': param_helper.get('DB_IP', '/microservice/db/master/ip'),
#     'db': param_helper.get('DB_NAME', '/microservice/pm-service/db/db_name')
# }

# SLAVE_DB = {
#     'username': param_helper.get('DB_USERNAME', '/microservice/pm-service/db/user_name'),
#     'password': param_helper.get('DB_PASSWORD', '/microservice/pm-service/db/password'),
#     'ip': param_helper.get('SLAVE_DB_IP', '/microservice/db/slave/0/ip'),
#     'db': param_helper.get('DB_NAME', '/microservice/pm-service/db/db_name')
# }

# TEST_DB = {
#     'username': os.environ.get('DB_USERNAME'),
#     'password': os.environ.get('DB_PASSWORD'),
#     'ip': os.environ.get('DB_IP'),
#     'db': os.environ.get('TEST_DB_NAME')
# }
