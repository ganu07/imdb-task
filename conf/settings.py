"""
A file to store all the config related settings
"""
class Config(object):
    SQLITE_PREFIX = "sqlite:///"
    SQLITEDB = "inventory.db"
    FLASK_LOG_CONFIGURATION = {
        'version': 1,
        'formatters': {'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }},
       
    }
    EDIT_USER_MAP = {"admin": "admin"}
