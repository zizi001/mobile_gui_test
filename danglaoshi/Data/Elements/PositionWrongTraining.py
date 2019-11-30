# coding:utf-8


class PositionWrongTraining:
    # 错题练习
    tv_wrong_training = "com.ruicheng.teacher:id/tv_wrong_training"
    # 错题练习title text
    tv_titile = "com.ruicheng.teacher:id/tv_titile"
    # 用户没有错题练习记录
    no_practice_record = "com.ruicheng.teacher:id/erro_bg"
    # 错题练习列表XPath

    def wrong_training_chapter_xpath(self, i):
        wrong_chapter_name = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget." \
                             "FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget." \
                             "RelativeLayout/android.widget.ExpandableListView/android.widget." \
                             "RelativeLayout["+str(i)+"]/android.widget.RelativeLayout"
        return wrong_chapter_name

    def wrong_training_sections_xpath(self, i):
        wrong_sections_name = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android." \
                              "widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android." \
                              "widget.RelativeLayout/android.widget.ExpandableListView/android.widget." \
                              "RelativeLayout["+str(i)+"]/android.widget.RelativeLayout/android.widget.TextView[1]"
        return wrong_sections_name

    # 错题列表错题总数XPath(通过text去定位具体)
    tv_wrong_training_totalNumXPath = "/hierarchy/android.widget.FrameLayout/android." \
                                      "widget.LinearLayout/android.widget.FrameLayout/android." \
                                      "widget.LinearLayout/android.widget.FrameLayout/android." \
                                      "widget.RelativeLayout/android.widget.ExpandableListView/android.widget." \
                                      "RelativeLayout[2]/android.widget.RelativeLayout/android.widget.TextView[2]"
    # 展开错题章节按钮XPath
    Open_the_wrong_sectionButton = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android." \
                                   "widget.FrameLayout/android.widget.LinearLayout/android.widget." \
                                   "FrameLayout/android.widget.RelativeLayout/android.widget." \
                                   "ExpandableListView/android.widget.RelativeLayout[1]/android.widget." \
                                   "RelativeLayout/android.widget.ImageView"
    # 展开章节之后的小章节text XPath
    wrong_small_chapterXpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget." \
                               "FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android." \
                               "widget.RelativeLayout/android.widget.ExpandableListView/android.widget." \
                               "RelativeLayout[2]/android.widget.RelativeLayout/android.widget.TextView[1]"
    # 展开章节之后的各小章节错题总数 XPath
    tv_wrongsmallchapter_totalNumXPath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android." \
                                         "widget.FrameLayout/android.widget.LinearLayout/android.widget." \
                                         "FrameLayout/android.widget.RelativeLayout/android.widget." \
                                         "ExpandableListView/android.widget.RelativeLayout[2]/android." \
                                         "widget.RelativeLayout/android.widget.TextView[2]"
    # 错题练习中的收藏
    wrong_training_ll_add = "com.ruicheng.teacher:id/ll_add"
    # 收藏文字
    wrong_training_tv_add = "com.ruicheng.teacher:id/tv_add"
    # 移除收藏的题目
    wrong_training_ll_remove = "com.ruicheng.teacher:id/ll_remove"

    # 返回按钮
    iv_back_button = "com.ruicheng.teacher:id/iv_back"
