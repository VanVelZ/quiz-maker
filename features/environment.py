from selenium import webdriver
from selenium.webdriver.safari.webdriver import WebDriver
from features.pages.quiz_home_page import QuizHomePage

# All setup and teardown functions must go in this file.
# These functions must be named using behave's conventions


def before_all(context):

    driver: WebDriver = webdriver.safari()
    quiz_home_page = QuizHomePage(driver)

    context.driver = driver
    context.quiz_home_page = quiz_home_page
    print("started")


def after_all(context):
    context.driver.quit()
    print("ended")
