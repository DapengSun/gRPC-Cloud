# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals
import os
import sys
sys.path.append('..')
from Log.LogHelper_Client import main
from EnumType import CommonEnum

if __name__ == '__main__':
    task = main.delay('1m','2m',CommonEnum.LogLevel.INFO.value)
    print(task.get())

    # print(main('1m','2m'))



