# -*- coding:utf-8 -*-
'''错题解析'''
from danglaoshi.Common import BaseMethod
from danglaoshi.Data.Elements.PositionAnalysis import PositionAnalysis
from danglaoshi.TestAction.Practice_Test.IntelligentPracticeAction import IntelligentPracticeAction
import re

# 获取错题数目
def number_wrong_questions():
    string_n = BaseMethod.get_text(elem_detail=PositionAnalysis.statement_settlement, by='id')
    err_n = string_n[7:9]
    if not err_n.isdigit():
        err_n = string_n[7:8]
    num = int(err_n)
    return num

# 闯关判断单选多选题
def multiple_choice_questions():
    intelli_gent = IntelligentPracticeAction()
    mult1 = "多项选择题([A,B,C,D])"
    regex_str_chinese = ".*?([\u4E00-\u9FA5]+)"
    mult2 = re.match(regex_str_chinese, mult1)
    print(mult2.group(1))
    if BaseMethod.is_exist(elem_detail="com.ruicheng.teacher:id/tv_tittle", by="id") == mult2.group(1):
        intelli_gent.practice_option_answers()
        BaseMethod.click(PositionAnalysis.next_questions, by="xpath")
    else:
        intelli_gent.practice_option_answers()



