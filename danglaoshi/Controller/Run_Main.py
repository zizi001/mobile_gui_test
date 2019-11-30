#! /usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
import time
import os
import HTMLTestRunner


def run_case(dir="testcase"):
    case_dir = os.getcwd() + "\\" + dir
    print(case_dir)
    test_case = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir, pattern="case_01_yoyo.py", top_level_dir=None)
    return discover


if __name__ == '__main__':
    current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    report_path = os.getcwd() + "\\report\\" + current_time + '.html'  # 生成测试报告的路径
    print(report_path)
    fp = open(report_path, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"自动化测试报告", description=u'yoyo接口', verbosity=2)
    runner.run(run_case())
    fp.close()
