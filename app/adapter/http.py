from flask import Flask
# from healthcheck import HealthCheck, EnvironmentDump
# from check_health import CHECK_FUNCTIONS, dump_env
import settings

from presentation.configure.chatbot_api_configure import IChatbotApiConfigure, RealChatbotApiConfigure
from presentation.http.line_webhook_api import line_message_webhook_api

def get_app(
    chatbot_api_configure: IChatbotApiConfigure = RealChatbotApiConfigure(),
):
    app = Flask(__name__)
    # basic setting
    app.config['DEBUG'] = settings.DEBUG
    app.config['TESTING'] = settings.TEST
    app.config['APP_NAME'] = settings.SERVICE_NAME

    # register blueprint
    app.register_blueprint(line_message_webhook_api, url_prefix='/webhook/line/message')

    # setting configure for api
    app.config['CHATBOT_API_CONFIGURE'] = chatbot_api_configure

    # setting health check endpoint
    # set_health_check(app)

    # print(app.url_map)
    return app

# def set_health_check(app):
#     health = HealthCheck()
#     envdump = EnvironmentDump()

#     for check_func in CHECK_FUNCTIONS:
#         health.add_check(check_func)

#     envdump.add_section("application", dump_env)

#     # Add a flask route to expose information
#     app.add_url_rule("/healthcheck", "healthcheck", view_func=lambda: health.run())
#     app.add_url_rule("/environment", "environment", view_func=lambda: envdump.run())

def run_dev_server():
    app = get_app()
    app.run(host='0.0.0.0', port=settings.HTTP_PORT)

