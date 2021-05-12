from daos.questions_dao import QuestionsDAO
from models.questions import Questions
from util.db_connection import create_connection

connection = create_connection()

class QuestionDaoImpl(QuestionsDAO):

    @staticmethod
    def get_all_questions_for_quiz(quiz_id):
        sql = "Select * from questions where quiz_id=%s"
        cursor = connection.cursor()
        cursor.execute(sql, [quiz_id])
        records = cursor.fetchall()
        questions = []

        for record in records:
            question = Questions(id=record[0], description=record[1])
            questions.append(question)
        return questions

    @staticmethod
    def create_question(question, quiz_id, commit=True):
        sql = "insert into answers values (default, %s, %s)"
        cursor = connection.cursor()
        cursor.execute(sql, [question.description,
                             quiz_id])
        connection.commit() if commit else connection.rollback()
        return True
