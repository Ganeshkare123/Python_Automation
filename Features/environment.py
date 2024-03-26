import time

from selenium import webdriver

def before_all(context):
    print('Before all executed')


def before_scenario(context, scenario):
    browser_type = context.config.userdata.get("browser")
    context.browser_type = browser_type
    if browser_type == "chrome":
        driver = webdriver.Chrome()
    elif browser_type == "firefox":
        driver = webdriver.Firefox()
    elif browser_type == "IE":
        driver = webdriver.Ie()
    elif browser_type == "Edge":
        driver = webdriver.Edge()
    else:
        driver = webdriver.Chrome()
    driver.get("https://www.rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    print('Before scenario executed')
    context.driver = driver
    return driver


def after_scenario(context, scenario):
    context.driver.close()

