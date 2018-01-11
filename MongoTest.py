import os
import sys
import pandas as pd
import numpy as np
os.chdir('Z:\williamyizhu On My Mac\Documents\workspace\PyTest')
sys.path.append(os.path.join(os.path.abspath('..'), 'PyShare\\PyShare'))
sys.path.append(os.path.join(os.path.abspath('..'), 'PyShare\\PricingModel'))
sys.path.append(os.path.join(os.path.abspath('..'), 'PyShare\\VolatilityModel'))
sys.path.append(os.path.join(os.path.abspath('..'), 'PyShare\\OptionAnalysis'))
import Mongo
import datetime as dt
import matplotlib.pyplot as plt
import pymongo
    
# ------------------------ drop collection ------------------------
mongo_path = os.path.join(os.path.abspath('..'), 'PyShare', 'config', 'mongodb_connection.ini')
mdb = Mongo.MongoDB(mongo_path)
mdb.connect('ctp_mongodb2')

mdb.connect('ctp_mongodb2')
result = mdb.db['DCE.M1801-P-2750'].find().sort([('_id', pymongo.DESCENDING)]).limit(5)
for doc in result:
    print(doc)


result = mdb.db['DCE.M1709-C-2800'].distinct('TradingDay')


# ------------------------ drop collection ------------------------
cnt = 0
for collection in mdb.db.collection_names(include_system_collections=False):
    if 'SSE.xxxxxx' in collection:
        cnt += 1
        print('drop collection', collection)
#         mdb.db.drop_collection(collection)
print(cnt)


mdb.connect('ctp_mongodb2')
for idx in mdb.db['CFFEX.IF1709'].list_indexes():
    print(idx)
# ------------------------ drop index ------------------------
for collection in mdb.db.collection_names(include_system_collections=False):
    idx = 'TradingDay_1'
    if idx in mdb.db[collection].index_information().keys():
        print('drop index', idx, 'on collection', collection)
        mdb.db[collection].drop_index(idx)
        
        

#     def drop_index(self, name):
#         for collection in self.db.collection_names(include_system_collections=False):
#             
# #             print(self.client.database_names())
# #             print(self.db.name)
# #             print(type(self.db))
#             
# #             print('.'.join([self.db.name,collection]))
# #             xx = self.db.system.indexes.find({'name':name, 'ns':'.'.join([self.db.name,collection])})
#             
#             xx = self.db[collection].list_indexes().find({'name':name, 'ns':'.'.join([self.db.name,collection])})
#             print(xx)
#             
# #             print(xx, '.'.join([self.db.name,collection]))
#             
# #             if(self.db.system.indexes.find({name:'indexname', ns:{$regex:'.collection$'}}).count()==0) { 
# #                 db.collection.createIndex({blah:1},{name:'indexname'}) 
# #             }
#             
#             
# #             tt = self.db[collection].list_indexes()
# #             print(collection, tt)
# #             for cur in tt:
# #                 print(cur)
#             
# #             result = self.db[collection].drop_index(name)
# #             print(collection, result)



cond_dict = {'$or':[{'BID':{'$gt':1e32}}, 
                    {'ASK':{'$gt':1e32}}, 
                    {'BVOL':10},
                    {'AVOL':0}
                    ]}
mdb.find(cond_dict)





mdb.client.database_names()
mdb.db.collection_names()
mdb.db.command('usersInfo')

mdb.client['testdb'].command('usersInfo')

# mdb.client.drop_database('zzzdb')

mdb.client['CtpData'].add_user(name='testuser1', password='123456', read_only=True)


mdb.client['testdb'].remove_user('userdev')


import sys
 
print('Number of arguments:', len(sys.argv), 'arguments.')
# sys.exit()
print('Argument List:', str(sys.argv[1:]))

print(sys.argv[1].split())
 
s = 'a,b,c'
s.split(',')

import pymongo

# create connection to mongodb
client2 = pymongo.MongoClient('mongodb://root:Xhmz372701@114.55.54.144:3718')
client1 = pymongo.MongoClient('mongodb://root:Xhmz372701@114.55.54.144:3717')
# client = pymongo.MongoClient('mongodb://root:Xhmz372701@114.215.252.135:3718')
client4 = pymongo.MongoClient('mongodb://root:Xhmz372701@dds-bp1affea778ad1841.mongodb.rds.aliyuncs.com:3717')
# client = pymongo.MongoClient('mongodb://root:Xhmz372701@dds-bp1affea778ad1842.mongodb.rds.aliyuncs.com:3718')

# individual collection for each contract
db = client2["WindDataCnFutures"]

try:
    if client4.is_primary:
        print('ok')
    else:
        print('not ok')
except:
    print('mongodb connection error')



import numpy as np
import datetime as dt
import time
import pytz

# create connection to mongodb

# client = pymongo.MongoClient('mongodb://root:Xhmz372701@dds-bp1affea778ad1842.mongodb.rds.aliyuncs.com:3717,dds-bp1affea778ad1841.mongodb.rds.aliyuncs.com:3717/admin?replicaSet=mgset-1401299',maxPoolSize=100)

client = pymongo.MongoClient('mongodb://root:Xhmz372701@114.55.54.144:3717', maxPoolSize=100)
client = pymongo.MongoClient('mongodb://root:Xhmz372701@114.55.54.144:3718', maxPoolSize=100)

# client = pymongo.MongoClient('mongodb://root:Xhmz372701@114.215.252.135:3717', maxPoolSize=100)
# client = pymongo.MongoClient('mongodb://root:Xhmz372701@114.215.252.135:3718', maxPoolSize=100)

