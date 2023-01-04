from flask_restx import Namespace


class AutoMsgSkypeDto:
    ns_skype = Namespace(
        path='',
        name='auto-message',
        description='Auto Message Send Skype')
