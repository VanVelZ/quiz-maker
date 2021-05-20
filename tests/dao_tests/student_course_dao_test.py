import unittest

from models.student_courses import StudentCourses
from daos.student_course_dao import StudentCoursesDAO
from daos.daos_impl.student_course_dao_impl import StudentCourseDaoImpl

student_course_dao = StudentCourseDaoImpl()

test_student_course = StudentCourses(1, 1, 1)


class StudentCourseTest(unittest.TestCase):

    def test_get_all_courses(self):
        student_course = student_course_dao.get_all_student_courses()
        assert all(student_course)

    def test_get_courses_by_id(self):
        retrieved_student_course = student_course_dao.get_courses_by_id(
            test_student_course.course_id)
        assert test_student_course.student_id == retrieved_student_course.student_id
