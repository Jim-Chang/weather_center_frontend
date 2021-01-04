import json

from domain.enums.type import (
    FeatureType,
    RoleType,
)
from tasks.send_line_msg_tasks import async_send_text_message

from linebot.models import Event

# user id role define
_role_user_list_map = {
    RoleType.admin: [
        'Uebaac5edfee64f6b934a4d27b937cead',    # Jim
    ],
    RoleType.home_user: [
        'U97849deb917944d68c89350ba33a46af',    # Kate
    ],
}

# permission with feature define
_permission_define_map = {
    RoleType.admin: [
        FeatureType.all
    ],
    RoleType.home_user: [
        FeatureType.youtubedl,
        FeatureType.weather,
        FeatureType.stock,
        FeatureType.motion,
    ],
    RoleType.anonymous: {
        FeatureType.weather,
        FeatureType.stock,
    }
}

def check_permission(feature: FeatureType):
    def decorator(func):
        def wrapper(event: Event):
            role = get_user_role(event.source.user_id, _role_user_list_map)
            if check_has_feature(role, feature, _permission_define_map):
                return func(event)
            else:
                async_send_text_message(event.source.user_id, '🚫權限不足 403 Forbidden🚫')
        return wrapper
    return decorator

def get_user_role(user_id: int, role_user_list_map: dict) -> RoleType:
    for role_type, user_ids in role_user_list_map.items():
        if user_id in user_ids:
            return role_type

    return RoleType.anonymous

def check_has_feature(role: RoleType, feature: FeatureType, permission_define_map: dict) -> bool:
    if role == RoleType.admin:
        return True

    return feature in permission_define_map.get(role, [])