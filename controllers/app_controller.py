from flask_cors import CORS
from controllers import quiz_controller,user_controller,answers_controller,course_controller,questions_controller,student_questions_controller,student_courses_controller


def route(app):
    quiz_controller.route(app)
    user_controller.route(app)
    answers_controller.route(app)
    course_controller.route(app)
    questions_controller.route(app)
    student_questions_controller.route(app)
    student_courses_controller.route(app)
    CORS(app)