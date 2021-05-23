import unittest
from unittest.mock import MagicMock

from models.users import Users
from daos.user_dao import UserDAO
from daos.daos_impl.user_dao_impl import UserDAOImpl
from service.user_services import UserService

user1 = Users(1, 'Steve', 'Steven', '100000', 'password', 0)
user2 = Users(2, 'Ben', 'Steven', '100001', 'password', 0)
user3 = Users(3, 'George', 'Steven', '100002', 'password', 0)
users = [user1, user2, user3]

mock_user_dao = UserDAOImpl()
mock_user_dao.get_all_users = MagicMock(return_value=users)
user_service = UserService()


class UserServiceTest(unittest.TestCase):

    def test_service_create_user(self):
        new_user = user_service.create_user(user1)
        assert new_user.users_id != 0

    def test_service_get_user_by_id(self):
        returned_user = user_service.get_user_by_id(2)
        assert returned_user.first_name == user2.first_name

    def test_service_all_users(self):
        users = user_service.get_all_users()
        assert all(users)

    def test_service_update_user(self):
        pass

    def test_service_delete_user(self):
        user1.users_id = 1
        result = user_service.delete_user(user1.users_id)
        assert result == True
