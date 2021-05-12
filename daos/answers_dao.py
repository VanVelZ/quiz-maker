from abc import abstractmethod, ABC


class AnswersDAO(ABC):

    @staticmethod
    @abstractmethod
    def get_all_answers():
        pass

