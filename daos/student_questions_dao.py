
from abc import abstractmethod, ABC


class StudentQuestionsDAO(ABC):

    @staticmethod
    @abstractmethod
    def get_all_questions():
        pass
