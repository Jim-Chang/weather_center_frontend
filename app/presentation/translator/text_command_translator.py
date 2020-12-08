from typing import Type, Optional
import validators
from application.command.chat_bot_commands import (
    run_download_and_upload_task_command,
    run_refresh_cache_for_wp_command,
    run_get_stock_price_command,
)

class TextCommandTranslator:

    # <command_key>: <command_func>
    command_map = {
        '刷新部落格': run_refresh_cache_for_wp_command,
        '股票': run_get_stock_price_command,               # 指令範例 '股票 0050.tw' 
    }

    def decode_command(self, command: str) -> Optional[Type]:
        # 先確認是否為網址，如果是網址，就啟動下載任務
        if validators.url(command):
            return run_download_and_upload_task_command
        else:
            commands = command.split(' ')
            return self.command_map.get(commands[0])