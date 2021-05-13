from daos.daos_impl.courses_dao_impl import CoursesDaoImpl


class CoursesService:
    courses_dao = CoursesDaoImpl()

    @classmethod
    def all_courses(cls):
        return cls.courses_dao.get_all_courses()

    @classmethod
    def get_course_by_id(cls, course_id):
        return cls.courses_dao.get_course_by_id(course_id)
