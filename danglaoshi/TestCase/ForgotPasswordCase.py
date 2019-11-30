from danglaoshi.Common import BaseMethod
import unittest
from danglaoshi.TestAction.ForgotPassword_Test import ForgotPasswordAction
from danglaoshi.TestAction.Login_Test import LoginAction
from danglaoshi.Data.Elements import PositionLogin
from ddt import ddt, data, unpack


@ddt
class ForgotPasswordCase(unittest.TestCase):
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

    @data(("13100000001", "66666666", "123456789", False), ("13100000001", "66666666", "", True),
          ("13100000001", "", "123456", True), ("13100000001", "11111", "123456", True), ("13100000001", "", "", True))
    @unpack
    def test_forgot_password(self, username, verification_code, pwd, expect):
        ForgotPasswordAction.forget_password(username, verification_code, pwd)
        actual1 = BaseMethod .is_exist(PositionLogin.PositionLogin.bt_register)
        assert (actual1 == expect)
        if not expect:
            actual2 = BaseMethod.current_activity()
            assert (actual2 == ".Activity.RegisterActivity")
            BaseMethod.send(PositionLogin.PositionLogin.password, pwd)
            BaseMethod.click(PositionLogin.PositionLogin.bt_login)
            LoginAction.after_login()
            BaseMethod.sleep(1)
            actual3 = BaseMethod.current_activity()
            assert (actual3 == ".Activity.MainActivity")
            LoginAction.login_out()
            ForgotPasswordAction.forget_password(username, verification_code, "123456")
            BaseMethod.send(PositionLogin.PositionLogin.password, pwd)
            BaseMethod.click(PositionLogin.PositionLogin.bt_login)
            actual4 = BaseMethod.current_activity()
            assert (actual4 == ".Activity.RegisterActivity")

    @data(("13100000001", True, False))
    @unpack
    def test_forgot_password_cancel(self, username, expect1, expect2):
        ForgotPasswordAction.forget_password_cancel(username)
        actual1 = BaseMethod.is_exist(PositionLogin.PositionLogin.bt_login)
        assert (actual1 == expect1)
        actual2 = BaseMethod.is_exist(PositionLogin.PositionLogin.bt_register)
        assert (actual2 == expect2)
        actual3 = BaseMethod.current_activity()
        assert (actual3 == ".Activity.RegisterActivity")


if __name__ == '__main__':
    unittest.main()
