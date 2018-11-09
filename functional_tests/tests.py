from selenium import webdriver
import unittest

from selenium.webdriver.chrome.options import Options


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.browser = webdriver.Chrome(chrome_options=chrome_options)

    def tearDown(self):
        self.browser.quit()

    def test_user_visits_blog(self):
        self.browser.get('http://127.0.0.1:8000/')
        assert 'IT Blog' in self.browser.title


    



