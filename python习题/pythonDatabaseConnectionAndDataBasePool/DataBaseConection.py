"""
    建立数据库连接池，减少数据库反复连接的消耗
    DBUtils提供了两种外部接口
        PersistentDB:提供线程专用的数据库的连接，自动管理连接
        PooledDB: 提供线程之间可共享数据库的连接。并自动管理
    dbapi:数据库接口
    mincached:启动时开启时的空连接数
    maxcached：连接池开启的最大连接数
    maxshared：连接池最大的可共享连接数量
    maxconnections：最大允许连接数量
    blocking:达到最大数量是否阻塞
    maxusage：单个连接最大复用次数

"""

import pymysql

db  = pymysql.connect("localhost", "root", "123456", "seckill")

cursor = db.cursor()

cursor.execute('select * from seckill')

data = cursor.fetchall()

print(data)

db.close()

