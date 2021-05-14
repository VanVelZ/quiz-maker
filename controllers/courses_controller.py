from flask import jsonify

from service.courses_services import CoursesServices


def route(app):
    # ----Retrieve all courses from the database and return status code of 200 for successful retrieval
    @app.route("/courses", methods=['GET'])
    def get_all_courses():
        return jsonify(CoursesServices.get_all_courses()), 200

        # ----Retrieve all courses from the database and return status code of 200 for successful retrieval

    @app.route("/courses/<courseid>", methods=['GET'])
    def get_all_courses_byid(courseid):
        return jsonify(CoursesServices.get_all_courses_by_id(courseid)), 200
