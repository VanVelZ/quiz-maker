import unittest
from models.users import Users
from daos.user_dao import UserDAO
from daos.daos_impl.user_dao_impl import UserDAOImpl

user_dao = UserDAOImpl()

test_user = Users(0, 'TestFirstName', 'TestLastName',
                  '000000', 'TestPassword', 0)
test_user_steve = Users(1, 'Steve', 'Steven', '100000', 'password', 0)

users = [test_user, test_user_steve]


class UserTest(unittest.TestCase):

    def test_create_user(self):
        new_user = user_dao.create_user(test_user)
        print(new_user)
        assert new_user.users_id != 0

    def test_get_user_by_id(self):
        retrieved_user = user_dao.get_user_by_id(test_user_steve.users_id)
        assert test_user_steve.first_name == retrieved_user.first_name

    def test_all_users(self):
        users = user_dao.get_all_users()
        assert all(users)

    def test_update_user(self):
        test_user.first_name = "NewName"
        test_user.last_name = "NewLastName"
        test_user.password = "NewPassword"
        test_user.users_id = 13  # THIS IS THE TEST USER IN MY OWN DB
        updated_user = user_dao.update_user(test_user)
        assert updated_user.first_name == test_user.first_name
        assert updated_user.last_name == test_user.last_name
        assert updated_user.password == test_user.password

    def test_delete_user(self):
        result = user_dao.delete_user(test_user.users_id)
        assert result == True
