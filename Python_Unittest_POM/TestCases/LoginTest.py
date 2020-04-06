import unittest
import HtmlTestRunner
from selenium import webdriver
import time
import sys

sys.path.append("/Users/tatiana/Desktop/PROJECTS/UnitTest_POM/Python_Unittest_POM")
from Pages.LoginPage import LoginPage


class LoginTest(unittest.TestCase):
    link = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    username = "admin@yourstore.com"
    password = "admin"
    driver = webdriver.Chrome(executable_path="/Users/tatiana/Desktop/PROJECTS/UnitTest_POM/Python_Unittest_POM/Drivers/chromedriver")

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.link)
        cls.driver.maximize_window()

    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.setUserName(self.username)
        login_page.setPassword(self.password)
        login_page.clickLoginBtn()

        time.sleep(5)
        self.assertEqual("Dashboard / nopCommerce administration", self.driver.title, "\nThe title of the page NOT matching")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("\nThe browser is closed")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="Reports"))
