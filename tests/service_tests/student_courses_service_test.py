import unittest
from unittest.mock import MagicMock

from models.student_courses import StudentCourses
from daos.student_course_dao import StudentCoursesDAO
from daos.daos_impl.student_course_dao_impl import StudentCourseDaoImpl
from service.student_courses_services import StudentCourseServices

student_course1 = StudentCourses(1, 1, 1)
student_course2 = StudentCourses(2, 2, 1)
student_course3 = StudentCourses(3, 3, 1)

student_courses = [student_course1, student_course2, student_course3]

mock_student_course_dao = StudentCourseDaoImpl()
mock_student_course_dao.get_all_student_courses = MagicMock(
    return_value=student_courses)
student_courses_service = StudentCourseServices()


class StudentCoursesService(unittest.TestCase):

    def test_service_get_all_student_courses(cls):
        student_courses = student_courses_service.get_all_student_courses()
        assert all(student_courses)

    def test_service_get_student_courses_by_id(cls):
        returned_student_course = student_courses_service.get_student_courses_byid(
            1)
        assert returned_student_course.student_id == student_course1.student_id
