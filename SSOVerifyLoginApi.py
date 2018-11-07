# -*- coding: utf-8 -*-

import sys
sys.path.append('..')
from SSO import SSOVerifyLogin_Client
from Log import LogHelper_Client
from EnumType.CommonEnum import LogLevel
from RedisOper import oper

if __name__ == '__main__':
    try:
        task = SSOVerifyLogin_Client.main.delay('13520387252','123456')
        print(task.get())
        print(LogHelper_Client.main('SSO登录','SSO请求成功',LogLevel.INFO.value))
    except Exception as e:
        print(LogHelper_Client.main('SSO登录', 'SSO请求异常', LogLevel.ERROR.value))

