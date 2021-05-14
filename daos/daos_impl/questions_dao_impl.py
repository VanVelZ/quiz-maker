from daos.questions_dao import QuestionsDAO
from models.questions import Questions
from util.db_connection import connection


class QuestionsDAOImpl(QuestionsDAO):

    @staticmethod
    def get_all_questions():  # retrieve all user questions
        sql = "SELECT * FROM questions"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        question_list = []
        for record in records:
            questions = Questions(record[0], record[1], record[2])
            question_list.append(questions.json())
        return question_list



