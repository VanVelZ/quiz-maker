from abc import abstractmethod, ABC


class AnswersDAO(ABC):

    @staticmethod
    @abstractmethod
    def get_all_answers_for_question(question_id):
        pass

    @staticmethod
    @abstractmethod
    def create_answer(answer, question_id):
        pass