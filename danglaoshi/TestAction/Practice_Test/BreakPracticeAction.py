# -*- coding:utf-8 -*-
'''闯关练习'''
from danglaoshi.Common import BaseMethod, Settings
from danglaoshi.TestAction.PersonalCenter_Test import ExamTypeAction
from danglaoshi.Data.Elements import PositionPracticeBreak, PositionPersonalCenter
from danglaoshi.Common.BaseApi import BaseApi
import json, re
import random


class BreakPracticeAction:
    base_api = BaseApi()

    def __init__(self):
        self.subject_response_data = []
        self.chapter_response_data = None
        self.knowledge_response_data = None
        self.subject_speed = 0
        self.subject_star = 0
        self.chapter_speed = 0
        self.chapter_all = 0
        self.chapter_star = 0

    # 修改当前的学段类型
    def change_type_period(self, exam_type, exam_period):
        BaseMethod.sleep(1)
        BaseMethod.click(PositionPersonalCenter.PositionPersonalCenter.foot_user)
        BaseMethod.sleep(1)
        BaseMethod.click(PositionPersonalCenter.PositionPersonalCenter.tv_testtype)
        BaseMethod.sleep(1)
        ExamTypeAction.exam_type(exam_type, exam_period)
        BaseMethod.click(PositionPersonalCenter.PositionPersonalCenter.foot_home)

    # 顺序获取APP全部科目及对应版本
    def subject_name_version_app(self):
        i = 1
        subject = []
        BaseMethod.sleep(1)
        while 1:
            while BaseMethod.is_exist(PositionPracticeBreak.subject_name_xpath(i), 'xpath'):
                s = [BaseMethod.get_text(PositionPracticeBreak.subject_name_xpath(i), 'xpath'),
                     BaseMethod.get_text(PositionPracticeBreak.subject_version_xpath(i), 'xpath')]
                if s in subject:
                    i = i+1
                else:
                    subject.append(s)
                    i = i+1
            last_before_swipe = BaseMethod.get_text(PositionPracticeBreak.subject_name_xpath(i-1), 'xpath')
            BaseMethod.sleep(1)
            BaseMethod.swipe_on('up', 1000)
            BaseMethod.sleep(1)
            last_after_swipe = BaseMethod.get_text(PositionPracticeBreak.subject_name_xpath(i-1), 'xpath')
            if last_before_swipe == last_after_swipe:
                break
            else:
                i = 2
        return subject

    # 顺序获取APP第subject科目下的章节名称，subject从1开始
    def chapter_name_app(self, subject):
        BaseMethod.click(PositionPracticeBreak.subject_name_xpath(subject), 'xpath')
        i = 1
        chapter = []
        while 1:
            BaseMethod.sleep(1)
            while BaseMethod.is_exist_xpath(PositionPracticeBreak.chapter_name_xpath(i)):
                if BaseMethod.get_text(PositionPracticeBreak.chapter_name_xpath(i), 'xpath') in chapter:
                    i = i+1
                else:
                    # print('***' + str(i) + BaseMethod.get_text(PositionPracticeBreak.chapter_name_xpath(i), 'xpath'))
                    chapter.append(BaseMethod.get_text(PositionPracticeBreak.chapter_name_xpath(i), 'xpath'))
                    i = i+1
            last_before_swipe = BaseMethod.get_text(PositionPracticeBreak.chapter_name_xpath(i-1), 'xpath')
            BaseMethod.sleep(1)
            BaseMethod.swipe_on('up', 1000)
            BaseMethod.sleep(1)
            last_after_swipe = BaseMethod.get_text(PositionPracticeBreak.chapter_name_xpath(i-1), 'xpath')
            if last_after_swipe == last_before_swipe:
                break
            else:
                i = 2
        BaseMethod.click(PositionPracticeBreak.iv_back)
        return chapter

    #  获取APP第subject科目下的第chapter下的知识点，subject和chapter从0开始
    def knowledge_name_app(self, subject, chapter):
        BaseMethod.click(PositionPracticeBreak.subject_name_xpath(subject), 'xpath')
        knowledge_number = BaseMethod.get_text(elem_detail=PositionPracticeBreak.chapter_knowledge_number_xpath(chapter), by='xpath')
        BaseMethod.click(PositionPracticeBreak.chapter_name_xpath(chapter), 'xpath')
        knowledge = []
        i = 1
        # while BaseMethod.is_exist(PositionPracticeBreak.knowledge_point_xpath(i), 'xpath'):
        while i <= int(knowledge_number):
                k = [BaseMethod.get_text(PositionPracticeBreak.knowledge_big),
                     BaseMethod.get_text(PositionPracticeBreak.knowledge_small)]
                knowledge.append(k)
                BaseMethod.sleep(1)
                BaseMethod.swipe_on('left')
                BaseMethod.sleep(1)
                i = i+1
        BaseMethod.click(PositionPracticeBreak.iv_back)
        BaseMethod.click(PositionPracticeBreak.iv_back)
        return knowledge

    # 获取接口返回的科目
    def subject_interface(self):
        headers = Settings.HEADERS
        data = {}
        url = "/breakpoint/listSubject"
        r = self.base_api.post(url, data, headers)
        # print(r.text)
        self.subject_response_data = self.base_api.get_response_data()
        return self.subject_response_data

    # 获取接口第subject科目下的返回章节，subject从0开始
    def chapter_interface(self, subject):
        headers = Settings.HEADERS
        exam_subject_version_id = self.subject_response_data[subject]['examSubjectVersionId']
        subject_id = self.subject_response_data[subject]['examSubjectId']
        data = {
            "examSubjectVersionId": exam_subject_version_id,
            "subjectId": subject_id
        }
        url = "/breakpoint/listChapter"
        r = self.base_api.post(url, data, headers)
        # print(r.text)
        self.chapter_response_data = self.base_api.get_response_data()
        return self.chapter_response_data

    # 获取接口第subject科目下的第chapter下的知识点，subject和chapter从0开始
    def knowledge_interface(self, subject, chapter):
        headers = Settings.HEADERS
        exam_subject_version_id = self.subject_response_data[subject]['examSubjectVersionId']
        subject_id = self.subject_response_data[subject]['examSubjectId']
        exam_chapter_id = self.chapter_response_data['chapters'][chapter]['examChapterId']
        data = {
            "examChapterId": exam_chapter_id,
            "examSubjectVersionId": exam_subject_version_id,
            "subjectId": subject_id
        }
        url = "/breakpoint/listKnowledge"
        r = self.base_api.post(url, data, headers)
        # print(r.text)
        self.knowledge_response_data = self.base_api.get_response_data()
        print(self.knowledge_response_data)
        return self.knowledge_response_data

    # 保存第一个学科第一个章节的闯关进度和星星数（待优化）
    def save_speed_star(self):
        self.change_type_period('教师资格证', '小学')
        self.subject_speed = int(BaseMethod.get_text(elem_detail=PositionPracticeBreak.subject_speed_xapth(1), by='xpath'))
        self.subject_star = int(BaseMethod.get_text(elem_detail=PositionPracticeBreak.subject_star_xapth(1), by='xpath'))
        BaseMethod.click(elem_detail=PositionPracticeBreak.subject_name_xpath(1), by='xpath')
        self.chapter_speed = int(BaseMethod.get_text(elem_detail=PositionPracticeBreak.chapter_speed_xpath(1), by='xpath'))
        self.chapter_all = int(BaseMethod.get_text(elem_detail=PositionPracticeBreak.chapter_knowledge_number_xpath(1), by='xpath'))
        self.chapter_star = int(BaseMethod.get_text(elem_detail=PositionPracticeBreak.chapter_star_xpath(1), by='xpath'))
        BaseMethod.click(PositionPracticeBreak.iv_back)

    # 进入答题界面
    def go_in_practice(self):
        BaseMethod.sleep(1)
        BaseMethod.click(elem_detail=PositionPracticeBreak.subject_name_xpath(1), by='xpath')
        BaseMethod.sleep(1)
        BaseMethod.click(elem_detail=PositionPracticeBreak.chapter_name_xpath(1), by='xpath')
        BaseMethod.sleep(1)
        BaseMethod.click(PositionPracticeBreak.begin_break_practice)
        # if self.chapter_speed < self.chapter_all:
        #     i = self.chapter_speed
        #     while i > 0:
        #         BaseMethod.swipe_on('left', t=600)
        #         i = i-1
        #     BaseMethod.click(PositionPracticeBreak.begin_break_practice)
        # else:
        #     # 后期优化
        #     pass

    # 做答过程（right的true、false表示做答正误）
    def break_practice(self, right):
        title = BaseMethod.get_text(PositionPracticeBreak.tv_tittle)
        regex_str_chinese = ".*?([\u4E00-\u9FA5]+)"
        question_type = ''.join(re.findall(regex_str_chinese, title))
        regex_str_english = ".*?([A-Z]+)"
        answer = ''.join(re.findall(regex_str_english, title))
        if question_type == '单项选择题':
            wrong_options = ['A', 'B', 'C', 'D']
            wrong_options.pop(wrong_options.index(answer))
            wrong_answer = random.sample(wrong_options, 1)[0]
            if right:
                BaseMethod.click(PositionPracticeBreak.option(answer))
            else:
                BaseMethod.click(PositionPracticeBreak.option(wrong_answer))
        elif question_type == '判断题':
            wrong_options = ['A', 'B']
            wrong_options.pop(wrong_options.index(answer))
            wrong_answer = wrong_options[0]
            if right:
                BaseMethod.click(PositionPracticeBreak.option(answer))
            else:
                BaseMethod.click(PositionPracticeBreak.option(wrong_answer))
        elif question_type == '多项选择题':
            wrong_options = ['A', 'B', 'C', 'D']
            wrong_options.pop(wrong_options.index(answer[0]))
            wrong_answer = random.sample(wrong_options, 1)[0]
            if right:
                for ans in answer:
                    BaseMethod.click(PositionPracticeBreak.option(ans))
            else:
                BaseMethod.click(PositionPracticeBreak.option(wrong_answer))
            BaseMethod.click(PositionPracticeBreak.next_questions)

    # 闯关中/结束退回首页
    def back_to_begin(self):
        BaseMethod.click(PositionPracticeBreak.iv_back)
        BaseMethod.click(PositionPracticeBreak.iv_back)
        BaseMethod.click(PositionPracticeBreak.iv_back)

