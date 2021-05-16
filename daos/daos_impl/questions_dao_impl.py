from daos.daos_impl.answers_dao_impl import AnswersDaoImpl
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
            question: Questions = Questions(id=record[0], description=record[2])
            question.answers = AnswersDaoImpl.get_all_answers_for_question(question.id)
            questions.append(question)
        return questions

    @staticmethod
    def create_question(question:Questions, quiz_id, commit=True):
        sql = "insert into questions values (default, %s, %s) returning id"
        cursor = connection.cursor()
        cursor.execute(sql, [quiz_id,
                             question.description])
        connection.commit() if commit else connection.rollback()
        id = cursor.fetchone()
        for answer in question.answers:
            AnswersDaoImpl.create_answer(answer, id)
        return True

    @staticmethod
    def submit_question(question:Questions, user_id, commit=True):
        sql = "insert into student_questions values (default, %s, %s, %s)"
        cursor = connection.cursor()
        cursor.execute(sql, [user_id,
                             question.id,
                             question.students_answer.id])
        connection.commit() if commit else connection.rollback()
        return True


