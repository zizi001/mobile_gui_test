'''真题练习'''
import re
from danglaoshi.Common import BaseMethod
from danglaoshi.Data.Elements.PositionRealProblemsYears import PositionRealProblemsYears
from danglaoshi.TestAction.Practice_Test import WrongTrainingAction


class RealExerciseAction:

    # 真题练习多选
    def multiple_real_questions(self):
        rea11 = "多项选择题"
        real2 = BaseMethod.get_text(elem_detail=PositionRealProblemsYears.multiplechoices, by="xpath")
        wrong_training = WrongTrainingAction.WrongTrainingAction()
        if rea11 == real2:
            BaseMethod.click(PositionRealProblemsYears.selectb)
            BaseMethod.click(PositionRealProblemsYears.selectd)
        else:
            wrong_training.practice_option_answers()
