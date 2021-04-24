from flask import Flask
#import app.config as conf
app = Flask(__name__)
#app.config.from_object(conf.AppConfig)
from app import routes
from app import user_routes