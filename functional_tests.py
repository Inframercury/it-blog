from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    


browser = webdriver.Firefox()
browser.get('http://127.0.0.1:8000/')

assert 'It Blog' in browser.title
