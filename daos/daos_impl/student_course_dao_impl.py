from daos.student_course_dao import StudentCoursesDAO
from exceptions.resource_not_found import ResourceNotFound
from models.student_courses import StudentCourses
from util.db_connection import connection


class StudentCourseDaoImpl(StudentCoursesDAO):

<<<<<<< HEAD
=======

>>>>>>> parent of 9c6cc3c (Merge pull request #32 from VanVelZ/DonBranch)
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

<<<<<<< HEAD
    @staticmethod
    def get_courses_by_id(course_id):
=======
    def get_courses_by_id(self,  courseid):
>>>>>>> parent of 9c6cc3c (Merge pull request #32 from VanVelZ/DonBranch)
        sql = "SELECT * FROM student_courses where id=%s"
        cursor = connection.cursor()
        cursor.execute(sql, [course_id])
        record = cursor.fetchone()

        if record:
            return StudentCourses(record[0], record[1], record[2])
        else:
<<<<<<< HEAD
            raise ResourceNotFound(
                f"Student course id: {course_id} - Not Found")
=======
            raise ResourceNotFound(f"Student course id: {courseid} - Not Found")

>>>>>>> parent of 9c6cc3c (Merge pull request #32 from VanVelZ/DonBranch)
