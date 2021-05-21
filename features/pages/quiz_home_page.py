from selenium.webdriver.safari.webdriver import WebDriver
from selenium.webdriver.support.select import Select


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
        return Select(self.driver.find_element_by_id('classes'))

    def teacherClassDisplay(self):
        return Select(self.driver.find_element_by_id("courseSelect"))

    def classGrade(self):
        return self.driver.find_element_by_id("classGrade")

    def quizName(self):
        return self.driver.find_element_by_id('quizName')

    def selectQuiz(self):
        return self.driver.find_elements_by_class_name("quizName")

    def Question1(self):
        return self.driver.find_element_by_id('q1Description')

    def answer1(self):
        return self.driver.find_element_by_id('a1_1')

    def answer2(self):
        return self.driver.find_element_by_id('a1_2')

    def answer3(self):
        return self.driver.find_element_by_id('a1_3')

    def answer4(self):
        return self.driver.find_element_by_id('a1_4')

    def answer1Radio(self):
        return self.driver.find_element_by_xpath('//*[@id="option1_1Radio"]/input')

    def quizResults(self):
        return self.driver.find_element_by_id("quizResults")

    def answer2Radio(self):
        return self.driver.find_element_by_xpath('//*[@id="option2_1Radio"]/input')

    def makeQuizButton(self):
        return self.driver.find_element_by_id('makeQuizButton')

    def submitQuizButton(self):
        return self.driver.find_element_by_id('submitQuiz')

