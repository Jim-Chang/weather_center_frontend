import pytest
from presentation.translator.text_command_translator import TextCommandTranslator

from application.command.chat_bot_commands import (
    run_download_and_upload_task_command,
    run_refresh_cache_for_wp_command,
    run_get_stock_price_command,
)

@pytest.mark.in_memory
def test_text_command_translator__decode_command__command_not_found():
    t = TextCommandTranslator()
    assert t.decode_command('fake command') is None

@pytest.mark.in_memory
def test_text_command_translator__decode_command__is_url():
    t = TextCommandTranslator()
    assert t.decode_command('https://google.com') is run_download_and_upload_task_command

@pytest.mark.in_memory
def test_text_command_translator__decode_command__refresh_cache_for_wp():
    t = TextCommandTranslator()
    assert t.decode_command('刷新部落格') == run_refresh_cache_for_wp_command

@pytest.mark.in_memory
def test_text_command_translator__decode_command__get_stock_price():
    t = TextCommandTranslator()
    assert t.decode_command('股票 0050.tw') == run_get_stock_price_command

