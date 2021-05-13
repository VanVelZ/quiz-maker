from flask import request, jsonify

from exceptions.resource_unavailable import ResourceUnavailable
from exceptions.resource_not_found import ResourceNotFound

from models.courses import Courses
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
