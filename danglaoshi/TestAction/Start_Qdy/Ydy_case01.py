#! /usr/bin/env python
# -*- coding:utf-8 -*-
'''首次安装并启动，引导页面及闪屏'''

import unittest
import requests
from ddt import ddt, data, unpack
from danglaoshi.Common import SendRequests
from danglaoshi.Common import ReadExcel
import os

# path = os.path.dirname(os.getcwd())+"\\data\\yoyo_apiTest.xlsx"
# print(path)
testData = ReadExcel.readExcel("E:\\fukun_apitest\\data\\yoyo_apiTest.xlsx", "Sheet1")


@ddt
class Test1(unittest.TestCase):

    def setUp(self):
        self.s = requests.session()

    def tearDown(self):
        pass

    @data(*testData)
    def test_yoyo_api(self,data):

        re = SendRequests().sendRequests(self.s, data)
        #print(re.json())

        #切割字符串取后面的部分
        expect_result1 = data["expect_result"].split(":")[1]
        #转换为字符串
        expect_result = eval(expect_result1)
        #断言
        self.assertEqual(re.json()["origin"], expect_result, "返回错误,实际结果是%s"%re.json()["origin"])


if __name__ == '__main__':

    unittest.main()
