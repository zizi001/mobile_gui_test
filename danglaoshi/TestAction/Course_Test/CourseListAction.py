# 课程列表 & 课程表
from danglaoshi.Common import BaseMethod
from danglaoshi.Data.Elements.PositionPersonalCenter import PositionPersonalCenter
from danglaoshi.Data.Elements.PositionCourseList import PositionCourseList
from danglaoshi.TestAction.PersonalCenter_Test import ExamTypeAction


class CourseListAction:
    def __init__(self):
        self.position_course_list = PositionCourseList()

    # 修改当前的学段类型
    def change_type_period(self, exam_type, exam_period):
        BaseMethod.sleep(1)
        BaseMethod.click(elem_detail=PositionPersonalCenter.foot_user)
        BaseMethod.sleep(1)
        BaseMethod.click(elem_detail=PositionPersonalCenter.tv_testtype)
        BaseMethod.sleep(1)
        ExamTypeAction.exam_type(exam_type, exam_period)

    # 判断课程是否存在
    def find_course_xpath(self, course_name):
        i = 1
        BaseMethod.sleep(1)
        while 1:
            if BaseMethod.is_exist(elem_detail=self.position_course_list.course_name_xpath(i), by='xpath'):
                print('+++++++++++++++'+BaseMethod.get_text(elem_detail=self.position_course_list.course_name_xpath(i), by='xpath'))
                if BaseMethod.get_text(elem_detail=self.position_course_list.course_name_xpath(i), by='xpath') \
                        == course_name:
                    return True
                else:
                    i = i+1
            else:
                print('i======'+str(i))
                last_before_swipe = BaseMethod.get_text(elem_detail=self.position_course_list.course_name_xpath(i-1),
                                                        by='xpath')
                BaseMethod.sleep(1)
                BaseMethod.swipe_on('up', t=1000)
                BaseMethod.sleep(1)
                try:
                    last_after_swipe = \
                        BaseMethod.get_text(elem_detail=self.position_course_list.course_name_xpath(i-1), by='xpath')
                except Exception as error:
                    print('***********'+str(error))
                    i = 1
                    continue
                if last_after_swipe == last_before_swipe:
                    return False
                else:
                    i = 1

    # 判断课程是否存在
    def find_course(self, course_name):
        BaseMethod.sleep(1)
        num = 0
        while 1:
            if BaseMethod.is_exist(elem_detail=self.position_course_list.course_name_ids, by='ids', i=num):
                course = BaseMethod.get_text(elem_detail=self.position_course_list.course_name_ids, by='ids', i=num)
                print('+++++++++++++++' + course)
                if course == course_name:
                    return True
                else:
                    num = num+1
            else:
                last_before_swipe = BaseMethod.get_text(elem_detail=self.position_course_list.course_name_ids, by='ids', i=num-1)
                BaseMethod.swipe_on('up', t=1500)
                BaseMethod.sleep(1.5)
                try:
                    last_after_swipe = BaseMethod.get_text(elem_detail=self.position_course_list.course_name_ids,
                                                           by='ids', i=num - 1)
                except Exception as error:
                    print('***********'+str(error))
                    num = 1
                    continue
                if last_after_swipe == last_before_swipe:
                    return False
                else:
                    num = 1

    # 点击进入课程
    def click_course(self, course_name):
        BaseMethod.sleep(1)
        num = 0
        while 1:
            if BaseMethod.is_exist(elem_detail=self.position_course_list.course_name_ids, by='ids', i=num):
                course = BaseMethod.get_text(elem_detail=self.position_course_list.course_name_ids, by='ids', i=num)
                print('+++++++++++++++' + course)
                if course == course_name:
                    BaseMethod.click(elem_detail=self.position_course_list.course_name_ids, by='ids', i=num)
                    return True
                else:
                    num = num + 1
            else:
                last_before_swipe = BaseMethod.get_text(elem_detail=self.position_course_list.course_name_ids, by='ids',
                                                        i=num - 1)
                BaseMethod.swipe_on('up', t=1500)
                BaseMethod.sleep(1.5)
                try:
                    last_after_swipe = BaseMethod.get_text(elem_detail=self.position_course_list.course_name_ids,
                                                           by='ids', i=num - 1)
                except Exception as error:
                    print('***********' + str(error))
                    num = 1
                    continue
                if last_after_swipe == last_before_swipe:
                    return False
                else:
                    num = 1
