from flask import Flask 
from flask import Blueprint
from . import application
from . import company

def create_app():
    app = Flask(__name__)
    app.register_blueprint(application.application, url_prefix='/')
    app.register_blueprint(company.company, url_prefix='/xml-api')

    return app

app = create_app()
