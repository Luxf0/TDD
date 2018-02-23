from selenium import webdriver
import unittest

class FirstVisitor(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome("F:\TDD\chromedriver.exe")
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_First(self):
        self.browser.get("http://localhost:8000")
        self.assertIn("To-Do",self.browser.title,msg='browser title was :'+ self.browser.title)
        #self.fail("finish the test!")


if __name__ == "__main__":
    unittest.main()