from selenium.webdriver.safari.webdriver import WebDriver

class QuizHomePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def loginName(self):
        return self.driver.find_element_by_id('loginField')

    def loginPassword(self):
        return self.driver.find_element_by_id('passField')

    def loginButton(self):
        return self.driver.find_element_by_id('loginButton')

    def logout(self):
        return self.driver.find_element_by_id('logoutButton')

    def studentNameDisplay(self):
        return self.driver.find_element_by_id('studentName')

    def classesDisplay(self):
        return self.driver.find_element_by_id('classes')

    def selectQuiz(self):
        return self.driver.find_elements_by_class_name('quizName')

    def Question1(self):
        return self.driver.find_elements_by_class_name('q1')

    def answer1(self):
        return self.driver.find_elements_by_class_name('a1_1')

    def answer2(self):
        return self.driver.find_elements_by_class_name('a1_2')

    def answer3(self):
        return self.driver.find_elements_by_class_name('a1_3')

    def answer4(self):
        return self.driver.find_elements_by_class_name('aq_4')

    def answer4Radio(self):
        return self.driver.find_elements_by_class_name('option1_4Radio')

    def makeQuizButton(self):
        return self.driver.find_elements_by_class_name('makeQuizButton')

    def submitQuizButton(self):
        return self.driver.find_elements_by_class_name('submitQuiz')

