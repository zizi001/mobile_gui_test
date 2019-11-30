from danglaoshi.Common import BaseMethod
import unittest
from danglaoshi.TestAction.Login_Test import ThreeLoginAction
from danglaoshi.TestAction.Login_Test import LoginAction


class ThreeLoginCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        BaseMethod.driver_open(True)
        BaseMethod.sleep(4)

    def setUp(self):
        pass

    def test_ThreeLogin(self):
        ThreeLoginAction.Threelogin_click()
        BaseMethod.sleep(3)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        LoginAction.login_out()
        BaseMethod.driver_close()


if __name__ == '__main__':
    unittest.main()