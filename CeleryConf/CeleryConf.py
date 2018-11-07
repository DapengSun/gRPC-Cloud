# coding:utf-8
from datetime import timedelta
from celery.schedules import crontab

BROKER_URL = 'redis://localhost:6379/4'

CELERY_RESULT_BACKEND = 'redis://localhost:6379/5'

CELERY_TIMEZONE = 'Asia/Shanghai'

CELERY_IMPORTS = (
    'Log.LogHelper_Client',
    'SSO.SSOVerifyUrl_Client',
    'SSO.SSOVerifyLogin_Client'
)