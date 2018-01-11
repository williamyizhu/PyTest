import os
import sys
import pandas as pd
os.chdir('Z:\Documents\workspace\PyWind2')
mpath = os.path.join(os.path.abspath('..'), 'PyShare\\PyShare')
sys.path.append(mpath)
import Wind
import Mysql

# ------------- connect to rds -------------    
fpath = os.path.join(os.path.abspath('..'), 'PyShare', 'config', 'mysql_connection.ini')
rds = Mysql.MySqlDB(fpath)
rtn = rds.connect(rds.connection['rds_prod'])

mm, result = rds.execute('''SELECT * FROM model_params WHERE accountid=%s AND model='wing' AND modelinstance LIKE %s AND modelinstance LIKE %s ''', ('3', '%%otc%%', '%%rb1710%%'))

# sql = '''SELECT * FROM model_params WHERE accountid=%s AND model='wing' AND modelinstance LIKE '%%%s%%' AND modelinstance LIKE '%%%s%%' ''' % ('3', 'DCE', 'm1712')

# mm, result = rds.execute(sql, ())

mm, result = rds.execute('''SELECT * FROM model_params WHERE accountid=%s AND model='wing' ''', ('3'))

print(result)
modelinstance = set(result['modelinstance'])

modelinstance = pd.DataFrame({'modelinstance':list(set(result['modelinstance']))})
              
jj = modelinstance.apply(lambda x: x[0].split('-'), axis=1)

modelinstance.apply(lambda x: , axis=1)
            