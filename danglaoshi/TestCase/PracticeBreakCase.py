from danglaoshi.Common import BaseMethod
import unittest
from danglaoshi.TestAction.Login_Test import LoginAction
from danglaoshi.TestAction.Practice_Test.BreakPracticeAction import BreakPracticeAction
from ddt import ddt, data, unpack
from danglaoshi.Data.Elements import PositionPracticeBreak
import json


@ddt
class PracticeBreakCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        BaseMethod.driver_open(True)
        LoginAction.login("13100000993", "123456")
        LoginAction.after_login()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        LoginAction.login_out()
        BaseMethod.driver_close()

    @data(("教师资格证", "中学"), ("教师资格证", "小学"), ("教师资格证", "幼儿园"),
          ("教师招聘", "中学"), ("教师招聘", "小学"), ("教师招聘", "幼儿园"))
    @unpack
    def test_exam_subject_version(self, style, period):
        break_practice_action = BreakPracticeAction()
        break_practice_action.change_type_period(style, period)
        # subject_app = BreakPracticeAction.all_subject_app()
        # subject_db = BreakPracticeAction.all_subject_db(style, period)
        # print(subject_app)
        # print(subject_db)
        # assert (subject_db.__len__() == subject_app.__len__())
        # subject_db_list = []
        # for subject in subject_db:
        #     sub = subject[0][1]
        #     subject_db_list.append(list(sub))
        # num = 0
        # for a in subject_app:
        #     for b in subject_db_list:
        #         if a == b:
        #             num = num + 1
        subject_app = break_practice_action.subject_name_version_app()
        subject_response = break_practice_action.subject_interface()
        subject_interface = []
        if subject_response:
            for sub in subject_response:
                subject_interface.append([sub['subjectName'], sub['versionName']+'版'])
        print(subject_app)
        print(subject_interface)
        assert (subject_app.__len__() == subject_interface.__len__())
        assert (subject_app == subject_interface)

    @data(("教师资格证", "中学"), ("教师资格证", "小学"), ("教师资格证", "幼儿园"),
          ("教师招聘", "中学"), ("教师招聘", "小学"), ("教师招聘", "幼儿园"))
    @unpack
    def test_chapter(self, style, period):
        break_practice_action = BreakPracticeAction()
        break_practice_action.change_type_period(style, period)
        subject_response = break_practice_action.subject_interface()
        subject_number = subject_response.__len__()
        # 由于界面大小限制，仅校验前四个，subject_number
        i = 0
        while i < 4:
            chapter_response = break_practice_action.chapter_interface(i)['chapters']
            chapter_interface = []
            for chap in chapter_response:
                chapter_interface.append(chap['chapterName'])
            chapter_app = break_practice_action.chapter_name_app(i+1)
            print('chapter' + str(chapter_interface))
            print('chapter_app' + str(chapter_app))
            assert (chapter_interface == chapter_app)
            i = i+1

    @data(("教师资格证", "中学"), ("教师资格证", "小学"), ("教师资格证", "幼儿园"),
          ("教师招聘", "中学"), ("教师招聘", "小学"), ("教师招聘", "幼儿园"))
    @unpack
    def test_exam_subject_version(self, style, period):
        break_practice_action = BreakPracticeAction()
        break_practice_action.change_type_period(style, period)
        subject_response = break_practice_action.subject_interface()
        subject_number = subject_response.__len__()
        # 由于界面大小限制，仅校验前四个，subject_number
        if subject_number <= 4:
            max1 = subject_number
        else:
            max1 = 4
        i = 0
        while i < max1:
            chapter_response = break_practice_action.chapter_interface(i)['chapters']
            chapter_number = chapter_response.__len__()
            # 由于界面大小限制，仅校验前七个，而不是chapter_number
            if chapter_number <= 7:
                max2 = chapter_number
            else:
                max2 = 7
            j = 0
            while j < max2:
                knowledge_response = break_practice_action.knowledge_interface(i, j)['knowledge']
                knowledge_interface = []
                for know in knowledge_response:
                    knowledge_interface.append([know['subChapterName'], know['knowledgeName']])
                knowledge_app = break_practice_action.knowledge_name_app(i+1, j+1)
                print('knowledge_interface:' + str(knowledge_interface))
                print('knowledge_app:' + str(knowledge_app))
                assert (knowledge_interface == knowledge_app)
                j = j+1
            i = i+1

    @data(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
    # @unpack
    def test_break_exam(self, right_number):
        BaseMethod.to_activity(".Activity.MainActivity")
        break_practice_action = BreakPracticeAction()
        break_practice_action.save_speed_star()
        break_practice_action.go_in_practice()
        current_right_num_expect = 0
        for i in range(15):
            current_num = int(BaseMethod.get_text(PositionPracticeBreak.tv_usednum))
            current_right_num = BaseMethod.get_text(PositionPracticeBreak.tv_main_title)
            print("current_right_num_expect:" + ("已答对：" + str(current_right_num_expect)))
            print("current_right_num:" + str(current_right_num))
            assert (("已答对：" + str(current_right_num_expect)) == current_right_num)
            print("current_num_expect:" + str(i+1))
            print("current_num:" + str(current_num))
            assert (current_num == (i+1))
            if i < right_number:
                break_practice_action.break_practice(True)
                current_right_num_expect = current_right_num_expect + 1
            else:
                break_practice_action.break_practice(False)
            BaseMethod.sleep(1)
        LoginAction.clear_medal()
        result_expect = "共15题，答对" + str(right_number) + "题，正确率" + str(int(round(right_number/15, 2) * 100)) + "%"
        result_app = BaseMethod.get_text(PositionPracticeBreak.tv_result)
        print("result_expect:"+result_expect)
        print("result_app:"+result_app)
        assert (result_app == result_expect)
        break_practice_action.back_to_begin()


if __name__ == '__main__':
    unittest.main()
