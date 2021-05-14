from daos.answers_dao import AnswersDAO
from models.answers import Answers
from util.db_connection import create_connection, connection


class AnswersDAOImpl(AnswersDAO):

    @staticmethod
    def get_all_answers():  # retrieve all user answers
        sql = "SELECT * FROM answers"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        answers_list = []
        for record in records:
            answer = Answers(record[0], record[1], record[2])
            answers_list.append(answer.json())
        return answers_list
