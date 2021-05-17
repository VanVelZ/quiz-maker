
from typing import Mapping
from daos.courses_dao import CoursesDAO
from models.courses import Courses
from daos.daos_impl.quizzes_dao_impl import QuizzesDaoImpl
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
    
    @staticmethod
    def get_student_grade(course_id, student_id):
        quizzes = QuizzesDaoImpl.get_all_quizzes_for_course(course_id)
        reviewed_quizzes = []
        student_grade = 0
        for quiz in quizzes:
            reviewed_quiz = QuizzesDaoImpl.get_quiz_review(quiz.id, student_id)
            if reviewed_quiz.grade is not None: reviewed_quizzes.append(reviewed_quiz)
        for quiz in reviewed_quizzes:
            student_grade += quiz.grade
        return student_grade / len(reviewed_quizzes)

        # commenting this out for now until getting the other daos impl from main/merge

    # @staticmethod
    # def get_courses_by_teacher_id(teacher_id):
    #     sql = "SELECT * FROM courses WHERE teacher_id=%s"
    #     cursor = connection.cursor()
    #     cursor.execute(sql, [teacher_id])
    #     records = cursor.fetchall()
    #     courses = []

    #     for record in records:
    #         course: Courses = Courses(record[0], record[1], record[2])
    # -------------------------------------PARTICULARY THIS LINE
    #         course.teacher_id = CoursesDaoImpl.get_courses_by_teacher_id(
    #             teacher_id)
    # ------------------------------------
    #         courses.append(course)
    #     return courses

