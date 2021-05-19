from flask import jsonify, request

from models.questions import Questions
from service.questions_services import QuestionsServices


def route(app):
    # ----Retrieve all questions from the database and return status code of 200 for successful retrieval
    @app.route("/questions", methods=['GET'])
    def get_all_questions():
        return jsonify(QuestionsServices.get_all_questions()), 200


    # @app.route("/questions", methods=['POST'])
    # # ----Create a new question
    # def create_question():
    #     question = Questions.json_parse(request.json)
    #     question_services = QuestionsServices.create_answer(question)
    #     return jsonify(question_services.json()), 201  # resource created

