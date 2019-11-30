from danglaoshi.Common import BaseMethod
import unittest
from danglaoshi.TestAction.Login_Test import LoginAction
from danglaoshi.TestAction.Regist_Test import RegistAction
from danglaoshi.Data.Elements import PositionLogin
from ddt import ddt, data, unpack


@ddt
class RegistCase(unittest.TestCase):
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

    # 第一个为成功注册，每次执行应加1
    @data(("13200000010", "66666666", "123456", False), ("13300000002", "66666666", "", True),
          ("13300000002", "", "123456", True), ("13300000002", "1111", "123456", True), ("13300000002", "", "", True))
    @unpack
    def test_register(self, username, verification_code, pwd, expect):
        RegistAction.register(username, verification_code, pwd)
        actual1 = BaseMethod.is_exist(PositionLogin.PositionLogin.bt_register)
        assert(actual1 == expect)
        if not expect:
            actual2 = BaseMethod.current_activity()
            assert (actual2 == ".Activity.ChoiceOfSubjectsActivity")
            LoginAction.login(username, pwd)
            LoginAction.after_login()
            actual3 = BaseMethod.is_exist(PositionLogin.PositionLogin.bt_login)
            assert (actual3 == expect)
            actual4 = BaseMethod.current_activity()
            assert (actual4 == ".Activity.ChoiceOfSubjectsActivity")
            LoginAction.login_out()

    @data(("13300000001", True, False))
    @unpack
    def test_register_cancel(self, username, expect1, expect2):
        RegistAction.register_cancel(username)
        actual1 = BaseMethod.is_exist(PositionLogin.PositionLogin.bt_login)
        assert (actual1 == expect1)
        actual2 = BaseMethod.is_exist(PositionLogin.PositionLogin.bt_register)
        assert (actual2 == expect2)
        actual3 = BaseMethod.current_activity()
        assert (actual3 == ".Activity.LoginActivity")


if __name__ == '__main__':
    unittest.main()
