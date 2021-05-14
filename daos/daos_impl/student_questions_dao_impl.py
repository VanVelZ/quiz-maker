from daos.student_questions_dao import StudentQuestionsDAO
from models.student_questions import StudentQuestions
from util.db_connection import connection


class StudentQuestionsDAOImpl(StudentQuestionsDAO):

    @staticmethod
    def get_all_questions(): # retrieve all student questions
        sql = "SELECT * FROM questions"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        questions_list = []
        for record in records:
            questions = StudentQuestions(record[0], record[1], record[2])
            questions_list.append(questions.json())
        return questions_list
