# 课程列表 & 课程表 & 赠品
import unittest, re
from ddt import ddt, data, unpack
from danglaoshi.Common import BaseMethod
from danglaoshi.Data.Elements.PositionCourseList import PositionCourseList
from danglaoshi.TestAction.Login_Test import LoginAction
from danglaoshi.TestAction.Course_Test.CourseListAction import CourseListAction


@ddt
class CourseListCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        BaseMethod.driver_open(True)
        LoginAction.login('13100000900', '123456')
        LoginAction.after_login()

    def setUp(self):
        self.course_list_action = CourseListAction()
        self.position_course_list = PositionCourseList()
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        LoginAction.login_out()
        BaseMethod.driver_close()

    @data(('教师资格证', '陕西招教备考指导', True), ('教师资格证', '测试混合直播', True),
          ('教师资格证', '无规格分销测试', True), ('教师招聘', '课程服务无信息测试', True),
          ('教师招聘', '测试面试分班课程', True))
    @unpack
    def test_course_list(self, exam_type, course_name, expect):
        self.course_list_action.change_type_period(exam_type, '中学')
        BaseMethod.click(self.position_course_list.foot_course)
        BaseMethod.sleep(1)
        if BaseMethod.is_exist(self.position_course_list.i_know):
            BaseMethod.click(self.position_course_list.i_know)
        BaseMethod.swipe_on('down', t=200)
        BaseMethod.sleep(2)
        actual = self.course_list_action.find_course(course_name)
        self.assertEqual(actual, expect, '课程未找到')

    def test_course_schedule(self):
        self.course_list_action.change_type_period('教师资格证', '中学')
        BaseMethod.click(self.position_course_list.foot_course)
        BaseMethod.sleep(1)
        if BaseMethod.is_exist(self.position_course_list.i_know):
            BaseMethod.click(self.position_course_list.i_know)
        self.course_list_action.click_course("陕西招教备考指导")
        self.course_list_action.click_course("陕西省教师招聘备考指导-自动化测试专用勿动！")
        BaseMethod.click(self.position_course_list.rb_course)
        actual1 = BaseMethod.get_text(elem_detail=self.position_course_list.tv_tittle, by='ids', i=0)
        expect1 = "职业能力倾向测验"
        actual2 = BaseMethod.get_text(elem_detail=self.position_course_list.tv_tittle, by='ids', i=1)
        expect2 = "自动化测试劵"
        BaseMethod.click(elem_detail=self.position_course_list.iv_back)
        BaseMethod.click(elem_detail=self.position_course_list.iv_back)
        self.assertEqual(actual1, expect1, '课程表中的课时名字错误')
        self.assertEqual(actual2, expect2, '课程表中的课时名字错误')

    def test_gift(self):
        self.course_list_action.change_type_period('教师资格证', '中学')
        BaseMethod.click(elem_detail=self.position_course_list.foot_course)
        BaseMethod.sleep(1)
        if BaseMethod.is_exist(elem_detail=self.position_course_list.i_know):
            BaseMethod.click(elem_detail=self.position_course_list.i_know)
        self.course_list_action.click_course("陕西招教备考指导")
        self.course_list_action.click_course("陕西省教师招聘备考指导-自动化测试专用勿动！")
        gift_num = BaseMethod.get_text(elem_detail=self.position_course_list.tv_gift_num)
        gift_num = int(re.sub("\D", "", gift_num))
        gift_type_out = []
        type_num = 1
        while BaseMethod.is_exist(elem_detail=self.position_course_list.gift_type_out_xpath(type_num), by="xpath"):
            gift_type_out.append(BaseMethod.get_text
                                 (elem_detail=self.position_course_list.gift_type_out_xpath(type_num), by="xpath"))
            type_num = type_num+1
        BaseMethod.click(elem_detail=self.position_course_list.tv_gift_num)
        num = 0
        gift_name = []
        gift_type_in = []
        while 1:
            if BaseMethod.is_exist(elem_detail=self.position_course_list.gift_name, by='ids', i=num):
                g_name = BaseMethod.get_text(elem_detail=self.position_course_list.gift_name, by='ids', i=num)
                g_type = BaseMethod.get_text(elem_detail=self.position_course_list.gift_type, by='ids', i=num)
                if not g_name in gift_name:
                    gift_name.append(g_name)
                    if not g_type in gift_type_in:
                        gift_type_in.append(g_type)
                        if g_type == "课程":
                            BaseMethod.click(elem_detail=self.position_course_list.gift_name, by='ids', i=num)
                            self.assertEqual(BaseMethod.get_text(elem_detail=self.position_course_list.tv_titile), "课程详情", "赠课跳转错误")
                            BaseMethod.click(elem_detail=self.position_course_list.iv_back)
                num = num+1
            else:
                last_before_swipe = BaseMethod.get_text(elem_detail=self.position_course_list.gift_name, by='ids', i=num-1)
                BaseMethod.swipe_up_small(t=1000)
                try:
                    last_after_swipe = BaseMethod.get_text(elem_detail=self.position_course_list.gift_name, by='ids', i=num-1)
                except Exception as error:
                    num = 0
                    print(error)
                    continue
                if last_before_swipe == last_after_swipe:
                    break
                else:
                    num = 0
        BaseMethod.click(elem_detail=self.position_course_list.iv_close)
        BaseMethod.click(elem_detail=self.position_course_list.iv_back)
        BaseMethod.click(elem_detail=self.position_course_list.iv_back)
        self.assertEqual(gift_num, gift_name.__len__(), "赠品个数不对")
        self.assertEqual(gift_type_out.__len__(), gift_type_in.__len__(), "赠品类型个数不对")
        self.assertEqual(gift_type_out, gift_type_in, "赠品类型不对")



