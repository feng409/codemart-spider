'''
# =============================================================================
#          Desc: codemart爬虫
#        Author: chemf
#         Email: eoyohe@gmail.com
#      HomePage: eoyohe.cn
#       Version: 0.0.1
#    LastChange: 2019-04-21 14:02
#       History: 
# =============================================================================
'''
import asyncio
import time

from fake_useragent import UserAgent
import aiohttp

from db_tool import save_documents
from util import _logger

ua = UserAgent()

headers = {
    'Accept': 'application/json;charset=UTF-8',
    'Host': 'codemart.com',
    'Pragma': 'no-cache',
    'User-Agent': ua.random,
}

base_url = 'https://codemart.com/api/project?page={page}&&sort=PUBLISH_TIME'

charles_proxies = {
    "http": "http://localhost:2333",
    "https": "https://localhost:2333",
}


async def get_content(session, url):
    async with session.get(url, headers=headers) as response:
        if response.status == 200:
            data = await response.json()
            pager, rewards = data['pager'], data['rewards']
            return pager, rewards
        else:
            _logger.warning('error code-> ', response.status_code)
            _logger.warning('error url -> ', response.url)
            return None, None


async def spider():
    page = 1
    async with aiohttp.ClientSession() as session:
        while True:
            _logger.debug('正在爬取 %s 页', page)
            pager, rewards = await get_content(session, base_url.format(page=page))
            save_documents(rewards)

            if pager['page'] >= pager['totalPage']:
                break
            page = page + 1


if __name__ == '__main__':
    now = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(spider())
    print('use time -> ', time.time() - now)

