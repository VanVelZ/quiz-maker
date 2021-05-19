from flask import jsonify

from service.student_courses_services import StudentCourseServices


def route(app):
    # ----Retrieve all course from the database and return status code of 200 for successful retrieval
    @app.route("/studentcourses", methods=['GET'])
    def get_all_student_courses():
        return jsonify(StudentCourseServices.get_all_student_courses()), 200

    @app.route("/studentcourses/<student_id>", methods=['GET'])
    def get_all_student_courses_by_studentid(student_id):
        return jsonify(StudentCourseServices.get_student_courses_by_studentid(student_id)), 200


