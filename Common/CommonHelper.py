# -*- coding: utf-8 -*-
import uuid
import json
from enum import Enum

from django.http import JsonResponse, HttpResponse


class ResponseStatus(Enum):
    Ok = 200,
    AuthFailed = 400,
    Error = 500

class Tool(object):
    @staticmethod
    def GetGuid():
        return uuid.uuid1()

    @staticmethod
    def Json(ResponseStatus,Message,Data):
        return {"Code":ResponseStatus.value,"Message":Message,"Data":Data}

    @staticmethod
    def JsonResult(ResponseStatus,Message,Data):
        response_data = {}
        response_data['Code'] = ResponseStatus.value
        response_data['Message'] = Message
        response_data['Data'] = Data
        response = HttpResponse(JsonResponse(response_data), content_type="application/json; charset=utf-8")
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        response["Access-Control-Allow-Credentials"] = "true"
        return response
