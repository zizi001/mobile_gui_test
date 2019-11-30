# -*- coding:utf-8 -*-
from danglaoshi.Common import BaseMethod
import unittest
from danglaoshi.TestAction.Login_Test import LoginAction
from danglaoshi.Data.Elements.PositionMyCoupons import PositionMyCoupons
from ddt import ddt, data, unpack
# import operator
# import time


@ddt
class MyCouponsCase(unittest.TestCase):
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

    my_coupons = PositionMyCoupons()

    def test_my_no_coupons(self):
        BaseMethod.click(elem_detail=self.my_coupons.user_center)
        coupon_num = BaseMethod.get_text(elem_detail=self.my_coupons.tv_coupon_num)
        print("优惠券为:"+coupon_num)
        if int(coupon_num[0]) == 0:
            BaseMethod.click(elem_detail=self.my_coupons.tv_coupon_num)
            self.assertEqual(BaseMethod.is_exist(elem_detail=self.my_coupons.no_coupon), True)
        BaseMethod.click(elem_detail=self.my_coupons.coupon_back)

    def test_my_have_coupons(self):
        BaseMethod.click(elem_detail=self.my_coupons.user_center)
        coupon_num = BaseMethod.get_text(elem_detail=self.my_coupons.tv_coupon_num)
        print("优惠券为:"+coupon_num)
        BaseMethod.click(elem_detail=self.my_coupons.tv_coupon_num)
        if int(coupon_num[0]) > 0:
            self.assertEqual(BaseMethod.is_exist(elem_detail=self.my_coupons.get_whole_coupons(coupon_num), by="xpath"),
                             False)
        BaseMethod.click(elem_detail=self.my_coupons.coupon_back)

    def test_use_coupons(self):
        pass

    def test_exchange_coupons(self):
        pass

    def test_invalid_exchange_coupons(self):
        pass

    def test_coupons_jump_course(self):
        pass

    def test_coupons_jump_collection(self):
        pass


if __name__ == '__main__':
    unittest.main()
