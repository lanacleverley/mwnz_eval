from flask import Blueprint

application =  Blueprint("application", __name__)

@application.route('/')
def leaves():
    return "Hello, World!"