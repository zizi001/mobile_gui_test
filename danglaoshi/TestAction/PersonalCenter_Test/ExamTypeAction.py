'''考试类型'''
from danglaoshi.Common import BaseMethod
from danglaoshi.Data.Elements import PositionPersonalCenter


def exam_type(style, period):
    if style == "教师资格证":
        BaseMethod.click_xpath(PositionPersonalCenter.PositionPersonalCenter.teacher_qualification_certificate)
    elif style == "教师招聘":
        BaseMethod.click_xpath(PositionPersonalCenter.PositionPersonalCenter.teacher_recruitment)
    BaseMethod.sleep(1)
    if period == "中学":
        BaseMethod.click_xpath(PositionPersonalCenter.PositionPersonalCenter.middle_school)
    elif period == "小学":
        BaseMethod.click_xpath(PositionPersonalCenter.PositionPersonalCenter.primary_school)
    elif period == "幼儿园":
        BaseMethod.click_xpath(PositionPersonalCenter.PositionPersonalCenter.kindergarten)
    BaseMethod.sleep(1)


