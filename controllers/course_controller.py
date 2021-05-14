from flask import request, jsonify
from exceptions.resource_not_found import ResourceNotFound
from daos.daos_impl.courses_dao_impl import CoursesDaoImpl
from service.courses_service import CoursesService


def route(app):

    @app.route("/courses/", methods=['GET'])
    def get_all_courses():
        return jsonify(CoursesService.all_courses()), 200

    @app.route("/courses/<course_id>", methods=['GET'])
    def get_course(course_id):
        try:
            course = CoursesService.get_course_by_id(int(course_id))
            return jsonify(course.json()), 200
        except ValueError:
            return "Not a valid ID", 400  # Bad Request
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/courses/<teacher_id>", methods=['GET'])
    def get_course_by_teacher_id(teacher_id):
        return jsonify(CoursesDaoImpl.get_courses_by_teacher_id(teacher_id))
