'''
Created on 2012-12-7

@author: zhongying.sun
'''
#!/usr/bin/python
#coding=utf-8
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestSelenium(unittest.TestCase):

    def setUp(self):
        print "%s:Begin Test ...." % time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
        self.browser = webdriver.Firefox() # Get local session of firefox
        self.browser.get("http://www.baidu.com") # Load page
    def tearDown(self):
        self.browser.close()
        print "%s:End Test ...." % time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())



    def testBaidu(self):
        elem = self.browser.find_element_by_id("kw") # Find the query box
        elem.send_keys("seleniumhq" + Keys.RETURN)
        time.sleep(0.2) # Let the page load, will be added to the API
        actual="%s" % self.browser.title
        expect="seleniumhq"
        self.assertTrue(expect in actual, "The title not contain +%s:Title is :%s"% (expect,actual))

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestSelenium('testBaidu'))
if __name__ == "__main__":
    unittest.main()
