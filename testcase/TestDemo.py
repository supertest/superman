'''
Created on 2012-12-7

@author: zhongying.sun
'''
import unittest
import time


class TestDemo(unittest.TestCase):


    def setUp(self):
        print "%s:Begin Test ...." % time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())


    def tearDown(self):
        print "%s:End Test ...." % time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())



    def testAdd(self):
        a=1
        b=21
        c=a+b
        self.assertEqual(c, 3, "a+b=!3;a=%s,b=%s"%(a,b)) 

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestDemo('testAdd'))
    
    return suite
if __name__ == "__main__":
    unittest.main()