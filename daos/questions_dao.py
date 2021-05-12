from abc import abstractmethod, ABC


class QuestionsDAO(ABC):

    @abstractmethod
    def get_all_questions(self):
        pass

