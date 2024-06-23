from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

def create_app():
    app = Flask(__name__, template_folder='../templates')  # Explicitly set the template folder
    from . import routes
    routes.init_app(app)
    return app
