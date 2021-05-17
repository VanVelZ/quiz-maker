from exceptions.resource_not_found import ResourceNotFound
from models.users import Users
from util.db_connection import connection
from daos.user_dao import UserDAO


class UserDAOImpl(UserDAO):

    @staticmethod
    def create_user(user):  # Create new User
        sql = "INSERT INTO users VALUES(DEFAULT, %s, %s, %s, %s ) RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql, [user.first_name, user.last_name, user.login_id, user.password, user.role_id])
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
            users = Users(record[0],
                          record[1],
                          record[2],
                          record[3],
                          record[4],
                          record[5])
            user_list.append(users.json())
        return user_list

    @staticmethod
    def get_users_by_id(userid):  # Retrieve  User  by ID from users and return
        sql = "SELECT * FROM users where id=%s"
        cursor = connection.cursor()
        cursor.execute(sql)
        record = cursor.fetchone()

        if record:
            return Users(record[0], record[1], record[2], record[3], record[4], record[5])
        else:
            raise ResourceNotFound(f"User with id: {userid} - Not Found")

    def update_user(self, change):  # Update user Table

        sql = "UPDATE users SET first_name = %s, last_name=%s, password=%s  WHERE id=%s RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql,
                       (change.first_name,
                        change.last_name,
                        change.password))
        connection.commit()
        record = cursor.fetchone()
        return Users(record[0], record[1], record[2], record[3])

    def delete_user(self, userid):  # Delete an  Employee  from Table
        sql = "DELETE FROM users WHERE id =%s"
        cursor = connection.cursor()
        cursor.execute(sql, [userid])
        connection.commit()


    # ----------- Testing section -------------
    def _test(self):
        pass
        user = UserDAO()
        users = user.get_all_users()

        print(users)

    if __name__ == '__main__':
        _test()
