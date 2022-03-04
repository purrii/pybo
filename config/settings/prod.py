from .base import *

ALLOWED_HOSTS = ['3.39.49.197', 'porrti14.duckdns.org']
STATIC_ROOT = BASE_DIR / 'pybo/static/'
STATICFILES_DIRS = []
DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pybo',
        'USER': 'dbmasteruser',
        'PASSWORD':'59-tw9&A.X=t1h;Bh(H[Sn,8w%5>.pFv',
        'HOST':'ls-1e4da8b0195d1964d96155946cf84b20d702dfb8.cawmzwoqjybh.ap-northeast-2.rds.amazonaws.com',
        'PORT':'5432',
    }
}