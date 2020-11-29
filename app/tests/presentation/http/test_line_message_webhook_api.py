import pytest
from mockito import when

from presentation.controllers.chatbot_api_controllers import LineCallbackController
from presentation.configure.chatbot_api_configure import FakeChatbotApiConfigure
from adapter.http import get_app

@pytest.fixture(scope="function")
def unstub():
    from mockito import unstub as mock_unstub
    yield
    mock_unstub()

def headers():
    return {
        'X-Line-Signature': 'fake-signature',
    }

@pytest.mark.http
def test_receive_callback(unstub):
    when(LineCallbackController).handle().thenReturn(True)

    config = FakeChatbotApiConfigure()
    app = get_app(chatbot_api_configure=config)
    client = app.test_client()

    response = client.post(
        '/webhook/line/message/callback',
        headers=headers(),
        data={
            'text': 'fake body'
        }
    )

    assert response.status_code == 200
    assert response.data == b'OK'