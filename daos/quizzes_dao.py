from abc import abstractmethod, ABC


class QuizesDAO(ABC):

    @staticmethod
    @abstractmethod
    def get_all_quizzes_for_course(course_id):
        pass

    @staticmethod
    @abstractmethod
    def get_quiz(quiz_id):
        pass

    @staticmethod
    @abstractmethod
    def create_quiz(quiz_id):
        pass


