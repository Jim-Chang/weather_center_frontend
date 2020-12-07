import pytest
from unittest.mock import patch
from tasks import send_line_msg_tasks as tasks

from linebot.models import TextSendMessage

@pytest.mark.celery
@pytest.mark.usefixtures('celery_session_app')
@pytest.mark.usefixtures('celery_session_worker')
@patch('linebot.LineBotApi.push_message')
def test_send_text_message(mock_method):
    tasks.send_text_message('fake user id', 'fake msg')
    mock_method.assert_called_once_with('fake user id', TextSendMessage(text='fake msg'))

@patch('tasks.send_line_msg_tasks.send_text_message.apply_async')
def test_async_send_text_message(mock_method):
    tasks.async_send_text_message('fake user id', 'fake msg')
    mock_method.assert_called_once()

@pytest.mark.celery
@pytest.mark.usefixtures('celery_session_app')
@pytest.mark.usefixtures('celery_session_worker')
@patch('linebot.LineBotApi.push_message')
def test_send_multi_text_message(mock_method):
    tasks.send_multi_text_message('fake user id', ['fake msg 1', 'fake msg 2'])
    mock_method.assert_called_once_with('fake user id', [TextSendMessage(text='fake msg 1'), TextSendMessage(text='fake msg 2')])

@patch('tasks.send_line_msg_tasks.send_multi_text_message.apply_async')
def test_async_send_multi_text_message(mock_method):
    tasks.async_send_multi_text_message('fake user id', ['fake msg 1', 'fake msg 2'])
    mock_method.assert_called_once()