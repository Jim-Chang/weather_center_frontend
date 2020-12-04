import pytest
from mockito import when
from unittest.mock import patch
from linebot.webhook import SignatureValidator

from presentation.controllers.chatbot_api_controllers import LineCallbackController


@pytest.fixture(scope="function")
def unstub():
    from mockito import unstub as mock_unstub
    yield
    mock_unstub()

@pytest.fixture(scope="function")
def stub_line_signature_validator():
    when(SignatureValidator).validate(...).thenReturn(True)
    yield


@pytest.mark.in_memory
@patch('presentation.controllers.chatbot_api_controllers.LineCallbackController._dispatch_command')
def test_line_callback_controller__text_message(mock_method, stub_line_signature_validator, unstub):
    with open('tests/files/line__text_message.json', 'r') as f:
        data = f.read()

    controller = LineCallbackController(data, '')
    assert controller.handle() is True
    mock_method.assert_called_once()

# @pytest.mark.in_memory
# @patch('tasks.send_line_msg_tasks.async_send_text_message')
# def test_line_callback_controller__image_message(mock_method, stub_line_signature_validator, unstub):
#     with open('tests/files/line__image_message.json', 'r') as f:
#         data = f.read()

#     controller = LineCallbackController(data, '')
#     assert controller.handle() is True
#     mock_method.assert_called_once_with('U4af4980629...', '這個我還看不懂所以略過哦')