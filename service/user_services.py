from daos.daos_impl.user_dao_impl import UserDAOImpl


class UserService:
    user_dao = UserDAOImpl()

    @classmethod
    def create_user(cls, user):
        return cls.user_dao.create_user(user)

    @classmethod
    def get_all_users(cls):
        return cls.user_dao.get_all_users()

    @classmethod
    def get_user_by_id(cls, userid):
        return cls.user_dao.get_user_by_id(userid)

    @classmethod
    def update_user(cls, user):
        return cls.user_dao.update_user(user)

    @classmethod
    def delete_user(cls, userid):
        return cls.user_dao.delete_user(userid)

