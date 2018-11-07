# -*- coding: utf-8 -*-

from celery import Celery

app = Celery('GRPCSpiderCelery')

app.config_from_object('CeleryConf.CeleryConf')