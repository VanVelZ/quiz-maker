from daos.student_course_dao import StudentCoursesDAO
from exceptions.resource_not_found import ResourceNotFound
from models.student_courses import StudentCourses
from util.db_connection import connection


class StudentCourseDaoImpl(StudentCoursesDAO):

    @staticmethod
    def get_all_student_courses():  # retrieve all student courses
        sql = "SELECT * FROM student_courses"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        studentcourses_list = []
        for record in records:
            student_courses = StudentCourses(record[0], record[1], record[2])
            studentcourses_list.append(student_courses.json())
        return studentcourses_list

    @staticmethod
    def get_courses_by_id(course_id):
        sql = "SELECT * FROM student_courses where id=%s"
        cursor = connection.cursor()
        cursor.execute(sql, [course_id])
        record = cursor.fetchone()

        if record:
            return StudentCourses(record[0], record[1], record[2])
        else:
            raise ResourceNotFound(
                f"Student course id: {course_id} - Not Found")

    @staticmethod
    def load_courses_for_student(student_id):
        sql = "Select course_id from student_courses where student_id =%s"
        cursor = connection.cursor()
        cursor.execute(sql, [student_id])
        record = cursor.fetchall()
        courses = []
        for courseID in record:
            student_course = StudentCourses(courseID[0])
            courses.append(student_course)
            return courses
