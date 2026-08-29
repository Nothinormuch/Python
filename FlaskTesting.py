import flask

gatewayapi=flask.Flask(__name__)

@gatewayapi.route("/")
def HomePage():
    return"Welcome to the home page!"
@gatewayapi.route("/sum")
def add(a=2,b=2):
    return str(a+b)

@gatewayapi.route("/difference")
def subtract(a=2,b=2,reverse=False):
    if reverse:return b-a
    else:return str(a-b)

@gatewayapi.route("/multiplication")
def multiply(a=2,b=2):
    return str(a*b)

@gatewayapi.route("/division")
def divide(a=2,b=2,reverse=False):
    if reverse:return b/a
    else:return str(a/b)


gatewayapi.run(port="404",host="0.0.0.0")

