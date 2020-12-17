import requests
import asyncio
import time
from application.wordpress.parse_sitemap import get_all_avaliable_urls, split_urls

from utils.log import logging

aws_lambda_url = 'https://nffnrzmc75.execute-api.us-west-2.amazonaws.com/v1/{}'

sess = requests.Session()
sess.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

async def start_request(url, loop):
    t = time.time()
    r = await loop.run_in_executor(None, sess.get, url)
    total_time = int((time.time() - t) * 1000)
    logging.info('prefetch finish => cache status: {}, age: {}, response time: {}ms, url: {}'.format(r.headers.get('cf-cache-status'), r.headers.get('age'), total_time, url))

def start_preload(urls=[]):
    if urls == []:
        urls = get_all_avaliable_urls()

    tasks = []
    loop = asyncio.get_event_loop()
    
    for paged_urls in split_urls(urls, page_max_urls_len=20):
        logging.info('preload 20 batch start')
       
        for url in paged_urls:
            tasks.append(asyncio.ensure_future(start_request(url, loop)))
        
        loop.run_until_complete(asyncio.wait(tasks))

    logging.info('finish')

def start_aws_lambda_preload():
    logging.info('trigger us-east')
    sess.get(aws_lambda_url.format('/us-east'))

    logging.info('trigger us-west')
    sess.get(aws_lambda_url.format('/us-west'))

    logging.info('trigger eu-west')
    sess.get(aws_lambda_url.format('/eu-west'))

    logging.info('trigger eu-central')
    sess.get(aws_lambda_url.format('/eu-central'))

    logging.info('trigger ap-southeast')
    sess.get(aws_lambda_url.format('/ap-southeast'))
