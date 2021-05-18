from flask import json, request, jsonify

from models.quizzes import Quizzes
from service.quiz_service import QuizService


def route(app):

    @app.route("/quizzes/<course_id>", methods=["GET"])
    def get_quizzes_by_course(course_id):
        return jsonify(QuizService.get_all_quizzes_for_course(course_id))
    
    @app.route("/quiz/<id>", methods=["GET"])
    def get_quiz(id):
        return jsonify(QuizService.get_quiz(id))

    @app.route("/quizzes/", methods=["PUT"])
    def create_quiz():
        quiz = Quizzes.json_parse(request.json)
        if QuizService.create_quiz(quiz):
            return "You did it!", 200
        else:
            return "Oops"

    @app.route("/quizzes/<student_id>/", methods=["POST"])
    def submit_quiz(student_id):
        quiz = Quizzes.json_parse(request.json)
        return jsonify(QuizService.submit_quiz(quiz, student_id))

    @app.route("/quizzes/<quiz_id>/<student_id>/", methods=["GET"])
    def get_quiz_review(quiz_id, student_id):
        return jsonify(QuizService.get_quiz_review(quiz_id, student_id))
    