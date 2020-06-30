from .base import * # NOQA

DEBUG = False

ALLOWED_HOSTS = ['the55box.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'typeidea',
        'USER': 'root',
        'PASSWORD': 'mysql',
        'HOST': '127.0.0.1',
        'POST': 3306,
        'CONN_MAX_AGE': 5 * 60,
        'OPTIONS': {
            'charset': 'utf8mb64'
        },
    },
}

REDIS_URL = '127.0.0.1:6379:1'

CACHEs = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': REDIS_URL,
        'TIMEOUT': 300,
        'OPTIONS': {
            # 'PASSWORD': '123456',
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'PARSER_CLASS': 'redis.connection.HiredisParser',
        },
        'CONNECTION_POOL_CLASS': 'redis.connection.BlockingConnectionPool',
    }
}
