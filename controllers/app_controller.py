from flask_cors import CORS
from controllers import quiz_controller
from controllers import course_controller


def route(app):
    quiz_controller.route(app)
    course_controller.route(app)
    CORS(app)