'''
# 顺序获取app的全部科目名称、版本名、以及对应知识点名称
    def all_subject_app(self):
        i = 1
        subject = []
        while BaseMethod.is_exist_xpath(PositionPracticeBreak.subject_name_xpath(i)):
            s = [BaseMethod.get_text_xpath(PositionPracticeBreak.subject_name_xpath(i)),
                 BaseMethod.get_text_xpath(PositionPracticeBreak.subject_version_xpath(i))[:-1]]
            BaseMethod.click_xpath(PositionPracticeBreak.subject_name_xpath(i))
            j = 1
            chapter = {}
            while BaseMethod.is_exist_xpath(PositionPracticeBreak.chapter_name_xpath(j)):
                BaseMethod.click_xpath(PositionPracticeBreak.chapter_name_xpath(j))
                k = 1
                children = {}
                child1 = ""
                knowledge = []
                while BaseMethod.is_exist_xpath(PositionPracticeBreak.knowledge_point_xpath(k)):
                    child2 = BaseMethod.get_text_xpath(PositionPracticeBreak.knowledge_big)
                    know = BaseMethod.get_text_xpath(PositionPracticeBreak.knowledge_small)
                    if child1 == child2:
                        knowledge.append(know)
                        child1 = child2
                    else:
                        children[child1] = knowledge
                        child1 = child2
                        knowledge = []
                    BaseMethod.swipe_left(1000)
                    k = k + 1
                chapter[BaseMethod.get_text_xpath(PositionPracticeBreak.chapter_name_xpath(j))] = children
                BaseMethod.click(PositionPracticeBreak.iv_back)
            s.append(chapter)
            subject.append(s)
            i = i + 1
            BaseMethod.click(PositionPracticeBreak.iv_back)
        return subject

    # 获取数据库的全部 科目名称、版本名称、以及对应知识点名称
    def all_subject_db(self, style, period):
        type_id = 0
        period_id = 0
        if style == "教师资格证":
            type_id = "1"
        elif style == "教师招聘":
            type_id = "2"
        if period == "中学":
            period_id = "1"
        elif period == "小学":
            period_id = "2"
        elif period == "幼儿园":
            period_id = "3"
        DbConnect.db_open()
        sql = "SELECT exam_subject_info.subject_name,exam_version_info.version_name ,exam_subject_struct.exam_node_ids FROM exam_version_info LEFT JOIN exam_subject_version ON exam_version_info.exam_version_id = exam_subject_version.exam_version_id LEFT JOIN exam_subject_info ON exam_subject_version.exam_subject_id = exam_subject_info.exam_subject_id 	LEFT JOIN exam_subject_struct ON exam_subject_version.exam_subject_id = exam_subject_struct.exam_subject_id WHERE exam_subject_version.default_status = 1	AND exam_subject_info.exam_subject_id IN ( SELECT exam_subject_id FROM exam_type_period_subject WHERE exam_type_id = "+type_id+" AND exam_period_id = "+period_id+" )"
        # sql = "SELECT exam_subject_info.subject_name,exam_version_info.version_name FROM exam_version_info	 LEFT JOIN exam_subject_version ON exam_version_info.exam_version_id = exam_subject_version.exam_version_id	 LEFT JOIN exam_subject_info ON exam_subject_version.exam_subject_id = exam_subject_info.exam_subject_id WHERE	exam_subject_version.default_status = 1	AND exam_subject_info.exam_subject_id IN ( SELECT exam_subject_id FROM exam_type_period_subject WHERE exam_type_id = "+type_id+" AND exam_period_id = "+period_id+" ) "
        result = DbConnect.db_select(sql)
        DbConnect.db_close()
        return result

    # 单独解析出数据库中返回的章节、知识点、知识子点的结构
    def analyze_chapter_children_knowledge(self, structs_db):
        structs = json.loads(structs_db)
        chapter = {}
        for chap in range(structs.__len__()):
            children = {}
            if "children" in structs[chap]:
                for child in range(structs[chap]["children"].__len__()):
                    knowledge = []
                    if "knowledge" in structs[chap]["children"][child]:
                        for know in range(structs[chap]["children"][child]["knowledge"].__len__()):
                            knowledge.append(structs[chap]["children"][child]["knowledge"][know]["name"])
                    children[structs[chap]["children"][child]["name"]] = knowledge
            chapter[structs[chap]["name"]] = children
        return chapter
'''
