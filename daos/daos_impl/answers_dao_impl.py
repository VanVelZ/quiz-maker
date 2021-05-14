from daos.answers_dao import AnswersDAO
from models.answers import Answers
from util.db_connection import create_connection

connection = create_connection()

class AnswersDaoImpl(AnswersDAO):

    @staticmethod
    def get_all_answers_for_question(question_id):
        sql = "Select * from answers where question_id=%s"
        cursor = connection.cursor()
        cursor.execute(sql, [question_id])
        records = cursor.fetchall()
        answers = []

        for record in records:
            answer = Answers(id=record[0], description=record[1], is_correct=record[3])
            answers.append(answer)
        return answers

    @staticmethod
    def create_answer(answer, question_id, commit=True):
        sql = "insert into answers values (default, %s, %s, %s)"
        cursor = connection.cursor()
        cursor.execute(sql, [answer.description,
                             question_id,
                             answer.is_correct])
        connection.commit() if commit else connection.rollback()
        return True
