from models.users import Users
from util.db_connection import connection
from daos.user_dao import UserDAO

class UserDAOImpl(UserDAO):

    @staticmethod
    def create_user(user):  # Create new User
        sql = "INSERT INTO users VALUES(DEFAULT, %s, %s, %s, %s ) RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql, [user.first_name,  user.last_name, user.login_id, user.password, user.role_id])
        connection.commit()
        record = cursor.fetchone()

        return Users(users_id=record[0],
                     first_name=record[1],
                     last_name=record[2],
                     login_id=record[3],
                     password=record[4],
                     role_id=record[5])

    @staticmethod
    def get_all_users():  # Retrieve all User from User and return
        sql = "SELECT * FROM users"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        user_list = []
        for record in records:
            users = Users(record[0], record[1], record[2], record[3], record[4], record[5])
            user_list.append(users.json())
        return user_list


    ## for branch test only




