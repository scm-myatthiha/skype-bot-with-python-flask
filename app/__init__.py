from flask import Blueprint
from flask_restx import Api

from .main.controller.create_zoom import ns_zoom
from .main.controller.auto_msg_skype import ns_skype

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Skype Bot API',
          version='1.0',
          description='Skype Auto Bot'
          )

api.add_namespace(ns_zoom)
api.add_namespace(ns_skype)
