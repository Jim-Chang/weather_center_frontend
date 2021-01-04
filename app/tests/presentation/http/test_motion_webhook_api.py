import pytest
from unittest.mock import patch

from adapter.http import get_app

@pytest.mark.http
@patch('tasks.send_line_msg_tasks.send_text_message.apply_async')
def test_on_new_record(mock_method):

    app = get_app()
    client = app.test_client()

    response = client.post(
        'webhook/motion/record/new',
        json={
            'filename': '/var/lib/motioneye/Camera1/2021-01-04/12-16-03.mp4'
        }
    )

    assert response.status_code == 200
    mock_method.assert_called_once_with(args=('Uebaac5edfee64f6b934a4d27b937cead', 'Camera1 偵測到動靜！\n日期：2021-01-04\n錄影檔名：12-16-03.mp4'))