import logging
from logging.config import dictConfig
from conf.settings import Config

dictConfig(Config.FLASK_LOG_CONFIGURATION)
LOG = logging.getLogger(__name__)
