from daos.daos_impl.student_questions_dao_impl import StudentQuestionsDAOImpl


class StudentQuestionsServices:
    students_questions_services = StudentQuestionsDAOImpl()

    @classmethod
    def get_all_student_questions(cls):
        return cls.students_questions_services.get_all_questions()

