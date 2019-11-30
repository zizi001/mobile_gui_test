from danglaoshi.Common import BaseMethod
import unittest
from danglaoshi.TestAction.Login_Test import LoginAction
from danglaoshi.Data.Elements import PositionLogin
from ddt import ddt, data, unpack


@ddt
class LoginCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        BaseMethod.driver_open(True)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        LoginAction.login_out()
        BaseMethod.driver_close()

    @data(("13100000121", "123456", False), ("", "", True), ("13100000121", "111222333", True),
          ("13100000", "", True), ("aaa", "123456", True))
    @unpack
    def test_login(self, username, password, expect):
        LoginAction.login(username, password)
        if not expect:
            LoginAction.after_login()
        BaseMethod.sleep(1)
        actual1 = BaseMethod.is_exist(PositionLogin.PositionLogin.bt_login)
        assert(actual1 == expect)
        if not expect:
            actual2 = BaseMethod.current_activity()
            assert (actual2 == ".Activity.MainActivity")
            LoginAction.login_out()
            BaseMethod.sleep(1)
            actual3 = BaseMethod.current_activity()
            assert (actual3 == ".Activity.LoginActivity")


if __name__ == '__main__':
    unittest.main()
