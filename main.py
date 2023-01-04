from app import blueprint
from app.main import create_app
from werkzeug.middleware.proxy_fix import ProxyFix
from flask_jwt_extended import JWTManager
import warnings

app = create_app()
app.wsgi_app = ProxyFix(app.wsgi_app)
app.register_blueprint(blueprint)
jwt = JWTManager(app)
warnings.filterwarnings("ignore", category=UserWarning, module='bs4')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
