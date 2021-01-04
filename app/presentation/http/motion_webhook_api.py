from flask import Blueprint, request, make_response
from utils.log import logging

motion_webhook_api = Blueprint('motion_webhook_api', __name__)


@motion_webhook_api.route('/record/new', methods=['POST'])
def on_new_record():
    data = request.json
    print(data)

    return make_response('', 200)