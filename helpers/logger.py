import logging
from logging.config import dictConfig


dictConfig(Config.FLASK_LOG_CONFIGURATION)
LOG = logging.getLogger(__name__)
