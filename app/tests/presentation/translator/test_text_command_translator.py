import pytest
from presentation.translator.text_command_translator import TextCommandTranslator

from application.command.chat_bot_commands import run_download_and_upload_task_command


def test_text_command_translator__decode_command__is_url():
    t = TextCommandTranslator()
    assert t.decode_command('https://google.com') is run_download_and_upload_task_command

def test_text_command_translator__decode_command__command_not_found():
    t = TextCommandTranslator()
    assert t.decode_command('fake command') is None