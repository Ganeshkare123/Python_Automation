import time


from selenium.webdriver.support.select import Select
from Utilities.Baseclass import Baseclass
from seleniumpagefactory import PageFactory


class HomePage(Baseclass, PageFactory):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.log = Baseclass().get_logger(self)

    locators = {
        'Name': ('XPATH', "(//input[@name='name'])[1]"),
        'email': ('XPATH', "//input[@name='email']"),
        'password': ('ID', "exampleInputPassword1"),
        'checkbox': ('ID', "exampleCheck1"),
        'gender': ('XPATH', "//select[@id='exampleFormControlSelect1']"),
        'estatus': ('ID', "inlineRadio1"),
        'DOB': ('XPATH', "//input[@type='date']"),
        'submit_button': ('XPATH', "//input[@type='submit']"),
        'Success_Message1': ('XPATH', "//div[contains(@class,'alert alert-success')]"),
        'Shop': ('XPATH', "//a[@href='/angularpractice/shop']")
    }

    def enter_name(self, name):
        self.Name.set_text(name)

    def enter_email(self, email):
        self.email.send_keys(email)

    def enter_password(self, Password):
        self.password.send_keys(Password)

    def select_checkbox(self):
        self.checkbox.click()

    def select_gender(self, gender_type):
        select = Select(self.gender)
        select.select_by_visible_text(gender_type)

    def employment_status(self):
        self.estatus.click()

    def date_of_birth(self, date_of_birth):
        self.DOB.send_keys(date_of_birth)

    def submit1(self):
        self.submit_button.click()

    def message1(self):
        success_message = 'Success! The Form has been submitted successfully!.'
        #actual_result = self.Success_Message1.text
        actual_result = self.Success_Message1.text
        self.log.info("Text received from application is " + actual_result)
        try:
            assert actual_result == success_message
        except Exception as e:
            self.log.info(f"Exception occurred: {e}")

    def navigate_shop(self):
        self.shop.click()
