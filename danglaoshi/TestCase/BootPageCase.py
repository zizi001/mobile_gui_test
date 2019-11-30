from appium import webdriver
from danglaoshi.Common import BaseMethod
import unittest


class BootPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        BaseMethod.driver_open(False)

    def setUp(self):
        pass

    def test_boot_page(self):
        BaseMethod.swipe_left(800)
        BaseMethod.sleep(2)
        BaseMethod.swipe_left(800)
        BaseMethod.sleep(2)
        BaseMethod.click("com.ruicheng.teacher:id/rl_logo")
        BaseMethod.sleep(3)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        BaseMethod.driver_close()