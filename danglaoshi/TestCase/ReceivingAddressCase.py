
# coding:utf-8
import unittest
from danglaoshi.Common import BaseMethod
from danglaoshi.TestAction.Login_Test import LoginAction
from danglaoshi.Data.Elements.PositionMyCoupons import PositionMyCoupons
from danglaoshi.Data.Elements.PositionAddress import PositionAddress


class ReceivingAddressCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        BaseMethod.driver_open(True)
        LoginAction.login("13100000051", "123456")
        LoginAction.after_login()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # 进入&判断
    def test_about_the_address1(self):
        BaseMethod.click(PositionMyCoupons.user_center)
        BaseMethod.swipe_down(200)
        w = BaseMethod.get_text(elem_detail=PositionAddress.number_of_addresses, by="id")
        print(w)
        BaseMethod.sleep(2)
        BaseMethod.click(PositionAddress.receiving_address)
        BaseMethod.sleep(2)
        self.assertEqual(BaseMethod.get_text(elem_detail=PositionAddress.address_title1, by="id"), "收货地址", "错了")

    # 新建地址
    def test_about_the_address2(self):
        BaseMethod.click(PositionAddress.new_address1)
        self.assertEqual(BaseMethod.get_text(elem_detail=PositionAddress.new_address2, by="id"), "收货详细地址", "错了")
        BaseMethod.send(elem_detail=PositionAddress.enter_name_box1, value="王二", by="id")
        BaseMethod.send(elem_detail=PositionAddress.input_phone_box1, value="17051454452", by="id")
        BaseMethod.click(PositionAddress.regional_selection)
        BaseMethod.sleep(3)
        BaseMethod.click(PositionAddress.regional_det)
        self.assertEqual(BaseMethod.get_text(elem_detail=PositionAddress.post_election, by="id"), "北京市 东城区", "错了")
        BaseMethod.send(elem_detail=PositionAddress.address_input_box1, value="东城区睿成孵化园区教育基地", by="id")
        BaseMethod.click(PositionAddress.save_address1)
        BaseMethod.sleep(2)
        self.assertTrue(BaseMethod.get_text(elem_detail=PositionAddress.address_name1, by="id") == "王二")
        print(PositionAddress.address_name1)

    # 修改地址
    def test_about_the_address3(self):
        BaseMethod.click_xpath(PositionAddress.edit_layout1)
        BaseMethod.clean_text(elem_detail=PositionAddress.enter_name_box1)
        BaseMethod.send(elem_detail=PositionAddress.enter_name_box1, value="王二毛", by="id")
        BaseMethod.click(PositionAddress.save_address1)
        BaseMethod.sleep(3)
        self.assertTrue(BaseMethod.get_text(elem_detail=PositionAddress.address_name1, by="id") == "王二毛")
        print(PositionAddress.address_name1)
        BaseMethod.sleep(2)

    # 其他操作&新建够五条无法点击判断
    def test_about_the_address4(self):
        BaseMethod.click(PositionAddress.new_address1)
        BaseMethod.sleep(2)
        self.assertTrue(BaseMethod.get_text(elem_detail=PositionAddress.address_title1, by="id") == "收货地址")

    # 其他操作
    def test_about_the_address5(self):
        if self.assertTrue(BaseMethod.get_text(elem_detail=PositionAddress.address_title1, by="id") == "收货地址"):
            BaseMethod.click(PositionAddress.address_back1)

    @classmethod
    def tearDownClass(cls):
        LoginAction.login_out()
        BaseMethod.driver_close()


if __name__ == '__main__':
    unittest.main()
