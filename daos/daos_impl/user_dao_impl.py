from models.users import User
from util.db_connection import connection
from daos.user_dao import UserDAO

class UserDAOImpl(UserDAO):

    def create_user(self, user):  # Create new User
        sql = "INSERT INTO users VALUES(DEFAULT, %s, %s, %s ) RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql, [user.first_name,  user.last_name, user.login_id, user.password])
        connection.commit()
        record = cursor.fetchone()

        return Employee(
            User(record[0], record[1], record[2], record[3], record[4]).json())

    def get_all_users(self):  # Retrieve all User from User and return
        sql = "SELECT * FROM users"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        user_list = []
        for record in records:
            users = User(record[0], record[1], record[2], record[3], record[4], record[5])
            user_list.append(users.json())
        return user_list

