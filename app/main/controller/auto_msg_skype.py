from flask_restx import Resource

from ..util.auto_msg_skype_swagger import AutoMsgSkypeDto
from ..service import skype

ns_skype = AutoMsgSkypeDto.ns_skype


@ns_skype.route('')
class AutoMsgSkype(Resource):
    def post(self):
        skype.AutoMessageSend()
        return '', 204
