from behave import *
from selenium import webdriver
from Features.Pages.HomePage import HomePage


@Given('user enter the "{name}"')
def enter_name1(context, name):
    HomePage(context.driver).enter_name("Ganesh")


@when('enter the "email"')
def ent_email(context):
    HomePage(context.driver).enter_email("allen@gmail.com")


@when('enter the "Password"')
def password(context):
    HomePage(context.driver).enter_password("Testing@123")


@when('select the checkbox')
def selectcheckbox(context):
    HomePage(context.driver).select_checkbox()


@when('Select the "gender_type"')
def Select_Gender(context):
    HomePage(context.driver).select_gender("Female")


@when('Select the Employment_status')
def status(context):
    HomePage(context.driver).employment_status()


@when('enter the "date_of_birth"')
def birthdate(context):
    HomePage(context.driver).date_of_birth("2004-03-20")


@when('click on Submit button')
def submit(context):
    HomePage(context.driver).submit1()


@then('verify the "success_message" displayed on screen')
def verify_message(context):
    HomePage(context.driver).message1()
