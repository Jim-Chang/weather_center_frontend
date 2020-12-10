import pytest
from mockito import when
from unittest.mock import patch
from linebot.models import Event
from linebot.models.sources import SourceUser

from domain.enums.type import (
    FeatureType,
    RoleType,
)

from utils import permission
from utils.permission import (
    check_permission,
    get_user_role,
    check_has_feature,
)

@pytest.fixture(scope="function")
def unstub():
    from mockito import unstub as mock_unstub
    yield
    mock_unstub()

@pytest.mark.in_memory
@patch('tasks.send_line_msg_tasks.async_send_text_message')
def test_check_permission__has_perm(mock_method, unstub):
    when(permission).check_has_feature(...).thenReturn(True)

    @check_permission(FeatureType.all)
    def fake_func(event):
        return 'in'

    event = Event()
    event.source = SourceUser(user_id=1)

    assert fake_func(event) == 'in'
    mock_method.assert_not_called()

@pytest.mark.in_memory
@patch('tasks.send_line_msg_tasks.send_text_message.apply_async')
def test_check_permission__no_perm(mock_method, unstub):
    when(permission).check_has_feature(...).thenReturn(False)

    @check_permission(FeatureType.all)
    def fake_func(event):
        return 'in'

    event = Event()
    event.source = SourceUser(user_id=1)

    assert fake_func(event) is None
    mock_method.assert_called_once_with(args=(1, '🚫權限不足 403 Forbidden🚫',))

@pytest.mark.in_memory
def test_get_user_role():
    role_map = {
        RoleType.admin: [1, 2, 3],
        RoleType.home_user: [4, 5],
    }

    assert get_user_role(1, role_map) == RoleType.admin
    assert get_user_role(4, role_map) == RoleType.home_user
    assert get_user_role(10000, role_map) == RoleType.anonymous

@pytest.mark.in_memory
def test_check_has_feature():
    permission_map = {
        RoleType.admin: [
            FeatureType.all
        ],
        RoleType.home_user: [
            FeatureType.youtubedl,
            FeatureType.weather,
            FeatureType.stock,
        ],
        RoleType.anonymous: {
            FeatureType.weather,
            FeatureType.stock,
        }
    }

    assert check_has_feature(RoleType.admin, FeatureType.wordpress, permission_map) is True
    assert check_has_feature(RoleType.admin, FeatureType.youtubedl, permission_map) is True
    assert check_has_feature(RoleType.admin, FeatureType.weather, permission_map) is True
    
    assert check_has_feature(RoleType.home_user, FeatureType.wordpress, permission_map) is False
    assert check_has_feature(RoleType.home_user, FeatureType.youtubedl, permission_map) is True
    assert check_has_feature(RoleType.home_user, FeatureType.weather, permission_map) is True

    assert check_has_feature(RoleType.anonymous, FeatureType.wordpress, permission_map) is False
    assert check_has_feature(RoleType.anonymous, FeatureType.youtubedl, permission_map) is False
    assert check_has_feature(RoleType.anonymous, FeatureType.weather, permission_map) is True