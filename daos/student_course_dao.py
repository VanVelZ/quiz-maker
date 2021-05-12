from abc import abstractmethod, ABC


class StudentCoursesDAO(ABC):

    @abstractmethod
    def all_courses(self):
        pass

    @abstractmethod
    def get_courses_by_id(self, empid, courseid):
        pass
