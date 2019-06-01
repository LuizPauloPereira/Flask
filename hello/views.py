from flask import Blueprint

hello = Blueprint("hello", __name__)

@hello.route("/")
def index():
    return "<h1>Hello World!</h1>"