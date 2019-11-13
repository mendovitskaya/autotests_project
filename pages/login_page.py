from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators
from selenium import webdriver
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка на корректный url адрес
        assert "login" in self.browser.current_url, "login not in current url"
        assert True

    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "Login email is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login password is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORGET_PASSWORD), "Link forget password is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_SUBMIT), "Login submit button is not presented"
        assert True

    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL), "Registration email is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD), "Registration password is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD), "Confirm password is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_SUBMIT), "Registration submit button is not presented"
        assert True

    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        password = "Stepik123!"
        reg_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        reg_email.send_keys(email)
        reg_password = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        reg_password.send_keys(password)
        reg_confirm_password = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD)
        reg_confirm_password.send_keys(password)
        reg_submit = self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT)
        reg_submit.click()
    

