from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox("/home/phil/browser_drivers/")

    def tearDown(self):
        self.browser.quit()

    def test_user_visits_blog(self):
        self.browser.get('http://127.0.0.1:8000/')
        assert 'IT Blog' in self.browser.title


    



