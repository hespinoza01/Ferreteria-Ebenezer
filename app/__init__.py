from flask import Flask

from .config import Config
from .routes import Routes

app = Flask(__name__, static_folder='public')

app.config.from_object(Config)
app.register_blueprint(Routes)
