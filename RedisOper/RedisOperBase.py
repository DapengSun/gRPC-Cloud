# -*- coding: utf-8 -*-
import datetime
import json
import sys
sys.path.append('..')
import abc
import hashlib
import pymysql
from RedisOper import oper

class redisOperBase(metaclass=abc.ABCMeta):
    def getSqlVal(self,sql,expires=0,**dbArgs):
        '''
        获取SQL值
        :param sql: 查询SQL语句
        :param expires: 默认key超时时间
        :param dbArgs:数据库连接参数
        :return:
        '''
        if not sql:
            return
        # 根据sql 通过MD5加密生成的Key
        key = self.createSqlKey(sql = sql)
        # 根据key 获取Redis值 命中-返回值 未命中设置
        res = self.getRedisData(key)

        # 缓存命中 返回结果
        if res != None:
            return res
        else:
            # 连接数据库 查询SQL结果
            db = pymysql.connect(**dbArgs)
            cursor = db.cursor()
            cursor.execute(sql)
            # 数据库字段描述
            description = [i[0] for i in cursor.description]
            # SQL结果
            resList = [dict(zip(description, i)) for i in cursor.fetchall()]
            res = json.dumps(resList,cls=CJsonEncoder)
            if res != '[]':
                self.getRedisData(key=key, val=res, expires=expires)
            cursor.close()
            return res

    @abc.abstractmethod
    def getRedisData(self,key = None,val = None,expires = 0):
        '''
        基类获取Redis数据并缓存的抽象方法
        :param key:redis key
        :param val:redis value
        :param expires:key 超时时间
        :return:
        '''
        pass

    def createSqlKey(self, sql):
        '''
        根据sql 通过MD5加密生成的Key
        :return:
        '''
        key = hashlib.md5(sql.encode(encoding = 'UTF-8')).hexdigest()
        return key

class redisOper(redisOperBase):
    '''
    缓存redis操作
    '''
    def getRedisData(self,key = None,val = None,expires = 0):
        '''
        实现-基类获取Redis数据并缓存的方法
        :param key:redis key
        :param val:redis value
        :param expires:key 超时时间
        :return:
        '''
        try:
            if key == None:
                return
            # 获取Redis key的value
            if val == None:
                return oper.strGet(key)
            # 设置Redis key的value
            else:
                oper.strSet(key,val)
                if expires != 0:
                    oper.setKeyExpires(key,expires)
        except Exception as ex:
            print(ex)


class CJsonEncoder(json.JSONEncoder):
    '''
    json.dumps的自定义处理 解决datetime无法序列化问题
    '''
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)

if __name__ == '__main__':
    sql = 'select LoginName,NickName,PassWord,Phone,CDate,Email from accountinfo'
    redisOper = redisOper()
    dbArgs = {'host':'localhost','user':'root','password':'sdmp','db':'spider','port':3306}
    res = redisOper.getSqlVal(sql,expires=60000,**dbArgs)
    print(res)