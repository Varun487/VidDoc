from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from .models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time
import hashlib


class TestLoginPage(StaticLiveServerTestCase):

    def setUp(self) -> None:
        # setup database
        User(
            name='test1',
            email='test1@gmail.com',
            password=hashlib.sha256('123'.encode()).hexdigest(),
            address='test1 address',
            age=12,
            city='abc',
            phone_number=1234567891,
        ).save()

        # setup browser
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def tearDown(self):
        self.browser.close()

    def init_login(self, testcase, username, password, css_id, correct_text):
        print(f'TESTING: {testcase}')
        self.browser.get(self.live_server_url)
        # time.sleep(0.5)
        self.browser.find_element_by_id('name').send_keys(username)
        # time.sleep(0.5)
        self.browser.find_element_by_id('password').send_keys(password)
        time.sleep(5)
        self.browser.find_element_by_id('submit').click()
        time.sleep(5)
        assert self.browser.find_element_by_id(css_id).text == correct_text
        print('PASSED')

    def test_login_correct_auth(self):
        self.init_login('login_correct_auth', 'test1', '123', 'appointments_home', 'VidDoc Appointments')

    def test_login_wrong_password(self):
        self.init_login('login_wrong_password', 'test1', '124', 'wrong_password',
                        'Please try again, either the username or password was wrong')

    def test_login_not_registered(self):
        self.init_login('login_not_registered', 'test2', '123', 'not_registered',
                        "It looks like it's your first time here. Please register here")

    def test_login_fill_required_fields(self):
        self.init_login('login_fill_required_fields', '', '', 'login_home', 'Login to VidDoc')


class TestRegisterPage(StaticLiveServerTestCase):

    def setUp(self) -> None:
        # setup database
        User(
            name='test1',
            email='test1@gmail.com',
            password=hashlib.sha256('123'.encode()).hexdigest(),
            address='test1 address',
            age=12,
            city='abc',
            phone_number=1234567891,
        ).save()

        # setup browser
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def tearDown(self):
        self.browser.close()

    def init_register(self, testcase, username, email, password, repeat_password, address, age, city, phone_number,
                      css_id, correct_text):
        print(f'TESTING: {testcase}')
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id('register_link').click()
        self.browser.find_element_by_id('name').send_keys(username)
        self.browser.find_element_by_id('email').send_keys(email)
        self.browser.find_element_by_id('password').send_keys(password)
        self.browser.find_element_by_id('repeat_password').send_keys(repeat_password)
        self.browser.find_element_by_id('address').send_keys(address)
        self.browser.find_element_by_id('age').send_keys(age)
        self.browser.find_element_by_id('city').send_keys(city)
        self.browser.find_element_by_id('phone_number').send_keys(phone_number)
        self.browser.find_element_by_id('register_button').click()
        time.sleep(2)
        assert self.browser.find_element_by_id(css_id).text == correct_text
        print('PASSED')

    def test_correct_registration(self):
        self.init_register('register_username_exists', 'test2', 'test2@gmail.com', '123', '123', 'address1', 12,
                           'city1', 1234567890, 'login_home',
                           'Login to VidDoc')

    def test_register_fill_required_fields(self):
        self.init_register('register_fill_required_fields', '', '', '', '', '', '', '', '', 'register_home',
                           'Register to VidDoc')

    def test_register_username_exists(self):
        self.init_register('register_username_exists', 'test1', 'test1@gmail.com', '123', '123', 'address1', 12,
                           'city1', 1234567890, 'invalid_user',
                           'A user with this name already exists, please try again with a different username.')

    def test_register_password_match(self):
        self.init_register('register_password_match', 'test2', 'test2@gmail.com', '123', '1234', 'address1', 12,
                           'city1', 1234567890, 'passwords_no_match',
                           'The passwords do not match! Please enter the same password in both fields.')

    def test_register_invalid_age(self):
        self.init_register('register_invalid_age', 'test2', 'test2@gmail.com', '123', '123', 'address1', -3,
                           'city1', 1234567890, 'invalid_age',
                           'Please enter an age within the range of 0 - 130 (inclusive)')

    def test_register_invalid_phone_number(self):
        self.init_register('register_invalid_phone_number', 'test2', 'test2@gmail.com', '123', '123', 'address1', 12,
                           'city1', 12345678901, 'invalid_phone_number',
                           'Please a 10 digit phone number')
