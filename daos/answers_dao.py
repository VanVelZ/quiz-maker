from abc import abstractmethod, ABC


class AnswersDAO(ABC):
<<<<<<< HEAD
    @staticmethod
    @abstractmethod
=======

>>>>>>> parent of 9c6cc3c (Merge pull request #32 from VanVelZ/DonBranch)
    def get_all_answers_for_question(question_id):
        pass

    @staticmethod
    @abstractmethod
    def create_answer(answer, question_id):
        pass
