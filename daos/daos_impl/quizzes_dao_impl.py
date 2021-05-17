from daos.daos_impl.questions_dao_impl import QuestionDAOImpl
from daos.quizzes_dao import QuizesDAO
from models.quizzes import Quizzes
from util.db_connection import create_connection

connection = create_connection()


class QuizzesDAOImpl(QuizesDAO):

    @staticmethod
    def get_all_quizzes_for_course(course_id):
        sql = "Select * from quizzes where course_id=%s"
        cursor = connection.cursor()
        cursor.execute(sql, [course_id])
        records = cursor.fetchall()
        quizzes = []

        for record in records:
            quiz = Quizzes(id=record[0], name=record[1], course_id=record[2])
            quiz.questions = QuestionDAOImpl.get_all_questions_for_quiz(quiz.id)
            quizzes.append(quiz)
        return quizzes

    @staticmethod
    def get_quiz(quiz_id):
        sql = "Select * from quizzes where id=%s"
        cursor = connection.cursor()
        cursor.execute(sql, [quiz_id])
        record = cursor.fetchone()
        quiz = Quizzes(id=record[0], name=record[1], course_id=record[2])
        quiz.questions = QuestionDAOImpl.get_all_questions_for_quiz(quiz.id)
        return quiz

    @staticmethod
    def create_quiz(quiz, commit=True):
        sql = "insert into quizzes values (default, %s, %s) Returning id"
        cursor = connection.cursor()
        cursor.execute(sql, [quiz.name,
                             quiz.course_id])
        id = cursor.fetchone()
        for question in quiz.questions:
            QuestionDAOImpl.create_question(question, quiz.id)
        connection.commit() if commit else connection.rollback()
        return True


if __name__ == '__main__':
    print(QuestionDAOImpl.create_quiz(Quizzes(name="New Quiz")))
