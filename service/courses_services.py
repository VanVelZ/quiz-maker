from daos.daos_impl.courses_dao_impl import CoursesDaoImpl


class CoursesServices:
    courses_dao = CoursesDaoImpl()

    @classmethod
    def get_all_courses(cls):
        return cls.courses_dao.get_all_courses()

    @classmethod
    def get_all_courses_by_id(cls, courseid):
        return cls.courses_dao.get_course_id(courseid)
