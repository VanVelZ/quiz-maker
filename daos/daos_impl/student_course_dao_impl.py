from daos.student_course_dao import StudentCoursesDAO
from exceptions.resource_not_found import ResourceNotFound
from models.student_courses import StudentCourses
from util.db_connection import connection


class StudentCourseDaoImpl(StudentCoursesDAO):

    def get_all_students_courses(self):  # retrieve all student courses
        sql = "SELECT * FROM student_courses"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        studentcourses_list = []
        for record in records:
            student_courses = StudentCourses(record[0], record[1], record[2])
            studentcourses_list.append(student_courses.json())
        return studentcourses_list

    def get_courses_by_id(self, courseid):
        sql = "SELECT * FROM student_courses where id=%s"
        cursor = connection.cursor()
        cursor.execute(sql)
        record = cursor.fetchone()

        if record:
            return StudentCourses(record[0], record[1], record[2])
        else:
            raise ResourceNotFound(f"Student course id: {courseid} - Not Found")
