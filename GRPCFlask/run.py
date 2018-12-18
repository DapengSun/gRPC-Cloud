# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
from flask import Flask
from flask_docs import ApiDoc
from flask_restful import Resource, Api
from GRPCFlask.LogFlask import logModule

app = Flask(__name__)
app.register_blueprint(logModule,url_prefix='/v1/log')

app.config['API_DOC_MEMBER'] = ['api', 'platform']
# 需要排除的 RESTful Api 文档
app.config['RESTFUL_API_DOC_EXCLUDE'] = []
# restful_api = Api(app)
# ApiDoc(app)


if __name__ == '__main__':
   #app.run(debug = True)
   app.run()