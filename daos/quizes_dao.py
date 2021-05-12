from abc import abstractmethod, ABC


class QuizesDAO(ABC):

    @staticmethod
    @abstractmethod
    def get_all_quizez():
        pass

