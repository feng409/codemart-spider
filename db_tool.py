'''
# =============================================================================
#      FileName: db_tool.py
#          Desc: 数据库
#        Author: chemf
#         Email: eoyohe@gmail.com
#      HomePage: eoyohe.cn
#       Version: 0.0.1
#    LastChange: 2019-04-22 13:00:08
#       History:
# =============================================================================
'''
import pymongo
from pymongo.collection import Collection
from pymongo.database import Database


client = pymongo.MongoClient('localhost', 27017)
db: Database = client.codemart
db_doc: Collection = db.work1


def save_documents(documents):
    for doc in documents:
        db_doc.update_one(dict(id=doc['id']), {'$set': doc}, upsert=True)


__ALL__ = {
    'client', 'db_doc', 'db'
}
