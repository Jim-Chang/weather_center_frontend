from flask import Blueprint, request, make_response
from utils.log import logging

from domain.enums.type import RoleType

from tasks.send_line_msg_tasks import async_send_text_message
from utils import permission

motion_webhook_api = Blueprint('motion_webhook_api', __name__)

notify_users = permission._role_user_list_map.get(RoleType.admin)

@motion_webhook_api.route('/record/new', methods=['POST'])
def on_new_record():
    '''
    {
        'filename': '/var/lib/motioneye/Camera1/2021-01-04/12-16-03.mp4'
    }
    '''
    data = request.json['filename'].split('/')
    camera, date, filename = data[4], data[5], data[6]
    message = '{} 偵測到動靜！\n日期：{}\n錄影檔名：{}'.format(camera, date, filename)
    
    for user_id in notify_users:
        async_send_text_message(user_id, message)

    return make_response('', 200)