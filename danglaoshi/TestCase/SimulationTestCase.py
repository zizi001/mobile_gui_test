# -*- coding:utf-8 -*-
# 模考大赛
from danglaoshi.Common import BaseMethod
import unittest
from danglaoshi.TestAction.Login_Test import LoginAction
from danglaoshi.Data.Elements.PositionMoreSimulationTest import PositionMoreSimulationTest
from ddt import ddt, data, unpack


@ddt
class SimulationTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        BaseMethod.driver_open(True)
        LoginAction.login("13100000889", "123456")
        LoginAction.after_login()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        LoginAction.login_out()
        BaseMethod.driver_close()

    def test_simulation_sign(self):
        position_simulation = PositionMoreSimulationTest()
        BaseMethod.click(position_simulation.tv_left_title)
        BaseMethod.click(position_simulation.rl_mokao)
        BaseMethod.sleep(2)
        i = 1
        while 1:
            if BaseMethod.is_exist(elem_detail=position_simulation.mokao_list_title_xpath(i), by='xpath'):
                if BaseMethod.get_text(elem_detail=position_simulation.mokao_list_title_xpath(i), by='xpath') \
                        == "1 自动化使用模考--请勿更改--报名":
                    print('等于的时候i=' + str(i))
                    break
                else:
                    i = i + 1
            elif not BaseMethod.is_exist(elem_detail=position_simulation.mokao_list_title_xpath(i), by='xpath'):
                print('未找到的i='+str(i))
                BaseMethod.sleep(1)
                BaseMethod.swipe_on(direction='up', t=1000)
                BaseMethod.sleep(1)
                i = 1
        status_list = BaseMethod.get_text(elem_detail=position_simulation.mokao_list_status_xpath(i), by='xpath')
        self.assertEqual(status_list, '报名参加', "模考列表页状态：" + status_list + " != 预期模考列表页状态：报名参加")
        time_list = BaseMethod.get_text(elem_detail=position_simulation.mokao_list_time_xpath(i), by='xpath')
        BaseMethod.click(elem_detail=position_simulation.mokao_list_title_xpath(i), by='xpath')
        title_detail = BaseMethod.get_text(elem_detail=position_simulation.tv_title_content)
        self.assertEqual(title_detail, '自动化使用模考--请勿更改--报名',
                         "模考详情页标题：" + title_detail + " != 预期模考详情页标题：自动化使用模考--请勿更改--报名")
        time_detail = BaseMethod.get_text(elem_detail=position_simulation.tv_time_day)
        self.assertEqual(time_detail, time_list, "模考详情页时间：" + time_detail + " != 模考列表页时间：" + time_list)
        status_detail = BaseMethod.get_text(elem_detail=position_simulation.textConfirm)
        self.assertEqual(status_detail, '立即报名', "模考详情页状态：" + status_detail + " != 预期模考详情页状态：立即报名")
        BaseMethod.click(elem_detail=position_simulation.textConfirm)
        BaseMethod.click(elem_detail=position_simulation.period_xpath(1), by='xpath')
        BaseMethod.click(elem_detail=position_simulation.subject_xpath(1), by='xpath')
        BaseMethod.click(elem_detail=position_simulation.btn_buy_input_message)
        BaseMethod.sleep(1)
        title_after_sign_up = BaseMethod.get_text(elem_detail=position_simulation.tv_titile)
        self.assertEqual(title_after_sign_up, '模考大赛', "报名后顶部标题：" + title_after_sign_up + " != 预期报名后顶部标题：模考大赛")
        exam_title = BaseMethod.get_text(elem_detail=position_simulation.tv_title)
        self.assertEqual(exam_title, '自动化测试劵--勿动', "试卷标题：" + exam_title + " != 预期试卷标题：自动化测试劵--勿动")
        exam_status = BaseMethod.get_text(elem_detail=position_simulation.tv_start)
        self.assertEqual(exam_status, '报名成功', "试卷状态：" + exam_status + " != 预期试卷状态：报名成功")
        BaseMethod.click(elem_detail=position_simulation.iv_back)
        status_detail = BaseMethod.get_text(elem_detail=position_simulation.textConfirm)
        self.assertEqual(status_detail, '进入考场', "报名后模考详情页状态：" + status_detail + " != 预期报名后模考详情页状态：进入考场")
        BaseMethod.click(position_simulation.iv_back)
        status_list = BaseMethod.get_text(elem_detail=position_simulation.mokao_list_status_xpath(i), by='xpath')
        self.assertEqual(status_list, '已报名', "报名后模考列表页状态：" + status_list + " != 报名后预期模考列表页状态：已报名")
        BaseMethod.click(position_simulation.iv_back)
        BaseMethod.click(PositionMoreSimulationTest.ll_my_mokao)
        BaseMethod.sleep(1)
        i = 1
        my_mokao_status = '无'
        while 1:
            if BaseMethod.is_exist(elem_detail=position_simulation.mokao_list_title_xpath(i), by='xpath'):
                if BaseMethod.get_text(elem_detail=position_simulation.mokao_list_title_xpath(i), by='xpath') \
                        == "1 自动化使用模考--请勿更改--报名":
                    print('等于的时候i=' + str(i))
                    actual = True
                    my_mokao_status = BaseMethod.get_text(elem_detail=position_simulation.mokao_list_status_xpath(i),
                                                          by='xpath')
                    break
                else:
                    i = i + 1
            elif not BaseMethod.is_exist(elem_detail=position_simulation.mokao_list_title_xpath(i), by='xpath'):
                before_swipe = BaseMethod.get_text(elem_detail=position_simulation.mokao_list_title_xpath(i-1),
                                                   by='xpath')
                BaseMethod.sleep(1)
                BaseMethod.swipe_on(direction='up', t=1000)
                BaseMethod.sleep(1)
                after_swipe = BaseMethod.get_text(elem_detail=position_simulation.mokao_list_title_xpath(i-1),
                                                  by='xpath')
                if before_swipe == after_swipe:
                    actual = False
                    break
                i = 1
        self.assertEqual(actual, True, '我的模考无报名成功的模考')
        self.assertEqual(my_mokao_status, '已报名', '我的模考中模考状态不对')
        BaseMethod.click(position_simulation.iv_back)
        BaseMethod.click(position_simulation.iv_back)

    # 受勋章印象，此用例暂不执行
    '''
    def test_simulation_exam(self):
        position_simulation = PositionMoreSimulationTest()
        BaseMethod.click(position_simulation.tv_left_title)
        BaseMethod.click(position_simulation.rl_mokao)
        BaseMethod.sleep(1)
        i = 1
        while 1:
            if BaseMethod.is_exist(elem_detail=position_simulation.mokao_list_title_xpath(i), by='xpath'):
                if BaseMethod.get_text(elem_detail=position_simulation.mokao_list_title_xpath(i), by='xpath') \
                        == "3 自动化使用模考--请勿更改--模考考试":
                    print('等于的时候i=' + str(i))
                    break
                else:
                    i = i + 1
            elif not BaseMethod.is_exist(elem_detail=position_simulation.mokao_list_title_xpath(i), by='xpath'):
                print('未找到的i='+str(i))
                BaseMethod.sleep(1)
                BaseMethod.swipe_on(direction='up', t=1000)
                BaseMethod.sleep(1)
                i = 1
        status_list = BaseMethod.get_text(elem_detail=position_simulation.mokao_list_status_xpath(i), by='xpath')
        self.assertEqual(status_list, '报名参加', "模考列表页状态：" + status_list + " != 预期模考列表页状态：报名参加")
        time_list = BaseMethod.get_text(elem_detail=position_simulation.mokao_list_time_xpath(i), by='xpath')
        BaseMethod.click(elem_detail=position_simulation.mokao_list_title_xpath(i), by='xpath')
        title_detail = BaseMethod.get_text(elem_detail=position_simulation.tv_title_content)
        self.assertEqual(title_detail, '自动化使用模考--请勿更改--模考考试',
                         "模考详情页标题：" + title_detail + " != 预期模考详情页标题：自动化使用模考--请勿更改--模考考试")
        time_detail = BaseMethod.get_text(elem_detail=position_simulation.tv_time_day)
        self.assertEqual(time_detail, time_list, "模考详情页时间：" + time_detail + " != 模考列表页时间：" + time_list)
        status_detail = BaseMethod.get_text(elem_detail=position_simulation.textConfirm)
        self.assertEqual(status_detail, '立即报名', "模考详情页状态：" + status_detail + " != 预期模考详情页状态：立即报名")
        BaseMethod.click(elem_detail=position_simulation.textConfirm)
        BaseMethod.click(elem_detail=position_simulation.period_xpath(1), by='xpath')
        BaseMethod.click(elem_detail=position_simulation.subject_xpath(1), by='xpath')
        BaseMethod.click(elem_detail=position_simulation.btn_buy_input_message)
        BaseMethod.sleep(1)
        title_after_sign_up = BaseMethod.get_text(elem_detail=position_simulation.tv_titile)
        self.assertEqual(title_after_sign_up, '模考大赛', "报名后顶部标题：" + title_after_sign_up + " != 预期报名后顶部标题：模考大赛")
        exam_title = BaseMethod.get_text(elem_detail=position_simulation.tv_title)
        self.assertEqual(exam_title, '中学综合素质', "试卷标题：" + exam_title + " != 预期试卷标题：中学综合素质")
        exam_status = BaseMethod.get_text(elem_detail=position_simulation.tv_start)
        self.assertEqual(exam_status, '开始考试', "试卷状态：" + exam_status + " != 预期试卷状态：开始考试")
        BaseMethod.click(elem_detail=position_simulation.tv_start)
        BaseMethod.sleep(1)
        BaseMethod.click(elem_detail=position_simulation.iv_guide_mokao)
        used_num = BaseMethod.get_text(elem_detail=position_simulation.tv_usednum)
        self.assertEqual(used_num, '1', '第一道题题号不为1')
        BaseMethod.click(elem_detail=position_simulation.tv_assignment)
        BaseMethod.click(elem_detail=position_simulation.md_buttonDefaultPositive)
        BaseMethod.sleep(1)
        BaseMethod.click(elem_detail=position_simulation.md_buttonDefaultPositive)
        BaseMethod.sleep(2)
        LoginAction.clear_medal()
        title_after_exam = BaseMethod.get_text(elem_detail=position_simulation.tv_titile)
        self.assertEqual(title_after_exam, '成绩单', "答题后顶部标题：" + title_after_exam + " != 预期答题后顶部标题：成绩单")
        BaseMethod.click(position_simulation.iv_back)
        BaseMethod.click(position_simulation.iv_back)
        status_list = BaseMethod.get_text(elem_detail=position_simulation.mokao_list_status_xpath(i), by='xpath')
        self.assertEqual(status_list, '开始考试', "模考列表页状态：" + status_list + " != 预期模考列表页状态：开始考试")
        BaseMethod.click(position_simulation.iv_back)
        BaseMethod.click(PositionMoreSimulationTest.ll_my_mokao)
        BaseMethod.sleep(1)
        i = 1
        my_mokao_status = '无'
        while 1:
            if BaseMethod.is_exist(elem_detail=position_simulation.mokao_list_title_xpath(i), by='xpath'):
                if BaseMethod.get_text(elem_detail=position_simulation.mokao_list_title_xpath(i), by='xpath') \
                        == "3 自动化使用模考--请勿更改--模考考试":
                    print('等于的时候i=' + str(i))
                    actual = True
                    my_mokao_status = BaseMethod.get_text(elem_detail=position_simulation.mokao_list_status_xpath(i),
                                                          by='xpath')
                    break
                else:
                    i = i + 1
            elif not BaseMethod.is_exist(elem_detail=position_simulation.mokao_list_title_xpath(i), by='xpath'):
                before_swipe = BaseMethod.get_text(elem_detail=position_simulation.mokao_list_title_xpath(i - 1),
                                                   by='xpath')
                BaseMethod.sleep(1)
                BaseMethod.swipe_on(direction='up', t=1000)
                BaseMethod.sleep(1)
                after_swipe = BaseMethod.get_text(elem_detail=position_simulation.mokao_list_title_xpath(i - 1),
                                                  by='xpath')
                if before_swipe == after_swipe:
                    actual = False
                    break
                i = 1
        self.assertEqual(actual, True, '我的模考无做答成功的模考')
        self.assertEqual(my_mokao_status, '开始考试', '我的模考中模考状态不对')
        BaseMethod.click(position_simulation.iv_back)
        BaseMethod.click(position_simulation.iv_back)
    '''

    def test_simulation_miss_sign(self):
        position_simulation = PositionMoreSimulationTest()
        BaseMethod.click(position_simulation.tv_left_title)
        BaseMethod.click(position_simulation.rl_mokao)
        BaseMethod.sleep(1)
        i = 1
        while 1:
            if BaseMethod.is_exist(elem_detail=position_simulation.mokao_list_title_xpath(i), by='xpath'):
                if BaseMethod.get_text(elem_detail=position_simulation.mokao_list_title_xpath(i), by='xpath') \
                        == "2 自动化使用模考--请勿更改--未报名":
                    print('等于的时候i=' + str(i))
                    break
                else:
                    i = i + 1
            elif not BaseMethod.is_exist(elem_detail=position_simulation.mokao_list_title_xpath(i), by='xpath'):
                print('未找到的i=' + str(i))
                BaseMethod.sleep(1)
                BaseMethod.swipe_on(direction='up', t=1000)
                BaseMethod.sleep(1)
                i = 1
        status_list = BaseMethod.get_text(elem_detail=position_simulation.mokao_list_status_xpath(i), by='xpath')
        self.assertEqual(status_list, '未报名', "模考列表页状态：" + status_list + " != 预期模考列表页状态：未报名")
        time_list = BaseMethod.get_text(elem_detail=position_simulation.mokao_list_time_xpath(i), by='xpath')
        BaseMethod.click(elem_detail=position_simulation.mokao_list_title_xpath(i), by='xpath')
        title_detail = BaseMethod.get_text(elem_detail=position_simulation.tv_title_content)
        self.assertEqual(title_detail, '自动化使用模考--请勿更改--未报名',
                         "模考详情页标题：" + title_detail + " != 预期模考详情页标题：自动化使用模考--请勿更改--未报名")
        time_detail = BaseMethod.get_text(elem_detail=position_simulation.tv_time_day)
        self.assertEqual(time_detail, time_list, "模考详情页时间：" + time_detail + " != 模考列表页时间：" + time_list)
        status_detail = BaseMethod.get_text(elem_detail=position_simulation.textConfirm)
        self.assertEqual(status_detail, '立即报名', "模考详情页状态：" + status_detail + " != 预期模考详情页状态：立即报名")
        BaseMethod.click(elem_detail=position_simulation.textConfirm)
        BaseMethod.click(elem_detail=position_simulation.one_period_xpath, by='xpath')
        BaseMethod.click(elem_detail=position_simulation.btn_buy_input_message)
        BaseMethod.sleep(1)
        msg = BaseMethod.get_text(elem_detail=position_simulation.md_content)
        self.assertEqual(msg, "很抱歉，本次模考报名时间已经截止，下次早点哦！", "未报名的课程点击报名信息提示错误")
        BaseMethod.click(elem_detail=position_simulation.md_buttonDefaultPositive)
        status_detail = BaseMethod.get_text(elem_detail=position_simulation.textConfirm)
        self.assertEqual(status_detail, '立即报名', "模考详情页状态：" + status_detail + " != 预期模考详情页状态：立即报名")
        BaseMethod.click(elem_detail=position_simulation.iv_back)
        status_list = BaseMethod.get_text(elem_detail=position_simulation.mokao_list_status_xpath(i), by='xpath')
        self.assertEqual(status_list, '未报名', "模考列表页状态：" + status_list + " != 预期模考列表页状态：未报名")
        BaseMethod.click(elem_detail=position_simulation.iv_back)
        BaseMethod.click(PositionMoreSimulationTest.ll_my_mokao)
        BaseMethod.sleep(1)
        i = 1
        while 1:
            if BaseMethod.is_exist(elem_detail=position_simulation.mokao_list_title_xpath(i), by='xpath'):
                if BaseMethod.get_text(elem_detail=position_simulation.mokao_list_title_xpath(i), by='xpath') \
                        == "2 自动化使用模考--请勿更改--未报名":
                    print('等于的时候i=' + str(i))
                    actual = True
                    break
                else:
                    i = i + 1
            elif not BaseMethod.is_exist(elem_detail=position_simulation.mokao_list_title_xpath(i), by='xpath'):
                before_swipe = BaseMethod.get_text(elem_detail=position_simulation.mokao_list_title_xpath(i - 1),
                                                   by='xpath')
                BaseMethod.sleep(1)
                BaseMethod.swipe_on(direction='up', t=1000)
                BaseMethod.sleep(1)
                after_swipe = BaseMethod.get_text(elem_detail=position_simulation.mokao_list_title_xpath(i - 1),
                                                  by='xpath')
                if before_swipe == after_swipe:
                    actual = False
                    break
                i = 1
        self.assertEqual(actual, False, '我的模考有错过报名的模考')
        BaseMethod.click(position_simulation.iv_back)
        BaseMethod.click(position_simulation.iv_back)


if __name__ == '__main__':
    unittest.main()
