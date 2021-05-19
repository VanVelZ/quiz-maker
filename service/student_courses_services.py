from daos.student_course_dao import StudentCoursesDAO
from daos.daos_impl.student_course_dao_impl import StudentCourseDaoImpl


class StudentCourseServices:
    studentcourse_dao = StudentCourseDaoImpl()

    @classmethod
    def get_all_student_courses(cls):
        return cls.studentcourse_dao.get_all_student_courses()

    @classmethod
    def get_student_courses_byid(cls, courseid):
        courses = cls.studentcourse_dao.get_courses_by_id(courseid)
        json_courses = []
        for course in courses:
            json_courses.append(course.json)
        return json_courses

    @staticmethod
    def get_student_courses_by_studentid(student_id):
        courses = StudentCourseDaoImpl.load_courses_for_student(student_id)
        json_courses = []
        for course in courses:
            json_courses.append(course.json())
        return json_courses
