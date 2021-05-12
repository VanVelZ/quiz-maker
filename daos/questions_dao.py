from abc import abstractmethod, ABC


class QuestionsDAO(ABC):

    @staticmethod
    @abstractmethod
    def get_all_questions():
        pass

