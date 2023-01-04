from flask import Flask
from flask_cors import CORS
from google.cloud import ndb
import os
# import gspread

credential_path = "skypebot.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
client = ndb.Client()


def ndb_wsgi_middleware(wsgi_app):
    def middleware(environ, start_response):
        with client.context():
            return wsgi_app(environ, start_response)
    return middleware


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.wsgi_app = ndb_wsgi_middleware(app.wsgi_app)  # Wrap the app in middleware.
    return app
