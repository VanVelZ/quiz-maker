from models.courses import Courses
from daos.courses_dao import CoursesDAO
from util.db_connection import connection


class CoursesDaoImpl(CoursesDAO):

    @staticmethod
    def get_all_courses():
        sql = "SELECT * FROM courses"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        course_list = []
        for record in records:
            courses = Courses(record[0], record[1], record[2])
            course_list.append(courses.json())
        return course_list

    @staticmethod
    def get_course_by_id(course_id):

        sql = "SELECT * FROM courses WHERE id=%s"
        cursor = connection.cursor()
        cursor.execute(sql, [course_id])
        record = cursor.fetchone()
        course = Courses(record[0], record[1], record[2])
        return course

    @staticmethod
    def get_courses_by_teacher_id(teacher_id):
        sql = "SELECT * FROM courses WHERE teacher_id=%s"
        cursor = connection.cursor()
        cursor.execute(sql, [teacher_id])
        records = cursor.fetchall()
        courses_list = []
        for record in records:
            course = Courses(record[0], record[1], record[2])
            courses_list.append(course.json())
        return courses_list

