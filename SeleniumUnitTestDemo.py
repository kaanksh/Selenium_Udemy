import unittest
from selenium import webdriver
import HtmlTestRunner


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path = "../drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()



    def test_search_1(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Automation Step by Step")
        self.driver.find_element_by_name('btnK').click()
        x = self.driver.title
        print(x)
        self.assertEqual(x, "Automation Step by Step - Google Search")

    def test_search_2(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Raghav Pal")
        self.driver.find_element_by_name('btnK').click()
        x = self.driver.title
        print(x)
        self.assertEqual(x, "Raghav Pal - Google Search")

    @unittest.skip("This is a skipped test.")
    def test_skip(self):
        """ This test should be skipped. """


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Dell/PycharmProjects/Selenium/reports'), verbosity=2)
