from flask_cors import CORS
from controllers import quiz_controller
from controllers import course_controller
from controllers import user_controller


def route(app):
    quiz_controller.route(app)
    course_controller.route(app)
    user_controller.route(app)
    answers_controller.route(app)
    questions_controller.route(app)
    student_courses_controller.route(app)
    student_questions_controller.route(app)
    CORS(app)

