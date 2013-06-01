#!/bin/env python
#coding=utf8
'''
Created on 2012-12-7

@author: zhongying.sun
'''
import sys, os, re, unittest
sys.path.append(os.path.abspath(os.path.dirname(__file__))+os.path.sep+'lib')
import HTMLTestRunner
import time
import datetime
import util
import sendmail

def regressionTest():
    path = os.path.abspath(os.path.dirname(sys.argv[0]))   
    path = path + os.path.sep + 'testcase'
    sys.path.append(path)
    files = os.listdir(path)   
    test = re.compile("^Test.*.py$", re.IGNORECASE)  
    files = filter(test.search, files)
    
    test1 = re.compile("^Test(?!Demo).*$",re.IGNORECASE)
    files = filter(test1.search, files)
    
    filenameToModuleName = lambda f: os.path.splitext(f)[0]
    moduleNames = map(filenameToModuleName, files) 
    modules = map(__import__, moduleNames) 
    load = unittest.defaultTestLoader.loadTestsFromModule
    suites= map(load, modules)
    return unittest.TestSuite(map(load, modules))

def htmlRunner():
    ownermap = util.loadcaseowner()
    descinfo = "Python FrameWork Test Demo"
    fp = file(reportpath,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title='API Test Report',
            description=descinfo,
            owner = ownermap)
    runner.run(regressionTest())
    
def textRunner():
    runner = unittest.TextTestRunner()
    runner.run(regressionTest())
 
def sendMail():
    print 'Sending mail...'
    try:
        toList = 'yueye-22@163.com'
        today = datetime.date.today()
        check = "please check the report"
        content = open(reportpath).read()
        message = util.mailtmpl %(today,check,content)
        token1 = '<strong>Status:</strong>'
        token2 = '</p>'
        flag = util.getStatus(content,token1,token2)
        emailSender = sendmail.SMTP_SSL('smtp.ops.xxx-inc.com')
        fromAdd = 'tom@test.com'
        title = '[Python-test-Report][Demo]%s@%s' % (flag,time.strftime('%Y%m%d'))
        ccList = ''
        emailSender.SendHTML('', '', fromAdd, toList, ccList, title, message)
        print 'Sending mail done'
    except Exception, e:
        sys.stderr.write('Sending mail error: ' + str(e) + '\n')
         
if __name__ == '__main__':
    rootpath = os.path.abspath(os.path.dirname(__file__))
    reportpath = rootpath +  os.path.sep + 'report' + os.path.sep + ('report_%s.html' % time.strftime('%Y%m%d_%H%M%S',time.localtime()))
    if sys.argv[1] == "text":
        textRunner()                                                                                                                                               
    else:
        htmlRunner()
        sendMail()