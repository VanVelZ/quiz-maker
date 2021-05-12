from abc import abstractmethod, ABC


class CoursesDAO(ABC):

    @staticmethod
    @abstractmethod
    def get_all_courses():
        pass

    @staticmethod
    @abstractmethod
    def get_courses_by_id(courseid):
        pass
