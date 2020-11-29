import logging
import sys
import settings

logging.basicConfig(
    stream=sys.stdout,
    level=logging.DEBUG if settings.DEBUG else logging.INFO,
    format="{service_name} | %(asctime)s - %(name)s-%(filename)s[line:%(lineno)d] - %(levelname)s - %(message)s".format(
        service_name=settings.SERVICE_NAME
    )
)
