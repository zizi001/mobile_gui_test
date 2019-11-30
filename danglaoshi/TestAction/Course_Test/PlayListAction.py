# 直播列表 & 回放列表
from danglaoshi.Common import BaseMethod
from danglaoshi.Data.Elements import PositionPlayList, PositionCourseList
from danglaoshi.TestAction.Course_Test.CourseListAction import CourseListAction


class PlayListAction:
    def __init__(self):
        self.position_play_list = PositionPlayList.PositionPlayList()
        self.position_course_list = PositionCourseList.PositionCourseList()
        self.course_list_action = CourseListAction()

    def go_in_play_list(self):
        self.course_list_action.change_type_period('教师资格证', '中学')
        BaseMethod.click(self.position_course_list.foot_course)
        BaseMethod.sleep(1)
        if BaseMethod.is_exist(self.position_course_list.i_know):
            BaseMethod.click(self.position_course_list.i_know)
        self.course_list_action.click_course("陕西招教备考指导")
        self.course_list_action.click_course("陕西省教师招聘备考指导-自动化测试专用勿动！")
        BaseMethod.sleep(1)
        BaseMethod.click(elem_detail=self.position_play_list.see_course)
        BaseMethod.sleep(1)

    # 通过 id 获取一组 id 相同的 text ，返回类型为list
    def swipe_get_text(self, ids):
        all_name = []
        while 1:
            num = 0
            while BaseMethod.is_exist(elem_detail=ids, by='ids', i=num):
                name = BaseMethod.get_text(elem_detail=ids, by='ids', i=num)
                if not name in all_name:
                    all_name.append(name)
                num = num+1
            else:
                last_before_swipe = BaseMethod.get_text(elem_detail=ids, by='ids', i=num-1)
                BaseMethod.swipe_on('up', t=1)
                try:
                    last_after_swipe = BaseMethod.get_text(elem_detail=ids, by='ids', i=num-1)
                except Exception as error:
                    print(error)
                    continue
                if last_after_swipe == last_before_swipe:
                    break
                else:
                    continue
        return all_name

    def click_lesson_name(self, lesson_name):
        all_lesson_name = self.swipe_get_text(self.position_play_list.tv_tittle_ids)
        print(all_lesson_name)
        index = all_lesson_name.index(lesson_name)
        BaseMethod.click(elem_detail=self.position_play_list.tv_tittle_ids, by='ids', i=index)

    def click_lesson_attachment(self, lesson_name):
        all_lesson_name = self.swipe_get_text(self.position_play_list.tv_tittle_ids)
        print(all_lesson_name)
        index = all_lesson_name.index(lesson_name)
        BaseMethod.click(elem_detail=self.position_play_list.tvKejian, by='ids', i=index)


