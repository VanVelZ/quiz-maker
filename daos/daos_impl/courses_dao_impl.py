from models.courses import Courses
from daos.courses_dao import CoursesDAO
from models.student_courses import StudentCourses
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
            courses_list.append(course.json()), 200
        return courses_list

    @staticmethod
    def get_student_grade(course_id,student_id):
        sql = "SELECT * FROM student_courses WHERE course_id=%s and  student_id=%s"
        cursor = connection.cursor()
        cursor.execute(sql, [course_id,student_id])
        records = cursor.fetchall()
        student_courses_list = []
        for record in records:
            course = StudentCourses(record[0], record[1], record[2])
            student_courses_list.append(course.json()), 200
        return student_courses_list

