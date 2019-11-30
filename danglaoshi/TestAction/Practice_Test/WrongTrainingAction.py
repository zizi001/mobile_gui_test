from danglaoshi.Common import BaseMethod
from danglaoshi.Data.Elements import PositionWrongTraining
from danglaoshi.Data.Elements import PositionIntellgentPractice
# import time
import random
from danglaoshi.TestAction.Login_Test import LoginAction


class WrongTrainingAction:
    # APP中错题练习
    def enter_wrong_practice(self):
        BaseMethod.click(PositionIntellgentPractice.PositionIntellgentPractice.foot_home_button)
        print("=====22222=====")
        BaseMethod.click_xpath(PositionIntellgentPractice.PositionIntellgentPractice.practice_chapter_xpath)
        BaseMethod.click(PositionWrongTraining.PositionWrongTraining.tv_wrong_training)
        print("=====进入错题练习=====")

    def get_wrong_chapters(self):
        pass

    # APP中智能练习
    def practice_option_answers(self):
        # time.sleep(1)
        options = ["com.ruicheng.teacher:id/rb_btnA",
                   "com.ruicheng.teacher:id/rb_btnB",
                   "com.ruicheng.teacher:id/rb_btnC",
                   "com.ruicheng.teacher:id/rb_btnD"]
        option = random.sample(options, 1)[0]
        print("我选"+option[30])
        BaseMethod.click("".join(option))
        print("3333333333333")

    def app_intellgent_practice(self, i):

        BaseMethod.click(PositionIntellgentPractice.PositionIntellgentPractice.foot_home_button)
        print("=====1111=====")
        BaseMethod.click_xpath(PositionIntellgentPractice.PositionIntellgentPractice.practice_chapter_xpath)
        BaseMethod.click(PositionIntellgentPractice.PositionIntellgentPractice.tv_intelligence_training)
        print("==========")
        count = 0
        while count <= i:
            print("我是第" + str(count+1) + "道题")
            self.practice_option_answers()
            BaseMethod.swipe_left(300)
            count += 1
            self.get_question_answer()
        else:
            print("滴滴滴,报警啦")


    # 获取题目答案
    def get_question_answer(self):
        answer_text = BaseMethod.get_text(PositionIntellgentPractice.PositionIntellgentPractice.question_ans)
        # 单项选择题(B)
        correct_answers = []
        if "A" in answer_text:
            correct_answers.append("A")
        elif "B" in answer_text:
            correct_answers.append("B")
        elif "C" in answer_text:
            correct_answers.append("C")
        elif "D" in answer_text:
            correct_answers.append("D")
        print("我是正确答案"+"".join(correct_answers))
        return "".join(correct_answers)

    # 正常练习流程
    def Practice_process(self):
        #intellgent_practice_ready()
        option_text = BaseMethod.get_text(PositionIntellgentPractice.PositionIntellgentPractice.rb_btn)
        print("我就是选项")
        options = []
        if "rb_btnA" in option_text:
            options.append(BaseMethod.get_text(PositionIntellgentPractice.PositionIntellgentPractice.rb_btn))
        elif "rb_btnB" in option_text:
            options.append(BaseMethod.get_text(PositionIntellgentPractice.PositionIntellgentPractice.rb_btn))
        elif "rb_btnC" in option_text:
            options.append(BaseMethod.get_text(PositionIntellgentPractice.PositionIntellgentPractice.rb_btn))
        elif "rb_btnD" in option_text:
            options.append(BaseMethod.get_text(PositionIntellgentPractice.PositionIntellgentPractice.rb_btn))
        print("我是选项"+"".join(options))
        BaseMethod.click(PositionIntellgentPractice.PositionIntellgentPractice.rb_btn)
        return options


if __name__ == '__main__':
    BaseMethod.driver_open(True)
    LoginAction.login_out()
    LoginAction.login("15769270635", "123456")
    LoginAction.after_login()

    BaseMethod.driver_close()










