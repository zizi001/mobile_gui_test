# -*- coding:utf-8 -*-
from danglaoshi.Common import BaseMethod
import unittest
from danglaoshi.TestAction.Login_Test import LoginAction
from danglaoshi.Data.Elements.PositionMyCollection import PositionMyCollection
from ddt import ddt, data, unpack
# import operator
import time


@ddt
class MyCollectionCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        BaseMethod.driver_open(True)
        LoginAction.login_out()
        LoginAction.login("15769270635", "123456")
        LoginAction.after_login()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        LoginAction.login_out()
        BaseMethod.driver_close()

    my_collection = PositionMyCollection()

    def test_my_no_collection_check(self):
        BaseMethod.click(elem_detail=self.my_collection.tv_practice)
        BaseMethod.click(elem_detail=self.my_collection.more_button)
        BaseMethod.click(elem_detail=self.my_collection.my_collection)
        BaseMethod.click(elem_detail=self.my_collection.get_my_collection_list(2), by="xpath", i=0)
        self.assertEqual(BaseMethod.is_exist(elem_detail=self.my_collection.tv_body), False)
        self.assertEqual(BaseMethod.is_exist(elem_detail=self.my_collection.no_collection), True)
        BaseMethod.click(elem_detail=self.my_collection.my_collection_back)
        BaseMethod.click(elem_detail=self.my_collection.collection_back)
        BaseMethod.click(elem_detail=self.my_collection.more_collection_back)

    def test_my_collection(self):
        BaseMethod.click(elem_detail=self.my_collection.tv_practice)
        BaseMethod.click(elem_detail=self.my_collection.more_button)
        BaseMethod.click(elem_detail=self.my_collection.my_collection)
        BaseMethod.click(elem_detail=self.my_collection.get_my_collection_list(1), by="xpath", i=0)
        self.assertEqual(BaseMethod.is_exist(elem_detail=self.my_collection.my_collection_title), True)
        self.assertEqual(BaseMethod.is_exist(elem_detail=self.my_collection.tv_body), True)
        self.assertEqual(BaseMethod.is_exist(elem_detail=self.my_collection.title_error_correction), True)
        self.assertEqual(BaseMethod.is_exist(elem_detail=self.my_collection.no_collection), False)
        BaseMethod.click(elem_detail=self.my_collection.my_collection_back)
        BaseMethod.click(elem_detail=self.my_collection.collection_back)
        BaseMethod.click(elem_detail=self.my_collection.more_collection_back)

    def test_remove_collection(self):
        BaseMethod.click(elem_detail=self.my_collection.tv_practice)
        BaseMethod.click(elem_detail=self.my_collection.more_button)
        BaseMethod.click(elem_detail=self.my_collection.my_collection)
        BaseMethod.click(elem_detail=self.my_collection.get_my_collection_list(1), by="xpath", i=0)
        before_remove_total_num = BaseMethod.get_text(elem_detail=self.my_collection.total_num)
        print("remove之前题目总数"+before_remove_total_num)
        BaseMethod.click(elem_detail=self.my_collection.collection_remove)
        after_remove_total_num = BaseMethod.get_text(elem_detail=self.my_collection.total_num)
        if int(before_remove_total_num[3]) > 2:
            self.assertEqual(after_remove_total_num, before_remove_total_num - 1)
        else:
            self.assertEqual(BaseMethod.is_exist(elem_detail=self.my_collection.no_collection), False)
        BaseMethod.click(elem_detail=self.my_collection.my_collection_back)
        BaseMethod.click(elem_detail=self.my_collection.collection_back)
        BaseMethod.click(elem_detail=self.my_collection.more_collection_back)

    def test_collection_from_practice(self):
        pass

    def test_cancel_collection_from_practice(self):
        pass

    def test_collection_data_validation(self):
        pass

    def test_wrong_topic_parsing(self):
        pass

    
if __name__ == '__main__':
    unittest.main()
