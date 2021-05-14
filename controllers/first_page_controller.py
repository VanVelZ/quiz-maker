from controllers import answers_controller,courses_controller,quizes_controller,questions_controller,student_courses_controller,student_questions_controller,user_controller


def route(app):
    # Calls all controllers
    answers_controller.route(app)
    courses_controller.route(app)
    quizes_controller.route(app)
    questions_controller.route(app)
    student_courses_controller.route(app)
    student_questions_controller.route(app)
    user_controller(app)
