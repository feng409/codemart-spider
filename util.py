import logging

import yagmail
from config import EMAIL_ACCOUNT, EMAIL_HOST, EMAIL_NOTIFY, EMAIL_PASSWORD


logging.basicConfig(level=logging.DEBUG)
_logger = logging.getLogger(__name__)


smtp = yagmail.SMTP(user=EMAIL_ACCOUNT, password=EMAIL_PASSWORD, host=EMAIL_HOST)


def send_work_mail(title, description, id):
    html = '<a href="https://codemart.com/project/%s">点击前往</a>' % id
    send_mail(title, [description, html])

def send_mail(title, description):
    _logger.info('发送邮件 -> %s ', title)
    smtp.send(EMAIL_NOTIFY, subject=title, contents=description)


if __name__ == '__main__':
    title = 'test'
    desc = 'hello world\n'
    id = 18501

    send_work_mail(title, desc, id)
    pass
