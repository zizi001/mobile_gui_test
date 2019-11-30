# 解析相关
from danglaoshi.Common import BaseMethod
import unittest
from danglaoshi.Data.Elements import PositionPractice
from danglaoshi.TestAction.Login_Test import LoginAction
from danglaoshi.Data.Elements import PositionAnalysis
from danglaoshi.TestAction.ParseCorrelation_test import ParsingWrong_Test
from danglaoshi.TestAction.Practice_Test import BreakPracticeAction
from danglaoshi.Data.Elements.PositionRealProblemsYears import PositionRealProblemsYears


class AnalysisCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        BaseMethod.driver_open(True)
        LoginAction.login("13100000998", "123456")
        LoginAction.after_login()

    def setUp(self):
        pass

    def tearDown(self):

        pass

    # 切换学段
    def test_analysis1(self):
        xueduan = BreakPracticeAction.BreakPracticeAction()
        xueduan.change_type_period("教师资格证", "中学")
        self.assertEqual(BaseMethod.get_text(elem_detail=PositionRealProblemsYears.homepagesection, by="id"),
                         "教师资格证-中学")

    # 做题并判断多选&点进错题解析
    def test_analysis2(self):
        BaseMethod.click_xpath(PositionAnalysis.PositionAnalysis.tv_practice_button)
        BaseMethod.sleep(1)
        BaseMethod.click(PositionAnalysis.PositionAnalysis.checkmark1, 'xpath')
        BaseMethod.click(PositionPractice.tv_open)
        i = 1
        while i <= 15:
            BaseMethod.sleep(2)
            ParsingWrong_Test.multiple_choice_questions()
            BaseMethod.sleep(2)
            i = i+1
        else:
            BaseMethod.sleep(3)
        # wrong_n = ParsingWrong_Test.number_wrong_questions()
        # print(wrong_n)
        # BaseMethod.click(PositionPractice.tv_erro)
        # BaseMethod.click(PositionAnalysis.PositionAnalysis.guide_wrong_problem)

    # 判断错题数目并输出
    def test_analysis3(self):
        p = 15 - ParsingWrong_Test.number_wrong_questions()
        BaseMethod.click(PositionPractice.tv_erro)
        BaseMethod.click(PositionAnalysis.PositionAnalysis.guide_wrong_problem)
        while p >= 0:
            BaseMethod.swipe_left(200)
            p = p - 1
            BaseMethod.sleep(2)
        else:
            BaseMethod.click(PositionAnalysis.PositionAnalysis.wrong_question_return)

    # 进行错题解析界面操作&判断
    def test_analysis4(self):
        BaseMethod.click(PositionAnalysis.PositionAnalysis.wrong_questions)
        self.assertIsNotNone(BaseMethod.get_text(elem_detail="com.ruicheng.teacher:id/tv_titile", by='id'))
        print(BaseMethod.get_text(elem_detail="com.ruicheng.teacher:id/tv_titile", by='id'))
        BaseMethod.swipe_left(200)
        BaseMethod.click(PositionAnalysis.PositionAnalysis.wrong_question_return)

    def test_analysis5(self):
        BaseMethod.click(PositionAnalysis.PositionAnalysis.all_parsing)

    def test_analysis6(self):
        BaseMethod.swipe_left(300)

    @classmethod
    def tearDownClass(cls):
        LoginAction.login_out()
        BaseMethod.driver_close()


if __name__ == '__main__':
    unittest.main()
