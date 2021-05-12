
# ---------------- Create a new user and return 201 status code for successful creation ----------------------
from flask import request, jsonify

from models.users import Users
from service.user_services import UserService


def route(app):
    @app.route("/user", methods=['POST'])
    # ----Create a new user
    def post_user():
        user = Users.json_parse(request.json)
        user_services = UserService.create_employee(user)
        return jsonify(user_services.json()), 201  # resource created

    # ----Retrieve all users from the database and return status code of 200 for successful retrieval
    @app.route("/users", methods=['GET'])
    def get_all_users():
        return jsonify(UserService.get_all_users()), 200

    # ---------------- Retrieve a user with a specific ID from the database and return status code of 200 for successful retrieval or 400 for bad request
    @app.route("/user/<userid>", methods=['GET'])
    def get_userby_id(userid):
        try:
            user = UserService.get_user_by_id(int(userid))

            return jsonify(user.json()), 200
        except ValueError as e:
            return "Not a valid ID or No such user exist with this ID", 400  # Bad Request
        # except ResourceNotFound as r:
        #     return r.message, 404

    # ---------------- Update a Employee  with an ID and return 200 status for a successful Update  or 404 ----------------------
    @app.route("/user/<userid>", methods=['PUT'])
    def update_user(userid):
        try:
            user = Users.json_parse(request.json)
            user.users_id = int(user)
            UserService.update_employee(user)
            return jsonify(user.json()), 200
        except ValueError as e:
            return "Not a valid ID or No such user exist with this ID", 400  # Bad Request
        # except ResourceNotFound as r:
        #     return r.message, 404

    # -------------delete with id -----------------
    @app.route("/user/<userid>", methods=['DELETE'])
    def del_user(userid):
        try:
            UserService.delete_employee(int(userid))
            return f'User with id of  {userid} has been deleted', 204
        except ValueError as e:
            return "Not a valid ID or No such user exist with this ID", 400  # Bad Request
        # except ResourceNotFound as r:
        #     return r.message, 404
