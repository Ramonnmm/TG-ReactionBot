from os import environ as env

class Telegram:
    API_ID = int(env.get("TG_API_ID", 1234))
    API_HASH = env.get("TG_API_HASH", "xyz")
    BOT_TOKEN = env.get("TG_BOT_TOKEN", "abc")
    BOT_USERNAME = env.get("TG_BOT_USERNAME", "DrReactBot")
    EMOJIS = [
        "👍", "👎", "❤", "🔥", 
        "🥰", "👏", "
        "🎉", 
        
    ]

LOGGER_CONFIG_JSON = {
    'version': 50,
    'formatters': {
        'default': {
            'format': '[%(asctime)s][%(name)s][%(levelname)s] -> %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'event-log.txt',
            'formatter': 'default'
        },
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'loggers': {
        'bot': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'pyrogram': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        }
    }
}
