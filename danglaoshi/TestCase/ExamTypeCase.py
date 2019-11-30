from danglaoshi.Common import BaseMethod
import unittest
from danglaoshi.TestAction.Login_Test import LoginAction
from danglaoshi.Data.Elements import PositionPersonalCenter, PositionPractice
from danglaoshi.TestAction.PersonalCenter_Test import ExamTypeAction
from ddt import ddt, data, unpack


@ddt
class ExamTypeCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        BaseMethod.driver_open(True)
        LoginAction.login("13100000998", "123456")
        LoginAction.after_login()

    def setUp(self):
        BaseMethod.to_activity(".Activity.MainActivity")
        BaseMethod.click(PositionPersonalCenter.PositionPersonalCenter.foot_user)
        BaseMethod.click(PositionPersonalCenter.PositionPersonalCenter.tv_testtype)
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        LoginAction.login_out()
        BaseMethod.driver_close()

    @data(("教师资格证", "中学"), ("教师资格证", "小学"), ("教师资格证", "幼儿园"),
          ("教师招聘", "中学"), ("教师招聘", "小学"), ("教师招聘", "幼儿园"))
    @unpack
    def test_exam_type(self, style, period):
        actual1 = BaseMethod.current_activity()
        assert (actual1 == ".Activity.ChoiceOfSubjectsActivity")
        ExamTypeAction.exam_type(style, period)
        BaseMethod.to_activity(".Activity.MainActivity")
        actual2 = BaseMethod.get_text(PositionPractice.tv_title2)
        BaseMethod.click(PositionPersonalCenter.PositionPersonalCenter.foot_user)
        actual3 = BaseMethod.get_text(PositionPersonalCenter.PositionPersonalCenter.tv_testtype)
        expect = style + '-' + period
        print('*********' + expect)
        print('*********' + actual2)
        print('*********' + actual3)
        assert (actual2 == expect)
        assert (actual3 == expect)


if __name__ == '__main__':
    unittest.main()
