import unittest
from models.courses import Courses
from daos.courses_dao import CoursesDAO
from daos.daos_impl.courses_dao_impl import CoursesDaoImpl

courses_dao = CoursesDaoImpl()

test_course = Courses(1, 'Physical Science', 6)
courses = [test_course]


class CourseTest(unittest.TestCase):

    def test_get_course_by_id(self):
        retrieved_course = courses_dao.get_course_by_id(test_course.courses_id)
        assert test_course.name == retrieved_course.name

    def test_get_course_by_teacher_id(self):
        retrieved_course = courses_dao.get_courses_by_teacher_id(
            test_course.teacher_id)
        assert courses[0].name == test_course.name
