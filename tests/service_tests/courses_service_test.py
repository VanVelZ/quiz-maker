from service.courses_service import CoursesService
import unittest
from unittest.mock import MagicMock

from models.courses import Courses
from daos.courses_dao import CoursesDAO
from daos.daos_impl.courses_dao_impl import CoursesDaoImpl
from service.courses_service import CoursesService

course = Courses(1, 'Physical Science', 6)
course2 = Courses(2, 'Physical Science', 6)
course3 = Courses(3, 'Physical Science', 6)
courses = [course, course2, course3]


mock_courses_dao = CoursesDaoImpl()
mock_courses_dao.get_all_courses = MagicMock(return_value=courses)
courses_service = CoursesService()


class CourseTest(unittest.TestCase):

    def test_service_all_courses(self):
        courses = courses_service.all_courses()
        assert all(courses)

    def test_service_get_course_by_id(self):
        retrieved_course = courses_service.get_course_by_id(course.courses_id)
        assert course.name == retrieved_course.name

    def test_service_get_courses_by_teacher_id(self):
        retrieved_course = courses_service.get_course_by_teacher_id(
            course.teacher_id)
        assert all(retrieved_course)
