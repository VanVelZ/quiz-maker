from flask_cors import CORS
from controllers import quiz_controller


def route(app):
    quiz_controller.route(app)
    CORS(app)