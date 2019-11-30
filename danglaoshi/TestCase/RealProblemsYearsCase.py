import unittest
from danglaoshi.Common import BaseMethod
from danglaoshi.TestAction.Login_Test import LoginAction
from danglaoshi.TestAction.Practice_Test import BreakPracticeAction
from danglaoshi.Data.Elements.PositionRealProblemsYears import PositionRealProblemsYears
from danglaoshi.Data.Elements.PositionMyCollection import PositionMyCollection
from danglaoshi.TestAction.Practice_Test import RealExerciseAction


class RealProblemsYearsCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        BaseMethod.driver_open(True)
        LoginAction.login("13100000898", "123456")
        LoginAction.after_login()

    def setUp(self):
        pass

    def tearDown(self):

        pass

    # 切换学段
    def test_RealProblems1(self):
        xueduan = BreakPracticeAction.BreakPracticeAction()
        xueduan.change_type_period("教师资格证", "幼儿园")
        self.assertEqual(BaseMethod.get_text(elem_detail=PositionRealProblemsYears.homepagesection, by="id"), "教师资格证-幼儿园")

    # 点击更多
    def test_RealProblems2(self):
        real = RealExerciseAction.RealExerciseAction()
        BaseMethod.click(PositionMyCollection.more_button)
        BaseMethod.sleep(1)
        BaseMethod.click(PositionRealProblemsYears.realproblems)
        BaseMethod.sleep(1)
        BaseMethod.click(PositionRealProblemsYears.realproblemclicking)
        BaseMethod.click(PositionRealProblemsYears.guide1)
        i = 1
        while i <= 11:
            BaseMethod.sleep(1)
            real.multiple_real_questions()
            BaseMethod.sleep(1)
            BaseMethod.swipe_left(200)
            i = i + 1
        else:
            BaseMethod.sleep(3)

    # 真题答题卡
    def test_RealProblems3(self):
        BaseMethod.click(PositionRealProblemsYears.questionansweringcard)
        self.assertEqual(BaseMethod.get_text(PositionRealProblemsYears.titleanswercard), "答题卡", "答题卡有问题")

    # 真题答题卡操作
    def test_RealProblems4(self):
        BaseMethod.click_xpath(PositionRealProblemsYears.fifthquestions)
        BaseMethod.sleep(2)
        self.assertEqual(BaseMethod.get_text(PositionRealProblemsYears.titlecount), "5", "有问题")

    @classmethod
    def tearDownClass(cls):
        LoginAction.login_out()
        BaseMethod.driver_close()













if __name__ == '__main__':
    unittest.main()
