from daos.courses_dao import CoursesDAO
from models.courses import Courses
from util.db_connection import connection


class CoursesDAOImpl(CoursesDAO):

    @staticmethod
    def get_all_courses():  # retrieve all user's courses
        sql = "SELECT * FROM courses"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        courses_list = []
        for record in records:
            courses = Courses(record[0], record[1], record[2])
            courses_list.append(courses.json())
        return courses_list

    @staticmethod
    def get_course_id(course_id): # retrieve all user's courses by ID
        sql = "Select * from courses where id=%s"
        cursor = connection.cursor()
        cursor.execute(sql, [course_id])
        record = cursor.fetchone()
        course = Courses(record[0], record[1], record[2])
        return course
