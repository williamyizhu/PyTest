import os
import sys
# import shutil
# import argparse
os.chdir('Z:\williamyizhu On My Mac\Documents\workspace\PyTest')
# mpath = os.path.join(os.path.abspath('..'), 'PyShare\\PyShare')
# sys.path.append(mpath)
import Mongo


mongo_path = os.path.join(os.path.abspath('..'), 'PyShare', 'config', 'mongodb_connection.ini')
mdb = Mongo.MongoDB(mongo_path)
mdb.connect(mdb.connection['_'.join(['wind_mongodb1'])])

mdb.client.database_names()

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



