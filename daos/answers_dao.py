from abc import abstractmethod, ABC


class AnswersDAO(ABC):
    @abstractmethod
    def get_all_answers_for_question(self, question_id):
        pass

    @abstractmethod
    def create_answer(self, answer, question_id):
        pass
