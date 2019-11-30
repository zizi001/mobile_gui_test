import unittest
from ddt import ddt, data, unpack
from danglaoshi.Common import BaseMethod
from danglaoshi.Data.Elements.PositionChangeCity import PositionChangeCity
from danglaoshi.TestAction.Login_Test import LoginAction


@ddt
class ChangeCityCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        BaseMethod.driver_open(True)
        LoginAction.login("13100000991", "123456")
        LoginAction.after_login()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        LoginAction.login_out()
        BaseMethod.driver_close()

    @data(('北京市', '北京市', True), ('河北省', '辛集市', False), ('澳门特别行政区', '澳门', True),
          ('陕西省', '西安市', False), ('陕西省', '商洛市', False))
    @unpack
    def test_change_city(self, province, city, straight_city):
        position_change_city = PositionChangeCity()
        BaseMethod.click(elem_detail=position_change_city.foot_user)
        BaseMethod.click(elem_detail=position_change_city.tv_city)
        BaseMethod.sleep(1)
        i = 1
        while 1:
            if BaseMethod.is_exist(elem_detail=position_change_city.province_xpath(i), by='xpath'):
                if BaseMethod.get_text(elem_detail=position_change_city.province_xpath(i), by='xpath') == province:
                    break
                else:
                    i = i+1
            else:
                BaseMethod.swipe_up(1000)
                BaseMethod.sleep(1)
                i = 1
        BaseMethod.click(elem_detail=position_change_city.province_xpath(i), by='xpath')
        BaseMethod.sleep(1)
        j = 1
        while 1:
            if BaseMethod.is_exist(elem_detail=position_change_city.city_xpath(j, straight_city), by='xpath'):
                if BaseMethod.get_text(elem_detail=position_change_city.city_xpath(j, straight_city), by='xpath') == city:
                    break
                else:
                    j = j + 1
            elif BaseMethod.is_exist(elem_detail=position_change_city.city_xpath(j, straight_city), by='xpath'):
                BaseMethod.swipe_up(600)
                BaseMethod.sleep(1)
                j = 1
        BaseMethod.click(elem_detail=position_change_city.city_xpath(j, straight_city), by='xpath')
        actual_city = BaseMethod.get_text(elem_detail=position_change_city.tv_city)
        self.assertEqual(actual_city, city, '报考城市修改失败')

    def test_clear_cache(self):
        position_change_city = PositionChangeCity()
        BaseMethod.click(elem_detail=position_change_city.foot_user)
        BaseMethod.swipe_on('up')
        BaseMethod.click(elem_detail=position_change_city.tv_cachesize)
        BaseMethod.click(elem_detail=position_change_city.md_buttonDefaultPositive)
        BaseMethod.sleep(1)
        actual = BaseMethod.get_text(elem_detail=position_change_city.tv_cachesize)
        self.assertEqual(actual, '0.00KB', '缓存未清空')
