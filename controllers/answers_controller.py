from flask import jsonify, request

from models.answers import Answers
from service.answers_services import AnswersServices


def route(app):
    @app.route("/answer/<question_id>", methods=['POST'])
    # ----Create a new answer
    def post_Answers(question_id):
        answers = Answers.json_parse(request.json)
        answer_services = AnswersServices.create_answers(answers, question_id)
        return jsonify(str(answer_services)), 201  # resource created

    # ----Retrieve all answers from the database and return status code of 200 for successful retrieval
    @app.route("/answers/<question_id>", methods=['GET'])
    def get_all_answers(question_id):
        return jsonify(AnswersServices.get_all_answers_by_questionID(question_id)), 200

    # Get answer by answer ID
    @app.route("/answer/<answer_id>", methods=['GET'])
    def get_answer_byid(answer_id):
        return jsonify(AnswersServices.get_answers_by_answerID(answer_id)), 200

    # Get answer by question_id, student_id
    @app.route("/studentanswer/<question_id>/<student_id>", methods=['GET'])
    def get_students_answer(question_id, student_id):
        return jsonify(AnswersServices.get_students_answer(question_id, student_id)), 200
