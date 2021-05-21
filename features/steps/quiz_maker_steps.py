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
    quiz_page.classesDisplay()[1].click()


@then(u'The User view a list of test with grades')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The User view a list of test with grades')


@then(u'The user sees their cumulative grade')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The user sees their cumulative grade')


@given(u'The Teacher is logged in')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given The Teacher is logged in')


@when(u'The user fills out quiz info')
def step_impl(context):
    raise NotImplementedError(u'STEP: When The user fills out quiz info')


@then(u'The page is refreshed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The page is refreshed')


@when(u'The User clicks a test')
def step_impl(context):
    raise NotImplementedError(u'STEP: When The User clicks a test')


@when(u'The User answers the question')
def step_impl(context):
    raise NotImplementedError(u'STEP: When The User answers the question')


@then(u'The User views the test results')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The User views the test results')


@given(u'User is on the home page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given User is on the home page')


@then(u'User views the test')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then User views the test')
