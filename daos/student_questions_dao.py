from abc import abstractmethod, ABC


class StudentQuestionsDAO(ABC):

    @abstractmethod
    def get_all_questions(self):
        pass
