from flask_restx import Resource

from ..util.zoom_swagger import ZoomCreateMeetingDto
from ..service import zoom, skype

ns_zoom = ZoomCreateMeetingDto.ns_zoom


@ns_zoom.route('')
class ZoomCreate(Resource):
    def post(self):
        joinUrl, meetingPassword = zoom.createMeeting()
        skype.MessageSend(joinUrl, meetingPassword)
        return '', 204
