# 答题卡操作
from danglaoshi.Common import BaseMethod
import unittest
from danglaoshi.TestAction.Login_Test import LoginAction
from danglaoshi.TestAction.Practice_Test import BreakPracticeAction
from danglaoshi.Data.Elements import PositionPractice
from danglaoshi.Data.Elements import PositionAnalysis
from danglaoshi.TestAction.ParseCorrelation_test import ParsingWrong_Test


class AnswerCardCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        BaseMethod.driver_open(True)
        LoginAction.login("13100000997", "123456")
        LoginAction.after_login()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # 切换学段
    def test_answercard1(self):
        xueduan = BreakPracticeAction.BreakPracticeAction()
        xueduan.change_type_period("教师资格证", "中学")

    # 做题并点击全部解析答题卡
    def test_answercard2(self):
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
            BaseMethod.click(PositionAnalysis.PositionAnalysis.wrong_questions)

    # 判断是否进入答题卡界面
    def test_answercard3(self):
        BaseMethod.click(PositionAnalysis.PositionAnalysis.answer_card)
        BaseMethod.sleep(2)
        self.assertIsNotNone(BaseMethod.get_text(elem_detail="com.ruicheng.teacher:id/tv_titile", by='id'))

    # 进行答题卡标号点击
    def test_answercard4(self):
        expect = BaseMethod.get_text(elem_detail=PositionAnalysis.PositionAnalysis.third_questions, by='xpath')
        BaseMethod.click_xpath(PositionAnalysis.PositionAnalysis.third_questions)
        actual = BaseMethod.get_text(elem_detail="com.ruicheng.teacher:id/tv_usednum", by='id')
        print("expect:" + expect)
        print("actual:" + actual)
        assert(expect == actual)

    @classmethod
    def tearDownClass(cls):
        LoginAction.login_out()
        BaseMethod.driver_close()


if __name__ == '__main__':
    unittest.main()