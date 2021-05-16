from daos.daos_impl.answers_dao_impl import AnswersDaoImpl
from daos.daos_impl.questions_dao_impl import QuestionDaoImpl
from daos.quizzes_dao import QuizesDAO
from models.quizzes import Quizzes
from util.db_connection import create_connection

connection = create_connection()

class QuizzesDaoImpl(QuizesDAO):
  
    @staticmethod
    def get_all_quizzes_for_course(course_id):
        sql = "Select * from quizzes where course_id=%s"
        cursor = connection.cursor()
        cursor.execute(sql, [course_id])
        records = cursor.fetchall()
        quizzes = []

        for record in records:
            quiz = Quizzes(id=record[0], name=record[1], course_id=record[2])
            quiz.questions = QuestionDaoImpl.get_all_questions_for_quiz(quiz.id)
            quizzes.append(quiz)
        return quizzes

    @staticmethod
    def get_quiz(quiz_id):
        sql = "Select * from quizzes where id=%s"
        cursor = connection.cursor()
        cursor.execute(sql, [quiz_id])
        record = cursor.fetchone()
        quiz = Quizzes(id=record[0], name=record[1], course_id=record[2])
        quiz.questions = QuestionDaoImpl.get_all_questions_for_quiz(quiz.id)
        return quiz

    @staticmethod
    def create_quiz(quiz, commit=True):
        sql = "insert into quizzes values (default, %s, %s) Returning *"
        cursor = connection.cursor()
        cursor.execute(sql, [quiz.name,
                             quiz.course_id])
        id = cursor.fetchone()[0]
        connection.commit() if commit else connection.rollback()
        for question in quiz.questions:
            QuestionDaoImpl.create_question(question, id)
        return True

    @staticmethod
    def get_quiz_review(quiz_id, user_id):
        quiz = QuizzesDaoImpl.get_quiz(quiz_id)
        for question in quiz.questions:
            question.students_answer = AnswersDaoImpl.get_students_answer(question.id, user_id)
        return quiz

    @staticmethod
    def submit_quiz(quiz, student_id):
        for question in quiz.questions:
            QuestionDaoImpl.submit_question(question, student_id)
        return QuizzesDaoImpl.get_quiz_review(quiz.id, student_id)


if __name__ == '__main__':
    print(QuizzesDaoImpl.create_quiz(Quizzes(name="New Quiz")))