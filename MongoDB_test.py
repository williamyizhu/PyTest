import pymongo
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

# ------------------------ drop index ------------------------
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


# ------------------------ drop collection ------------------------
db = client['WindDataCnFutures']
for collection in db.collection_names(include_system_collections=False):
    if '_eod' in collection:
        print('dropping', collection)
#         time.sleep(1)
#         db.drop_collection(collection)

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


db = client['CtpData']
index = 'TradingDay'
for collection in db.collection_names(include_system_collections=False):
    print(collection, 'create index', index)
    db[collection].create_index([(index, pymongo.ASCENDING)])



db['CFFEX.IC1700'].create_index([(index, pymongo.ASCENDING)])

gg = db['CFFEX.IC1703'].index_information()

'TradingDay_1' in gg.keys()



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

