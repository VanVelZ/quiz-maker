from flask import jsonify

from service.student_questions_services import StudentQuestionsServices


def route(app):
    # ----Retrieve all student questions from the database and return status code of 200 for successful retrieval
    @app.route("/studentquestions", methods=['GET'])
    def get_all_student_questions():
        return jsonify(StudentQuestionsServices.get_all_student_questions()), 200

