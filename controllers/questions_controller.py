from flask import jsonify

from service.questions_services import QuestionsServices


def route(app):
    # ----Retrieve a specific questions from the database by quiz id and return status code of 200 for successful
    # retrieval
    @app.route("/questions/<quiz_id>", methods=['GET'])
    def get_all_questions_byid(quiz_id):
        return jsonify(QuestionsServices.get_all_questions_by_id(quiz_id)), 200

   