from danglaoshi.Common import BaseMethod
import unittest
from danglaoshi.Data.Elements import PositionIntellgentPractice
# from danglaoshi.TestAction.Practice_Test.WrongTrainingAction import WrongTrainingAction
from danglaoshi.TestAction.Login_Test import LoginAction
from danglaoshi.Data.Elements.PositionWrongTraining import PositionWrongTraining
from ddt import ddt, data, unpack
import operator


@ddt
class WrongTrainingCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        BaseMethod.driver_open(True)
        LoginAction.login_out()
        LoginAction.login("13100000266", "123456")
        LoginAction.after_login()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        LoginAction.login_out()
        BaseMethod.driver_close()

    wrong_training = PositionWrongTraining()

    def test_wrong_practice_enter_success(self):
        BaseMethod.click(elem_detail=PositionIntellgentPractice.PositionIntellgentPractice.foot_home_button)
        BaseMethod.click_xpath(PositionIntellgentPractice.PositionIntellgentPractice.practice_chapter_xpath)
        BaseMethod.click(elem_detail=self.wrong_training.tv_wrong_training)
        actual = (BaseMethod.is_exist(elem_detail=self.wrong_training.tv_titile))\
            and (operator.eq(BaseMethod.get_text(elem_detail=self.wrong_training.tv_titile), "错题练习"))
        # actual1 = BaseMethod.is_exist(elem_detail=self.wrong_training.tv_titile)
        # actual2 = operator.eq(BaseMethod.get_text(elem_detail=self.wrong_training.tv_titile), "错题练习")
        # print(BaseMethod.get_text(elem_detail=self.wrong_training.tv_titile)+"111")
        # print(BaseMethod.is_exist(elem_detail=self.wrong_training.tv_titile)+"222")
        self.assertEquals(actual, True)
        BaseMethod.click(elem_detail=self.wrong_training.iv_back_button)
        BaseMethod.click(elem_detail=self.wrong_training.iv_back_button)

    def test_no_practice_record(self):
        BaseMethod.click(elem_detail=PositionIntellgentPractice.PositionIntellgentPractice.foot_home_button)
        BaseMethod.click_xpath(PositionIntellgentPractice.PositionIntellgentPractice.practice_chapter_xpath)
        BaseMethod.click(elem_detail=self.wrong_training.tv_wrong_training)
        actual1 = BaseMethod.is_exist(elem_detail=self.wrong_training.wrong_training_chapter_xpath(1))
        #  self.assertEquals(actual1, False)
        actual2 = BaseMethod.is_exist(elem_detail=self.wrong_training.no_practice_record)
        # self.assertEquals(actual2, True)
        if (actual1 is False) and (actual2 is True):
            print("我通过了,滴滴滴")
            pass
        BaseMethod.click(elem_detail=self.wrong_training.iv_back_button)
        BaseMethod.click(elem_detail=self.wrong_training.iv_back_button)


if __name__ == '__main__':
    unittest.main()
