# -*- coding: utf-8 -*-

import pymysql

dbArgs = {'host':'localhost','user':'root','password':'sdmp','db':'spider','port':3306}
db = pymysql.connect(**dbArgs)
cursor = db.cursor()
