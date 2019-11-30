# coding:utf-8


class PositionTryToLearn:
    # 课程
    foot_course = "com.ruicheng.teacher:id/foot_course"
    # 外面引导语
    my_course_guide = "com.ruicheng.teacher:id/iv_guide_2"
    # 测试试听课程
    try_to_learn_course = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget." \
                          "FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget." \
                          "RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android." \
                          "view.View[2]/android.support.v7.widget.RecyclerView/android.widget." \
                          "RelativeLayout[3]/android.widget.RelativeLayout"
    # "点击试学"按钮
    try_to_learn_button = "com.ruicheng.teacher:id/ll_course_listener"
    # 请选择试学内容
    try_to_learn_content_title = "com.ruicheng.teacher:id/ll_course_listener_title"
    # 试学播放按钮
    # try_to_learn_play_button = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget." \
    #                            "FrameLayout/android.widget.RelativeLayout/android.support.v7.widget." \
    #                            "RecyclerView/android.widget.RelativeLayout[1]/android.widget." \
    #                            "RelativeLayout/android." \
    #                            "widget.ImageView"
    # 试学播放按钮

    def try_to_learn_play_button_xpath(self, i):
        try_to_learn_play_button = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android." \
                                   "widget.FrameLayout/android.widget.RelativeLayout/android.support.v7." \
                                   "widget.RecyclerView/android.widget.RelativeLayout["+str(i)+"]/android.widget." \
                                  "RelativeLayout/android.widget.ImageView"
        return try_to_learn_play_button
    # 试学list

    def get_try_to_learn_list(self, i):
        try_to_learn_list = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget." \
                            "FrameLayout/android.widget.RelativeLayout/android.support.v7.widget." \
                            "RecyclerView/android.widget.RelativeLayout["+str(i)+"]/android.widget.RelativeLayout"
        return try_to_learn_list

    # 选择试学内容前面/
    try_to_learn_img = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget." \
                       "FrameLayout/android.widget.RelativeLayout/android.widget." \
                       "LinearLayout/android.widget.ImageView"
    # 试学返回back
    try_to_learn_back = "com.ruicheng.teacher:id/iv_back"
    # 试学播放rate
    try_to_learn_send = "com.ruicheng.teacher:id/dialog_message_send_et"
