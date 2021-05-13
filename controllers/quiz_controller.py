from flask import request, jsonify

from models.quizzes import Quizzes
from service.quiz_service import QuizService


def route(app):

    @app.route("/quizzes/<course_id>", methods=["GET"])
    def get_quizzes_by_course(course_id):
        return jsonify(QuizService.get_all_quizzes_for_course(course_id))

    @app.route("/quizzes/", methods=["POST"])
    def create_quiz():
        quiz = Quizzes.json_parse(request.json)
        return QuizService.create_quiz(quiz)
