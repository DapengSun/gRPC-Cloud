#coding:utf-8

import redis
import time
from EnumType import CommonEnum
import sys
sys.path.append('..')
# from RedisOper import db
from RedisOper.RedisOperBase import redisOperBase

class RedisOperHelper(redisOperBase):
    def __init__(self,db):
        # pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
        # self.db = redis.Redis(connection_pool=pool)
        self.db = db

    # Str操作
    # set 设置str值
    def strSet(self, key,val):
        return self.db.set(key,val)

    # get 返回str值
    def strGet(self, key):
        return self.db.get(key)

    # 获取所有执行的key值
    def keys(self,pattern):
        return self.db.keys(pattern)

    # 删除执行的key
    def delKeys(self,*names):
        return self.db.delete(*names)

    # List操作
    # 返回队列里面list内元素的数量
    def queueSize(self,key):
        return self.db.llen(key)

    # 向list中加入元素
    def queuePut(self,key,item):
        self.db.rpush(key,item)

    # 返回list中元素
    def queueGetNoWait(self,key):
        # 直接返回队列第一个元素，如果队列为空返回的是None
        return self.db.lpop(key)

    # 返回list中元素（等待）
    def queueGetWait(self,key, timeout=None):
        # 返回队列第一个元素，如果为空则等待至有元素被加入队列（超时时间阈值为timeout，如果为None则一直等待）
        item = self.db.blpop(key, timeout=timeout)
        return item

    # Hash操作
    # Hlen 命令用于获取哈希表中字段的数量。哈希表中字段的数量。 当 key 不存在时，返回 0 。
    def hashHlen(self,key):
        return self.db.hlen(key)

    # Hset 命令用于为哈希表中的字段赋值 。如果哈希表不存在，一个新的哈希表被创建并进行 HSET 操作。如果字段已经存在于哈希表中，旧值将被覆盖。
    # 如果字段是哈希表中的一个新建字段，并且值设置成功，返回 1 。 如果哈希表中域字段已经存在且旧值已被新值覆盖，返回 0 。
    def hashHset(self,name,key,value):
        return self.db.hset(name,key,value)

    # Hget 命令用于返回哈希表中指定字段的值。返回给定字段的值。如果给定的字段或 key 不存在时，返回 None 。
    def hashHget(self,name,key):
        return self.db.hget(name,key)

    # Hgetall 命令用于返回哈希表中，所有的字段和值。在返回值里，紧跟每个字段名(field name)之后是字段的值(value)，
    # 所以返回值的长度是哈希表大小的两倍。
    def hashHgetAll(self,name):
        return self.db.hgetall(name)

    # Hexists 命令用于查看哈希表的指定字段是否存在。如果哈希表含有给定字段，返回 True。
    # 如果哈希表不含有给定字段，或 key 不存在，返回False 。
    def hashHexists(self,name,key):
        return self.db.hexists(name,key)

    # Hincrby 命令用于为哈希表中的字段值加上指定增量值。
    # 增量也可以为负数，相当于对指定字段进行减法操作。
    # 如果哈希表的key不存在，一个新的哈希表被创建并执行HINCRBY命令。
    # 如果指定的字段不存在，那么在执行命令前，字段的值被初始化为0 。
    # 对一个储存字符串值的字段执行HINCRBY命令将造成一个错误。
    def hashHincrby(self,name,key,amount):
        return self.db.hincrby(name,key,amount)

    # Hincrbyfloat 命令用于为哈希表中的字段值加上指定浮点数增量值。
    # 如果指定的字段不存在，那么在执行命令前，字段的值被初始化为 0
    def hashHincrbyFloat(self,name,key,amount):
        return self.db.hincrbyfloat(name,key,amount)

    # Hkeys 命令用于获取哈希表中的所有字段名。包含哈希表中所有字段的列表。
    # 当 key 不存在时，返回一个空列表。
    def hashKeys(self,name):
        return self.db.hkeys(name)

    # Hmset 命令用于同时将多个 field-value (字段-值)对设置到哈希表中,此命令会覆盖哈希表中已存在的字段。
    # 如果哈希表不存在，会创建一个空哈希表，并执行 HMSET 操作。
    def hashHmset(self,name,mapping):
        return self.db.hmset(name,mapping)

    # Hmget 命令用于返回哈希表中，一个或多个给定字段的值。如果指定的字段不存在于哈希表，那么返回一个 nil 值。
    # 一个包含多个给定字段关联值的表，表值的排列顺序和指定字段的请求顺序一样。
    def hashHmget(self,name,keys,*args):
        return self.db.hmget(name,keys,*args)

    # Hsetnx 命令用于为哈希表中不存在的的字段赋值 。
    # 如果哈希表不存在，一个新的哈希表被创建并进行 HSET 操作。
    # 如果字段已经存在于哈希表中，操作无效。
    # 如果 key 不存在，一个新哈希表被创建并执行 HSETNX 命令。
    # 设置成功，返回 1 。 如果给定字段已经存在且没有操作被执行，返回 0
    def hashHsetnx(self,name,key,value):
        return self.db.hsetnx(name,key,value)

    # Hvals 命令返回哈希表所有字段的值。一个包含哈希表中所有值的表。
    # 当 key 不存在时，返回一个空表。
    def hashHsetnx(self,name):
        return self.db.hvals(name)


    # Hdel 命令用于删除哈希表 key 中的一个或多个指定字段，不存在的字段将被忽略。
    def hashHdel(self,name,*key):
        return self.db.hdel(name,*key)

    # Incrby 命令将 key 中储存的数字加上指定的增量值
    # 如果 key 不存在，那么 key 的值会先被初始化为 0 ，然后再执行 INCRBY 命令。
    # 如果值包含错误的类型，或字符串类型的值不能表示为数字，那么返回一个错误。
    # 本操作的值限制在 64 位(bit)有符号数字表示之内。
    # 例如：作计数用途
    def incrby(self,name,key):
        return self.db.incrby(name,key)

    # HyperLogLog 提供了两个指令 pfadd 和 pfcount，根据字面意义很好理解，一个是增加计数，一个是获取计数。
    # pfadd 用法和 set 集合的 sadd 是一样的，来一个用户 ID，就将用户 ID 塞进去就是。
    # pfcount 和 scard 用法是一样的，直接获取计数值...
    # 例如：用来统计页面UV数量
    def pfadd(self,key,*values):
        return self.db.pfadd(key,*values)

    def pfcount(self,key):
        return self.db.pfcount(key)

    def pfmerge(self,key,*source):
        return self.db.pfmerge(key,*source)

    # 根据SQL生成Key Key - 使用MD5等方式加密生成Key
    def getSqlKey(self,sqlKey,sql):
        if sqlKey == CommonEnum.sqlKey.MD5:
            pass

    # 设置key的过期时间
    def setKeyExpires(self,key,expires):
        return self.db.expire(key,expires)

    def getRedisData(self, key=None, val=None, expires=0):
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
                return self.strGet(key)
            # 设置Redis key的value
            else:
                self.strSet(key, val)
                if expires != 0:
                    self.setKeyExpires(key, expires)
        except Exception as ex:
            print(ex)

if __name__ == '__main__':
    sql = 'select LoginName,NickName,PassWord,Phone,CDate,Email from accountinfo'
    import redis
    pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True, db=6)
    db = redis.Redis(connection_pool=pool)
    redisOper = RedisOperHelper(db)
    dbArgs = {'host':'localhost','user':'root','password':'sdmp','db':'spider','port':3306}
    res = redisOper.getSqlVal(sql,expires=60000,**dbArgs)
    print(res)