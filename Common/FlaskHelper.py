# -*- coding: utf-8 -*-
import json
from enum import Enum
from flask import Response

class responseStatus(Enum):
    Ok = 200
    AuthFailed = 400
    Error = 500

class tool(object):
    @staticmethod
    def jsonResult(Status,Message,Data):
        response = json.dumps({"Code" : Status.value,"Message" : str(Message),"Data" : Data},ensure_ascii=False)
        return Response(response=response,status=Status.value,content_type='text/plain;charset=utf8')