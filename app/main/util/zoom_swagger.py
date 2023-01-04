from flask_restx import Namespace


class ZoomCreateMeetingDto:
    ns_zoom = Namespace(
        path='',
        name='zoom-create',
        description='Zoom Meeting Create Api')
