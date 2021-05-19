from abc import abstractmethod, ABC


class CoursesDAO(ABC):

    @abstractmethod
    def get_all_courses(self):
        pass

    @abstractmethod
<<<<<<< HEAD
    def get_courses_by_id(self, courseid):
=======
    def get_course_by_id(course_id):
>>>>>>> 2a6655c3720af1e58f5d5fc467702a56b09739f7
        pass

    @abstractmethod
    def get_courses_by_teacher_id(teacher_id):
        pass
