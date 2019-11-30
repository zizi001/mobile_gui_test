# -*- coding: UTF-8 -*-
'''课程购买&物流信息'''
from danglaoshi.Common import BaseMethod
import unittest
from danglaoshi.Data.Elements.PositionCurriculum1 import PositionCurriculum1
from danglaoshi.TestAction.Login_Test import LoginAction
from danglaoshi.TestAction.Course_Test import CourseListAction
from danglaoshi.Data.Elements.PositionChangeCity import PositionChangeCity
from danglaoshi.TestAction.Course_Test.PlayListAction import PlayListAction


class LogisticsInformationCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        BaseMethod.driver_open(True)
        LoginAction.login("13100000054", "123456")
        LoginAction.after_login()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # 点击进入课程页
    def test_LogisticsInformation1(self):
        BaseMethod.click(PositionCurriculum1.curriculum1)
        BaseMethod.click(PositionCurriculum1.curriculum_guidance)
        BaseMethod.sleep(2)
        self.assertEqual(BaseMethod.get_text(elem_detail=PositionCurriculum1.my_course1, by="id"), "我的课程", "错了")
        print(BaseMethod.get_text(elem_detail=PositionCurriculum1.my_course1, by="id"))

    # 点击课程
    def test_LogisticsInformation2(self):
        course_list_action = CourseListAction.CourseListAction()
        course_list_action.click_course(course_name="陕西招教备考指导")
        BaseMethod.sleep(2)
        course_list_action.click_course(course_name="陕西省教师招聘备考指导-自动化测试专用勿动！")
        BaseMethod.sleep(2)

    # 点课程购买
    def test_LogisticsInformation3(self):
        if BaseMethod.get_text(PositionCurriculum1.purchase_text) == "已购买":
            BaseMethod.click(PositionCurriculum1.look_course)
            BaseMethod.sleep(3)
        else:
            BaseMethod.click(PositionCurriculum1.look_course)
            BaseMethod.sleep(3)
            BaseMethod.click(PositionCurriculum1.get_course)
            BaseMethod.sleep(3)
            BaseMethod.click(PositionCurriculum1.see_course)
        BaseMethod.click(PositionCurriculum1.course_back1)
        BaseMethod.click(PositionCurriculum1.course_back1)

    # 返回主页
    # def test_LogisticsInformation4(self):
    #     my = BaseMethod.get_text(elem_detail=PositionCurriculum1.my_course1, by="id")
    #     while my != "我的课程":
    #         BaseMethod.click(PositionCurriculum1.course_back1)
    #     else:
    #         pass

    # 进入物流信息
    def test_LogisticsInformation5(self):
        BaseMethod.click(PositionChangeCity.foot_user)
        BaseMethod.click(PositionCurriculum1.logistics_xx)
        BaseMethod.sleep(2)
        self.assertEqual(BaseMethod.get_text(elem_detail=PositionCurriculum1.logistics_bt, by="id"), "物流信息", "错了")
        print(BaseMethod.get_text(elem_detail=PositionCurriculum1.logistics_bt, by="id"))

    # 进行效验并改地址
    def test_LogisticsInformation6(self):
        play_list_action = PlayListAction()
        title = play_list_action.swipe_get_text(ids=PositionCurriculum1.logistics_course)
        index1 = title.index("陕西省教师招聘备考指导-自动化测试专用勿动！")
        BaseMethod.click(elem_detail=PositionCurriculum1.change_address2, by='ids', i=index1)
        shou_name = play_list_action.swipe_get_text(ids=PositionCurriculum1.username_textview)
        index2 = shou_name.index("大声道")
        BaseMethod.click(elem_detail=PositionCurriculum1.username_textview, by='ids', i=index2)
        actual = BaseMethod.get_text(elem_detail=PositionCurriculum1.logistics_sh, by='ids', i=index1)
        self.assertEqual(actual, "大声道  13100000052", "修改地址出错")

    # # 返回
    # def test_LogisticsInformation7(self):
    #     BaseMethod.click(PositionCurriculum1.course_back)
    #
    # #  其他
    # def test_LogisticsInformation8(self):
    #     BaseMethod.click(PositionCurriculum1.course_back)

    @classmethod
    def tearDownClass(cls):
        LoginAction.login_out()
        BaseMethod.driver_close()


if __name__ == '__main__':
    unittest.main()
