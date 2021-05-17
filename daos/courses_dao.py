from abc import abstractmethod, ABC


class CoursesDAO(ABC):

    @abstractmethod
    def get_all_courses(self):
        pass

    @abstractmethod
    def get_course_by_id(self, courseid):
        pass

    @abstractmethod
    def get_courses_by_teacher_id(self, teacher_id):
        pass
