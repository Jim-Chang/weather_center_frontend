import time
from celery_app import app
from tasks.send_line_msg_tasks import send_text_message

from application.wordpress.preloader import start_preload
from application.wordpress.purge_cache import purge_cache
from application.wordpress.parse_sitemap import get_all_avaliable_urls

# do_download_and_upload_task 的包裝
def async_refresh_cache_for_wp_task(user_id: str):
    refresh_cache_for_wp_task.apply_async(args=(user_id,))

@app.task
def refresh_cache_for_wp_task(user_id: str):
    send_text_message(user_id, '開始刷新 KodingWork 的 Cloudflare cache\n\n正取得所有可用網址')
    urls = get_all_avaliable_urls()

    send_text_message(user_id, '正在清掉 Cloudflare cache')
    purge_cache(urls)

    send_text_message(user_id, '等待 30 秒')
    time.sleep(30)

    send_text_message(user_id, '開始 preload')
    start_preload(urls)

    send_text_message(user_id, '二次 preload')
    start_preload(urls)

    send_text_message(user_id, '刷新 KodingWork cache 完成！')