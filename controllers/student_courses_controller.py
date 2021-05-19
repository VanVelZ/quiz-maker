from flask import jsonify

from service.student_courses_services import StudentCourseServices


def route(app):
    # ----Retrieve all course from the database and return status code of 200 for successful retrieval
    @app.route("/studentcourses", methods=['GET'])
    def get_all_student_courses():
        return jsonify(StudentCourseServices.get_all_student_courses()), 200

    @app.route("/studentcourses/<courseid>", methods=['GET'])
    def get_all_student_courses_byid(courseid):
        try:
            return jsonify(StudentCourseServices.get_student_courses_byid(courseid)), 200
        except ValueError as e:
            return f"Invalid ID {courseid}", 400
