from abc import abstractmethod, ABC


class QuestionsDAO(ABC):

    @staticmethod
    @abstractmethod
    def get_all_questions_for_quiz(quiz_id):
        pass

    @staticmethod
    @abstractmethod
    def create_question(question, quiz_id):
        pass

