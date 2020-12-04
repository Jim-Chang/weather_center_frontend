from bs4 import BeautifulSoup
import requests
import asyncio

from utils.log import logging

domain = 'https://koding.work'

sitemap_post = domain + '/post-sitemap.xml'
sitemap_page = domain + '/page-sitemap.xml'
sitemap_category = domain + '/category-sitemap.xml'
sitemaps = [sitemap_post, sitemap_page, sitemap_category]

cv_urls = [
    'https://koding.work/cv-en/',
    'https://koding.work/cv-zh/',
]

sess = requests.Session()
sess.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

# 將 urls 切成等份
def split_urls(urls, page_max_urls_len=10):
    return [urls[i: i + page_max_urls_len] for i in range(0, len(urls), page_max_urls_len)]

# 取得所有網站上的 urls
def get_all_avaliable_urls():
    urls = parse_sitemap()
    urls += parse_contain_page_num(urls)
    return urls

# 從 sitemap 中抓 url
def parse_sitemap():
    tasks = []
    loop = asyncio.get_event_loop()

    for sitemap in sitemaps:
        tasks.append(asyncio.ensure_future(get_urls(sitemap + '?preview=true', loop)))

    task_results, _ = loop.run_until_complete(asyncio.wait(tasks))

    urls = []
    for task_result in task_results:
        urls += task_result.result()

    return urls + cv_urls

async def get_urls(sitemap_url, loop):
    result = []
    logging.info('start get {}'.format(sitemap_url))
    r = await loop.run_in_executor(None, sess.get, sitemap_url)
    
    soup = BeautifulSoup(r.text, 'html.parser')    
    for loc in soup.find_all('loc'):
        url = loc.string
        
        if domain in url:
            result.append(url)

    logging.info('parse finish {}'.format(sitemap_url))
    return result

# 從有分頁的網頁中爬出分頁 urls
def parse_contain_page_num(root_urls):
    tasks = []
    loop = asyncio.get_event_loop()

    root_urls = list(set(root_urls))
    for root_url in root_urls:
        if 'category' in root_url or 'https://koding.work/' == root_url:
            tasks.append(asyncio.ensure_future(get_contain_page_num_url(root_url + '?preview=true', loop)))

    task_results, _ = loop.run_until_complete(asyncio.wait(tasks))

    urls = []
    for task_result in task_results:
        urls += task_result.result()
    
    logging.info('find {} urls about page nums'.format(len(urls)))
    return urls

async def get_contain_page_num_url(root_url, loop):
    result = []
    logging.info('start find page num url of {}'.format(root_url))
    r = await loop.run_in_executor(None, sess.get, root_url)

    soup = BeautifulSoup(r.text, 'html.parser') 
    for a in soup.find_all('a', {'class': 'page'}):
        result.append(a.get('href').replace('?preview=true', ''))

    return result



