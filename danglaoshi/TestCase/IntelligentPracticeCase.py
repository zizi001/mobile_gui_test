from danglaoshi.Common import BaseMethod
import unittest
from danglaoshi.TestAction.Practice_Test.IntelligentPracticeAction import IntelligentPracticeAction
from danglaoshi.TestAction.Login_Test import LoginAction
from danglaoshi.Data.Elements import PositionIntellgentPractice
from ddt import ddt, data, unpack


@ddt
class IntelligentPracticeCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        BaseMethod.driver_open(True)
        LoginAction.login_out()
        LoginAction.login("15769270635", "123456")
        LoginAction.after_login()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        LoginAction.login_out()
        BaseMethod.driver_close()

    def test_page_element_check(self):
        # IntelligentPracticeAction.intelligentPracticeAction.app_intellgent_practice(5)
        BaseMethod.click(PositionIntellgentPractice.PositionIntellgentPractice.foot_home_button)
        BaseMethod.click_xpath(PositionIntellgentPractice.PositionIntellgentPractice.practice_chapter_xpath)
        BaseMethod.click(PositionIntellgentPractice.PositionIntellgentPractice.tv_intelligence_training)
        actual = BaseMethod.is_exist(PositionIntellgentPractice.PositionIntellgentPractice.tv_intelligence_training)
        BaseMethod.click(PositionIntellgentPractice.PositionIntellgentPractice.finish_test_button)
        self.assertEquals(actual, False)
        if not actual:
            self.assertEquals(actual, True)
        print("111111111111111111111111111111111111111111111111111111")

    def test_Intelligent_practice_question_bank(self):
        intelligentpracticeaction = IntelligentPracticeAction()
        # intelligentPracticeAction.app_intellgent_practice()
        intelligentpracticeaction.app_intellgent_practice(14)
        actual = BaseMethod.is_exist(PositionIntellgentPractice.PositionIntellgentPractice.finish_test_button)
        self.assertEquals(actual, True)
        # pass

    def test_answer_card(self):
        actual = BaseMethod.is_exist(PositionIntellgentPractice.PositionIntellgentPractice.finish_test_button)
        self.assertEquals(actual, True)
        pass

    def test_answer_Submit(self):
        actual = BaseMethod.is_exist(PositionIntellgentPractice.PositionIntellgentPractice.tv_assignment)
        self.assertEquals(actual, False)
        pass

    def test_collect_topic(self):
        actual = BaseMethod.is_exist_text("已收藏")
        self.assertEquals(actual, False)
        pass

    def test_submit_paper(self):
        actual = BaseMethod.is_exist(PositionIntellgentPractice.PositionIntellgentPractice.tv_answer)
        self.assertEquals(actual, False)
        pass

    def test_sheet(self):
        pass

    def test_correct_answer_rate(self):
        pass

    def test_submit_bounced(self):
        actual = BaseMethod.is_exist(PositionIntellgentPractice.PositionIntellgentPractice.md_content)
        self.assertEquals(actual, False)

    def test_confirm_submit(self):
        actual = BaseMethod.is_exist(PositionIntellgentPractice.PositionIntellgentPractice.md_buttonDefaultPositive)
        self.assertEquals(actual, False)

    def test_cancel_submit(self):
        actual = BaseMethod.is_exist(PositionIntellgentPractice.PositionIntellgentPractice.md_buttonDefaultNegative)
        self.assertEquals(actual, False)

    def test_tv_total(self):
        actual = BaseMethod.is_exist(PositionIntellgentPractice.PositionIntellgentPractice.tv_total)
        self.assertEquals(actual, True)


if __name__ == '__main__':
    unittest.main()
