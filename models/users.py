class Users:

    def __init__(self, users_id=0, first_name="", last_name="", login_id="",  password="", role_id=0):
        self.users_id = users_id
        self.first_name = first_name
        self.last_name = last_name
        self.login_id = login_id
        self.password = password
        self.role_id = role_id

    def json(self):
        return {
            'usersId': self.users_id,
            'firstName': self.first_name,
            'lastName': self.last_name,
            'loginId': self.login_id,
            'password': self.password,
            'roleId': self.role_id,
        }

    @staticmethod
    def json_parse(json):
        users = Users()
        users.users_id = json["usersId"]
        users.first_name = json["firstName"]
        users.last_name = json["lastName"]
        users.login_id = json["loginId"]
        users.password = json["password"]
        users.role_id = json["roleId"]
        print(users)
        return users

    def __repr__(self):
        return str(self.json())
