# -*- coding: utf-8 -*-

import pymysql

db = pymysql.connect(host='localhost',user='root',password='sdmp',db='spider',port=3306)
cursor = db.cursor()
