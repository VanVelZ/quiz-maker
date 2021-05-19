from flask import jsonify

from service.answers_services import AnswersServices


def route(app):
    # ----Retrieve all answers from the database and return status code of 200 for successful retrieval
    @app.route("/answers", methods=['GET'])
    def get_all_answers():
        return jsonify(AnswersServices.get_all_answers()), 200
