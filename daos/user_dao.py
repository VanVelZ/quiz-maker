
from abc import abstractmethod, ABC


class UserDAO(ABC):

    @staticmethod
    @abstractmethod
    def create_user(user):
        pass

    @staticmethod
    @abstractmethod
    def get_all_users():
        pass

    @staticmethod
    @abstractmethod
    def get_user_by_id(userid):
        pass

    @staticmethod
    @abstractmethod
    def update_user(change, userid):
        pass

    @staticmethod
    @abstractmethod
    def delete_user(userid):
        pass

