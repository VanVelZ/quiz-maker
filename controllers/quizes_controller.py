from flask import jsonify

from service.quizes_services import QuizesServices


def route(app):
    # ----Retrieve all quizes from the database and return status code of 200 for successful retrieval
    @app.route("/quizes", methods=['GET'])
    def get_all_quizes():
        return jsonify(QuizesServices.get_all_quizes()), 200

        # ----Retrieve  quizes  by ID from the database and return status code of 200 for successful retrieval

    @app.route("/quizes/<quizeid>", methods=['GET'])
    def get_all_quizes(quizeid):
        return jsonify(QuizesServices.get_quizes_by(quizeid)), 200
