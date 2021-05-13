from models.courses import Courses
from daos.courses_dao import CoursesDAO
from util.db_connection import connection


class CoursesDaoImpl(CoursesDAO):
    @staticmethod
    def get_all_courses():
        sql = "Select * from courses"
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
        sql = "Select * from courses where id=%s"
        cursor = connection.cursor()
        cursor.execute(sql, [course_id])
        record = cursor.fetchone()
        course = Courses(record[0], record[1], record[2])
        return course
