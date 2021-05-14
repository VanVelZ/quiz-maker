from flask import jsonify

from service.questions_services import QuestionsServices


def route(app):
    # ----Retrieve all questions from the database and return status code of 200 for successful retrieval
    @app.route("/questions", methods=['GET'])
    def get_all_questions():
        return jsonify(QuestionsServices.get_all_questions()), 200


