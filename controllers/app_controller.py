from flask_cors import CORS
from controllers import quiz_controller
from controllers import course_controller
from controllers import user_controller


def route(app):
    quiz_controller.route(app)
    course_controller.route(app)
    user_controller.route(app)
    CORS(app)
