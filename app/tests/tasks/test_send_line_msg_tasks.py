import pytest
from unittest.mock import patch
from tasks import send_line_msg_tasks as tasks

from linebot.models import TextSendMessage

@pytest.mark.celery
@pytest.mark.usefixtures('celery_session_app')
@pytest.mark.usefixtures('celery_session_worker')
@patch('linebot.LineBotApi.reply_message')
def test_set_text_message(mock_method):
    tasks.set_text_message('fake token', 'fake msg')
    mock_method.assert_called_once_with('fake token', TextSendMessage(text='fake msg'))