# coding:utf-8


# 智能练习

class PositionIntellgentPractice:
    # 练习按钮
    foot_home_button = "com.ruicheng.teacher:id/foot_home"
    # 章节
    practice_chapter_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget." \
                             "FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget." \
                             "RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android." \
                             "view.View/android.support.v7.widget.RecyclerView/android.widget." \
                             "RelativeLayout[1]/android.widget.RelativeLayout"

    # def get_practice_chapter_xpath(self, i):
    #     practice_chapter_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android." \
    #                              "widget.FrameLayout/android.widget.LinearLayout/android.widget." \
    #                              "FrameLayout/android.widget.RelativeLayout/android.widget." \
    #                              "FrameLayout/android.widget.RelativeLayout/android.view.View/android." \
    #                              "support.v7.widget.RecyclerView/android.widget.RelativeLayout["+str(i)+"]/android." \
    #                              "widget.RelativeLayout"
    #     return practice_chapter_xpath
    # 智能练习
    tv_intelligence_training = "com.ruicheng.teacher:id/tv_intelligence_training"
    # 当前题目数
    tv_usednum = "com.ruicheng.teacher:id/tv_usednum"
    # 题目总数,应为15道
    tv_total = "com.ruicheng.teacher:id/tv_total"
    # 题目内容
    tv_body = "com.ruicheng.teacher:id/tv_body"
    # 选项id

    rb_btnA = "com.ruicheng.teacher:id/rb_btnA"
    rb_btnB = "com.ruicheng.teacher:id/rb_btnB"
    rb_btnC = "com.ruicheng.teacher:id/rb_btnC"
    rb_btnD = "com.ruicheng.teacher:id/rb_btnD"
    rb_btn = [rb_btnA, rb_btnB, rb_btnC, rb_btnD]

    # 题目答案id
    question_ans = "com.ruicheng.teacher:id/tv_tittle"
    # 选中选项的XPath

    def get_radio_button_xpath(self, i):
        radio_button_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget." \
                      "FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget." \
                      "RelativeLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android." \
                      "widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget." \
                      "RadioGroup/android.widget.RadioButton["+str(i)+"]"
        return radio_button_xpath
    # 交卷
    tv_assignment = "com.ruicheng.teacher:id/tv_assignment"
    # 收藏 & 收藏按钮
    tv_collection = "com.ruicheng.teacher:id/tv_collection"
    # 答题卡
    tv_answer = "com.ruicheng.teacher:id/tv_answer"
    # 答题卡题目

    def get_tv_answer_button(self, i):
        tv_answer_button = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android." \
                        "widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android." \
                        "widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.GridView/android." \
                        "widget.LinearLayout["+str(i)+"]/android.widget.Button"
        return tv_answer_button
    # 交卷并查看结果按钮
    finish_test_button = "com.ruicheng.teacher:id/finishTest"
    # 确认交卷弹框XPath
    finish_test_bounced = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget." \
                          "FrameLayout/android.view.View"
    # "确定要交卷吗"text
    md_content = "com.ruicheng.teacher:id/md_content"
    # 取消交卷
    md_buttonDefaultNegative = "com.ruicheng.teacher:id/md_buttonDefaultNegative"
    # 确定交卷
    md_buttonDefaultPositive = "com.ruicheng.teacher:id/md_buttonDefaultPositive"
    # 确认交卷后的正确率
    pb_circle_arc_progress_bar = "com.ruicheng.teacher:id/pb_circle_arc_progress_bar"
    # 共15道题,答对x道
    tv_answer_result = "com.ruicheng.teacher:id/tv_answer_result"
    # 交卷后的题目XPath

    def get_tv_answer_resultxpath(self, i):
        tv_answer_resultxpath = "/hierarchy/android.widget.FrameLayout/android.widget." \
                                "LinearLayout/android.widget.FrameLayout/android." \
                                "widget.LinearLayout/android.widget.FrameLayout/android." \
                                "widget.RelativeLayout/android.widget.RelativeLayout[3]/android." \
                                "widget.GridView/android.widget.LinearLayout["+str(i)+"]/android.widget.Button"
        return tv_answer_resultxpath
    # 题目解析
    tv_answer_analysis = "com.ruicheng.teacher:id/tv_answer_analysis"
    # 题目纠错
    tv_problems_error = "com.ruicheng.teacher:id/tv_problems_error"
    # 题目纠错content
    et_content = "com.ruicheng.teacher:id/et_content"
    # 题目纠错提交button
    tv_submit = "com.ruicheng.teacher:id/tv_submit"
    # 错题解析
    tv_analysis = "com.ruicheng.teacher:id/tv_analysis"
    # 全部解析id 与错题解析id 相同
    tv_all_analysis = "com.ruicheng.teacher:id/tv_analysis"
    # 全部解析XPath
    # def get_tv_all_analysisXPath(self, i):
    tv_all_analysisXPath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget." \
                           "FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget." \
                           "LinearLayout/android.widget.LinearLayout[2]/android.widget.TextView[1]"
    # return tv_all_analysisXPath
    # 错题练习总数
    wrong_practice_totalNum = "com.ruicheng.teacher:id/tv_total"

    # 收藏成功吐司

    # 继续练习
    tv_answer_exercise = "com.ruicheng.teacher:id/tv_answer_exercise"
    # 继续练习之后相当于又重新开始一次智能练习

    # 返回按钮
    iv_back_button = "com.ruicheng.teacher:id/iv_back"
    # 页面title "题目纠错"
    tv_titile = "com.ruicheng.teacher:id/tv_titile"






