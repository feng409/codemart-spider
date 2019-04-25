'''
# =============================================================================
#      FileName: code_schedule.py
#          Desc: 定时器检查数据库
#        Author: chemf
#         Email: eoyohe@gmail.com
#      HomePage: eoyohe.cn
#       Version: 0.0.1
#    LastChange: 2019-04-22 13:01:31
#       History:
# =============================================================================
'''
from db_tool import db_doc
from util import send_work_mail, _logger


key_words = ['python', 'flask', 'django']


def find_work(doc):
    if doc.get('roles', '') == '后端开发':
        return True
    if any(word in doc.get('description', '') or word in doc.get('name', '') for word in key_words):
        return True
    return False


def work_schedule():
    unlikes = db_doc.find({'like': {'$not': {'$exists': True}}})
    _logger.info('新增了 -> %s', unlikes.count())
    for job in unlikes:
        if find_work(job):
            send_work_mail(job['name'], job['description'], job['id'])
        job['like'] = True
        db_doc.update_one({'id': job['id']}, {'$set': {'like': True}})


if __name__ == '__main__':
    work_schedule()
