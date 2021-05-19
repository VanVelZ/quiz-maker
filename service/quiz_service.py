from daos.daos_impl.quizzes_dao_impl import QuizzesDaoImpl
from models.quizzes import Quizzes


class QuizService:

    @staticmethod
    def get_all_quizzes_for_course(course_id):
        quizzes = QuizzesDaoImpl.get_all_quizzes_for_course(course_id)
        quizzes_as_json = []
        for quiz in quizzes:
            quizzes_as_json.append(quiz.json())
        return quizzes_as_json

    @staticmethod
    def create_quiz(quiz: Quizzes):
        return QuizzesDaoImpl.create_quiz(quiz)

    @staticmethod
    def get_quiz_review(quiz_id, student_id):
        return QuizzesDaoImpl.get_quiz_review(quiz_id, student_id).json()

    @staticmethod
    def submit_quiz(quiz, student_id):
        return QuizzesDaoImpl.submit_quiz(quiz, student_id).json()

    @staticmethod
    def get_quiz(id):
        return QuizzesDaoImpl.get_quiz(id).json()

    @staticmethod
    def get_all_quizzes_for_course_for_student(course_id, student_id):
        quizzes = QuizzesDaoImpl.get_all_quizzes_for_course_for_student(course_id, student_id)
        quizzes_as_json = []
        for quiz in quizzes:
            quizzes_as_json.append(quiz.json())
        return quizzes_as_json