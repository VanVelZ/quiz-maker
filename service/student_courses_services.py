from daos.daos_impl.student_course_dao_impl import StudentCourseDaoImpl


class StudentCourseServices:
    studentcourse_dao = StudentCourseDaoImpl()

    @classmethod
    def get_all_student_courses(cls):
        return cls.studentcourse_dao.get_all_student_courses()

    @classmethod
    def get_student_courses_byid(cls, courseid):
        return cls.studentcourse_dao.get_courses_by_id(courseid)
