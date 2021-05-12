
from abc import abstractmethod, ABC


class UserDAO(ABC):

    @abstractmethod
    def create_user(self, user):
        pass

    @abstractmethod
    def get_all_users(self):
        pass

    @abstractmethod
    def get_user_by_id(self, userid):
        pass

    @abstractmethod
    def update_user(self, change, userid):
        pass

    @abstractmethod
    def delete_user(self, userid):
        pass

