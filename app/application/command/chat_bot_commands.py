from linebot.models import Event

def run_download_and_upload_task_command(event: Event):
    from tasks.download_and_upload_task import async_do_download_and_upload_task

    async_do_download_and_upload_task(event.source.user_id, event.message.text)

def run_refresh_cache_for_wp_command(event: Event):
    from tasks.refresh_cache_for_wp_task import async_refresh_cache_for_wp_task

    async_refresh_cache_for_wp_task(event.source.user_id)