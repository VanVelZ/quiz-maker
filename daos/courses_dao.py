from abc import abstractmethod, ABC


class CoursesDAO(ABC):

    @staticmethod
    @abstractmethod
    def get_all_courses():
        pass

    @staticmethod
    @abstractmethod
    def get_courses_by_id(course_id):
        pass

    @staticmethod
    @abstractmethod
    def get_courses_by_teacher_id(teacher_id):
        pass
