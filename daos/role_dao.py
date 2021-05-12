
from abc import abstractmethod, ABC


class RoleDAO(ABC):

    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def get_role_by_id(self, roleid):
        pass

    @abstractmethod
    def update_role(self, change, roleid):
        pass

    @abstractmethod
    def delete_role(self, roleid):
        pass

