from daos.daos_impl.courses_dao_impl import CoursesDaoImpl
from models.courses import Courses


class CoursesService:
    courses_dao = CoursesDaoImpl()

    @classmethod
    def all_courses(cls):
        return cls.courses_dao.get_all_courses()

    @classmethod
    def get_course_by_id(cls, course_id):
        return cls.courses_dao.get_course_by_id(course_id)

    @classmethod
    def get_course_by_teacher_id(cls, teacher_id):
        return cls.courses_dao.get_courses_by_teacher_id(teacher_id)
