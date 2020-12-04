from typing import Type, Optional
import validators
from application.command.chat_bot_commands import run_download_and_upload_task_command

class TextCommandTranslator:

    command_map = {

    }

    def decode_command(self, command: str) -> Optional[Type]:
        # 先確認是否為網址，如果是網址，就啟動下載任務
        if validators.url(command):
            return run_download_and_upload_task_command
        else:
            return self.command_map.get(command)