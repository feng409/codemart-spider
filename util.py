import logging

import yagmail
from config import EMAIL_ACCOUNT, EMAIL_HOST, EMAIL_NOTIFY, EMAIL_PASSWORD


logging.basicConfig(level=logging.DEBUG)
_logger = logging.getLogger(__name__)


smtp = yagmail.SMTP(user=EMAIL_ACCOUNT, password=EMAIL_PASSWORD, host=EMAIL_HOST)


def send_mail(title, description):
    _logger.info('发送邮件 -> %s ', title)
    smtp.send(EMAIL_NOTIFY, subject=title, contents=description)


if __name__ == '__main__':
    pass