print(client.is_primary)

client.close()


# client.server_info()

# client.close()

# ------------------------ intraday data query ------------------------
# _id, BID, ASK, BVOL, AVOL, LAST, VOLUME, OI, PRICE, CTPTIME, TradingDay
# verify PRICE, only need 1 data point
db = client['CtpData']
for collection in db.collection_names(include_system_collections=False):
#     print(collection)
    key = 'PRICE'
    cursor = db[collection].find({'$or':[{'key':0}, {'key':np.nan}, {'key':{'$gt':1e32}}]})
    if cursor.count()!=0:
        print(key, collection, cursor.count())

# ------------------------ eod query ------------------------
# _id, OPEN, HIGH, LOW, CLOSE, SETTLE, VOLUME, OI, DATETIME
# verify OPEN, HIGH, LOW, CLOSE, need 4 data point
db = client['WindDataCnFutures']
for collection in db.collection_names(include_system_collections=False):
    if 'eod' in collection:
#         print(collection)
        key = 'OPEN'
        cursor = db[collection].find({'$or':[{key:0}, {key:np.nan}, {key:{'$gt':1e32}}]})
        if cursor.count()!=0:
            print(key, collection, cursor.count())

# ------------------------ other time frame query ------------------------
# _id, OPEN, HIGH, LOW, CLOSE, VOLUME, OI, DATETIME
db = client['WindDataCnFutures']
for collection in db.collection_names(include_system_collections=False):
    if '60' in collection:
#         print(collection)
        key = 'OPEN'
        cursor = db[collection].find({'$or':[{key:0}, {key:np.nan}, {key:{'$gt':1e32}}]})
        if cursor.count()!=0:
            print(collection, cursor.count())

# ------------------------ remove nan value ------------------------
db = client['WindDataCnFutures']
for collection in db.collection_names(include_system_collections=False):
#     cursor = db[collection].find({
#         '$or':[{'DATETIME':np.nan}, 
#                {'OPEN':np.nan}, 
#                {'HIGH':np.nan},
#                {'LOW':np.nan},
#                {'CLOSE':np.nan},
#                {'SETTLE':np.nan},
#                {'VOLUME':np.nan},
#                {'OI':np.nan}
#                ]})
#     print(collection, cursor.count())

    result = db[collection].delete_many({
        '$or':[{'DATETIME':np.nan}, 
               {'OPEN':np.nan}, 
               {'HIGH':np.nan},
               {'LOW':np.nan},
               {'CLOSE':np.nan},
               {'SETTLE':np.nan},
               {'VOLUME':np.nan},
               {'OI':np.nan}
               ]})
    print(collection, result.deleted_count)



gg = db['CFFEX.IC1703'].index_information()


# # ------------------------ remove documents ------------------------
# dd = dt.datetime.today() + dt.timedelta(days=-14)
# # dd = dt.datetime.strptime('2016-11-22 18:00:35', '%Y-%m-%d %H:%M:%S')
# 
# isodate = pytz.timezone('Asia/Shanghai').localize(dd)    
# 
# db = client['CtpData']
# for collection in db.collection_names(include_system_collections=False):
#     cursor = db[collection].find({'CTPTIME':{'$lt':isodate}})
#     result = db[collection].delete_many({'CTPTIME':{'$lt':isodate}})
#     
#     print('collection:', collection, '| before:', id, '| found obs:', cursor.count(), '| removed:', result.deleted_count)
# 
# 
# for x in cursor[0:5]:
#     print(x)

    
# ------------------------ sdd ------------------------
sdd = {'_id':dt.datetime.today(),
       'BID':1.0, 'ASK':2e308, 'BVOL':3, 'AVOL':4,
       'LAST':5, 'VOLUME':6, 'OI':np.nan}
for k, v in sdd.items():
    print(k, type(v))

       
       
        
#             'CTPTIME':dt.datetime.strptime(' '.join([tk.getTradingDay(),tk.getUpdateTime(),str(tk.getUpdateMillisec())]),'%Y%m%d %H:%M:%S %f')}

# 
# import datetime
# import pytz

# 
# date_str = "2009-05-05 22:28:15"
# dd = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
# 
# mm=pytz.timezone('Asia/Shanghai').localize(dd)
# 
# 
# fmt = "%Y-%m-%d %H:%M:%S %Z%z"
# import datetime
# import pytz
# # Current time in UTC
# now_utc = datetime.datetime.now(pytz.timezone('UTC'))
# print(now_utc.strftime(fmt))
# print(now_utc.strftime('%Y-%m-%d %H:%M:%S'))
# 
# 
# datetime.datetime.utcnow()
# 
# 
# from datetime import datetime
# from pytz import timezone
# 
# date_str = "2009-05-05 22:28:15"
# datetime_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
# 
# 
# datetime_obj_utc = datetime_obj.replace(tzinfo=timezone('Asia/Shanghai'))
# print(datetime_obj_utc.strftime("%Y-%m-%d %H:%M:%S %Z%z"))
# 
# 
# 

# for x in cursor:
#     print(x)


# 
# 
# for i in pytz.all_timezones:
#     if 'Beijing' in i:
#         print(i)

# from datetime import datetime
# from pytz import timezone
# 
# date_str = "2014-05-28 22:28:15"
# datetime_obj_naive = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
# 
# # Right way!
# datetime_obj_pacific = timezone('Asia/Shanghai').localize(datetime_obj_naive)
# print(datetime_obj_pacific.strftime("%Y-%m-%d %H:%M:%S %Z%z"))


