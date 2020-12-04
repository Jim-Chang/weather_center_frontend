import requests
from application.wordpress.parse_sitemap import get_all_avaliable_urls, split_urls

from utils.log import logging

api_url = 'https://api.cloudflare.com/client/v4/zones/{}/purge_cache'
zone_identify = '9a0d41a726a0d8d26d815cbfe9a2d852'
email = 'dorajim15@gmail.com'
token = '66394b05b8035d6387037e478a2447d76f6e1'


def purge_cache(urls=[]):
    if urls == []:
        urls = get_all_avaliable_urls()

    logging.info('purge cache...')
    for paged_urls in split_urls(urls):
        #logging.info('will purge: ', paged_urls)
        r = requests.post(
            api_url.format(zone_identify),
            headers={
                'X-Auth-Email': email,
                'X-Auth-Key': token
            },
            json={
                'files': paged_urls,
            }
        )
        logging.info('result {}'.format(r.json()))


if __name__ == "__main__":
    purge_cache()

