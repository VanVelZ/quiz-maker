from behave import given, when, then
from selenium.webdriver.safari.webdriver import WebDriver
from selenium.webdriver.common import keys
from time import sleep

from selenium.webdriver.common.keys import Keys


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


@when(u'The User clicks a test')
def step_impl(context):
    raise NotImplementedError(u'STEP: When The User clicks a test')


@then(u'The User views the test')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The User views the test')


@given(u'The User is viewing the test')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given The User is viewing the test')


@when(u'The User answers the questions')
def step_impl(context):
    raise NotImplementedError(u'STEP: When The User answers the questions')


@when(u'The User clicks on the submit button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When The User clicks on the submit button')


@then(u'The User views their score')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The User views their score')


@then(u'User views the test')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then User views the test')

