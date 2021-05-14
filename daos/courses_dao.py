from abc import abstractmethod, ABC


class CoursesDAO(ABC):

    @abstractmethod
    def get_all_courses(self):
        pass

    @abstractmethod
    def get_course_id(self, courseid):
        pass
