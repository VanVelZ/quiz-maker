from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from features.pages.quiz_home_page import QuizHomePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep


@given(u'The User is logged in')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given The User is logged in')


@when(u'The User clicks on view tests')
def step_impl(context):
    raise NotImplementedError(u'STEP: When The User clicks on view tests')


@then(u'The User views the list of test')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The User views the list of test')


@given(u'The User is viewing the tests')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given The User is viewing the tests')


@when(u'The User selects a test')
def step_impl(context):
    raise NotImplementedError(u'STEP: When The User selects a test')


@then(u'The User views the grade on the test')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The User views the grade on the test')


@given(u'The User login')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given The User login')


@given(u'User is on the home page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given User is on the home page')


@then(u'User views the accumulative grade')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then User views the accumulative grade')


@given(u'Users login')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Users login')


@then(u'User views the test results')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then User views the test results')


# -------------------------login steps ----------------------------------------
@given(u'The User is on the login page')
def step_impl(context):
    driver: WebDriver = context.driver
    driver.get(
        "file:///C:/Users/adoko/Documents/Java%20Raveture%20notes/Newproject2/quiz-maker/presentation/index.html")
    sleep(10)


@when(u'The user put in the username')
def step_impl(context):
    driver: WebDriver = context.driver
    WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, 'loginField')))
    driver.find_element_by_id('loginField').send_keys("tomtom")

    sleep(5)


@when(u'The user put in the password')
def step_impl(context):
    driver: WebDriver = context.driver
    WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, 'passField')))
    driver.find_element_by_id('passField').send_keys("tom")

    sleep(5)


@when(u'The User clicks on login button')
def step_impl(context):
    quiz_home_page: QuizHomePage = context.quiz_home_page
    quiz_home_page.loginButton().click()


@then(u'The User is viewing the test')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The User is viewing the test')


@then(u'User views the test')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then User views the test')

# @given(u'The User is logged in')
# def step_impl(context):
#     driver: WebDriver = context.driver
#     driver.get("file:///C:/Users/adoko/Documents/Java%20Raveture%20notes/Newproject2/quiz-maker/presentation/index.html")
#     sleep(10)
#

#
# @when(u'The User clicks on view tests')
# def step_impl(context):
#     quiz_home_page: QuizHomePage = context.quiz_home_page
#     quiz_home_page.selectQuiz().click()
#
#     # raise NotImplementedError(u'STEP: When The User clicks on view tests')
#
#
# @then(u'The User views the list of test')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then The User views the list of test')
#
#
# @given(u'The User is viewing the tests')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Given The User is viewing the tests')
#
#
# @when(u'The User selects a test')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When The User selects a test')
#
#
# @then(u'The User views the grade on the test')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then The User views the grade on the test')
#
#
# @given(u'The User login')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Given The User login')
#
#
# @given(u'User is on the home page')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Given User is on the home page')
#
#
# @then(u'User views the accumulative grade')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then User views the accumulative grade')
#
#
# @given(u'Users login')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Given Users login')
#
#
# @then(u'User views the test results')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then User views the test results')
#
#
# @when(u'The User clicks a test')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When The User clicks a test')
#
#
# @then(u'The User views the test')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then The User views the test')
#
#
# @given(u'The User is viewing the test')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Given The User is viewing the test')
#
#
# @when(u'The User answers the questions')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When The User answers the questions')
#
#
# @when(u'The User clicks on the submit button')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When The User clicks on the submit button')
#
#
# @then(u'The User views their score')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then The User views their score')
#
#
# @then(u'User views the test')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then User views the test')
#
