from abc import abstractmethod, ABC


class StudentCoursesDAO(ABC):

    @staticmethod
    @abstractmethod
    def all_courses():
        pass

    @staticmethod
    @abstractmethod
    def get_courses_by_id(empid, courseid):
        pass
