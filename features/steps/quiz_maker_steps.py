from behave import given, when, then
from selenium.webdriver.safari.webdriver import WebDriver
from selenium.webdriver.common import keys
from time import sleep

from selenium.webdriver.common.keys import Keys

from features.pages.quiz_home_page import QuizHomePage


@given(u'The User is logged in')
def step_impl(context):
    driver: WebDriver = context.driver
    driver.get("file:///Users/prozachrx/Desktop/quiz-maker/presentation/index.html")
    driver.implicitly_wait(6)
    page: QuizHomePage = context.quiz_page
    page.loginName().send_keys("100000")
    page.loginPassword().send_keys("password")
    page.loginButton().click()


@when(u'The User selects a course')
def step_impl(context):
    quiz_page: QuizHomePage = context.quiz_page
    sleep(1)
    quiz_page.classesDisplay().select_by_visible_text("Potatos 101")
    sleep(1)


@then(u'The User view a list of test with grades')
def step_impl(context):
    quiz_page: QuizHomePage = context.quiz_page
    sleep(1)
    assert quiz_page.selectQuiz()[0]

@then(u'The user sees their cumulative grade')
def step_impl(context):
    assert context.quiz_page.classGrade() != ""


@given(u'The Teacher is logged in')
def step_impl(context):
    driver: WebDriver = context.driver
    driver.get("file:///Users/prozachrx/Desktop/quiz-maker/presentation/index.html")
    driver.implicitly_wait(6)
    page: QuizHomePage = context.quiz_page
    page.loginName().send_keys("200002")
    page.loginPassword().send_keys("password")
    page.loginButton().click()


@when(u'The user fills out quiz info')
def step_impl(context):
    page: QuizHomePage = context.quiz_page
    sleep(1)
    page.teacherClassDisplay().select_by_visible_text("Potatos 101")
    page.quizName().send_keys("Potatoes on mars")
    page.Question1().send_keys("What is the best vegetable to survive on mars with?")
    page.answer1().send_keys("Potatoes")
    page.answer2().send_keys("Carrots")
    page.answer3().send_keys("Tomato")
    page.answer4().send_keys("Cucumber")
    page.makeQuizButton().click()


@then(u'The page is refreshed')
def step_impl(context):
    sleep(1)
    assert context.quiz_page.Question1().get_attribute('value') == ""


@when(u'The User clicks a test')
def step_impl(context):
    context.quiz_page.selectQuiz()[0].click()


@when(u'The User answers the question')
def step_impl(context):
    context.quiz_page.answer1Radio().click()
    context.quiz_page.answer2Radio().click()
    context.quiz_page.submitQuizButton().click()


@then(u'The User views the test results')
def step_impl(context):
    assert context.quiz_page.quizResults()


@given(u'User is on the home page')
def step_impl(context):
    driver: WebDriver = context.driver
    driver.get("file:///Users/prozachrx/Desktop/quiz-maker/presentation/index.html")


@then(u'User views the test')
def step_impl(context):
    context.quiz_page.selectQuiz()
