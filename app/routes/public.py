from flask import Blueprint

public_route = Blueprint('public', __name__)

# Route Home
@public_route.route('/')
def home():
    return 'Home'

def register_public_routes(app):
    app.register_blueprint(public_route)
