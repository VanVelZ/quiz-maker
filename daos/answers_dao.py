from abc import abstractmethod, ABC


class AnswersDAO(ABC):

    @abstractmethod
    def get_all_answers(self):
        pass
