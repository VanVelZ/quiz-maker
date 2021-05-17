from daos.daos_impl.courses_dao_impl import CoursesDaoImpl
from models.courses import Courses


class CoursesService:

    @staticmethod
    def all_courses():
        return CoursesDaoImpl.get_all_courses()

    @staticmethod
    def get_course_by_id(course_id):
        return CoursesDaoImpl.get_course_by_id(course_id)

    @staticmethod
    def get_course_by_teacher_id(cls, teacher_id):
        courses = CoursesDaoImpl.get_courses_by_teacher_id(teacher_id)
        courses_as_json = []
        for course in courses:
            courses_as_json.append(course.json())
        return courses_as_json

    @staticmethod
    def get_student_grade(course_id, student_id):
        return {
            "grade": CoursesDaoImpl.get_student_grade(course_id, student_id)
        }