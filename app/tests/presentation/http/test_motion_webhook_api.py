import pytest

from adapter.http import get_app

@pytest.mark.http
def test_on_new_record():

    app = get_app()
    client = app.test_client()

    response = client.post(
        'webhook/motion/record/new',
        json={
            'test': 'test_data'
        }
    )

    assert response.status_code == 200