from abc import abstractmethod, ABC


class QuizesDAO(ABC):

    @abstractmethod
    def get_all_quizez(self):
        pass

