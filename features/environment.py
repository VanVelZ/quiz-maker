from selenium import webdriver
from selenium.webdriver.safari.webdriver import WebDriver
from features.pages.quiz_home_page import QuizHomePage


def before_all(context):
    driver: WebDriver = webdriver.Chrome(
        "C:/Users/adoko/Documents/2104-python-java-wvu/chromedriver.exe")
    # driver: WebDriver = webdriver.Chrome()
    driver.maximize_window()
    quiz_page = QuizHomePage(driver)
    context.driver = driver
    context.quiz_page = quiz_page


# def after_all(context):
#     context.driver.quit()
