# -*- coding: utf-8 -*-

import sys
sys.path.append('..')
from SSO.SSOVerifyUrl_Client import main

if __name__ == '__main__':
    task = main.delay('https://www.qq.com', 'adf84108d85211e89864559b0a5fbe9b')
    print(task.get())