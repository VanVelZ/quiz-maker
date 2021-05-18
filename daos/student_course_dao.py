from abc import abstractmethod, ABC


class StudentCoursesDAO(ABC):

    @abstractmethod
    def get_all_student_courses(self):
        pass

    @abstractmethod
    def get_courses_by_id(course_id):
        pass
