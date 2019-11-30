from danglaoshi.Common import BaseMethod
import unittest
from danglaoshi.TestAction.Banner_Test import BannerAction
import ddt
from danglaoshi.Data.Elements import PositionBanner
from danglaoshi.TestAction.Login_Test import LoginAction


class BannerCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        BaseMethod.driver_open(True)
        LoginAction.login("13100000985", "123456")
        LoginAction.after_login()

    def setUp(self):
        pass

    def test_banner_slide(self):
        BannerAction.banner_exist()
        BaseMethod.sleep(6)

    def test_banner_broadcast(self):
        BannerAction.banner_broadcast()

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        LoginAction.login_out()
        BaseMethod.driver_close()


if __name__ == '__main__':
    unittest.main()


