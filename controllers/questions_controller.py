from flask import jsonify, request

from models.questions import Questions
from service.questions_services import QuestionsServices


def route(app):
    # ----Retrieve a specific questions from the database by quiz id and return status code of 200 for successful
    # retrieval
    @app.route("/questions/<quiz_id>", methods=['GET'])
    def get_all_questions_byid(quiz_id):
        return jsonify(QuestionsServices.get_all_questions_by_id(quiz_id)), 200

    # @app.route("/questions", methods=['POST'])
    # # ----Create a new question
    # def create_question():
    #     question = Questions.json_parse(request.json)
    #     question_services = QuestionsServices.create_answer(question)
    #     return jsonify(question_services.json()), 201  # resource created

