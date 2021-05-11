class Student:
    def __init__(self):
        pass

    def json(self):
        return {

        }

    @staticmethod
    def json_parse(json):  # convert to JSON format
        student = Student()

        return student

    def __repr__(self):
        return str(self.json())
