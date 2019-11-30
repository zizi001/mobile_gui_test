# coding:utf-8
class PositionMyCourse:
    # 课程
    foot_course = "com.ruicheng.teacher:id/foot_course"
    # 我的课程
    my_course = "com.ruicheng.teacher:id/rl_myCourse"
    # 我的课程数量
    my_course_num = "com.ruicheng.teacher:id/tv_num"
    # 我的课程小箭头
    imageUser = "com.ruicheng.teacher:id/imageUser"
    # ================引导页=================
    # 外面引导语
    my_course_guide = "com.ruicheng.teacher:id/iv_guide_2"
    # 里面引导语
    course_guide = "com.ruicheng.teacher:id/iv_guide"
    # 我的课程title
    my_course_title = "com.ruicheng.teacher:id/tv_titile"
    # 我的课程back key
    my_course_back = "com.ruicheng.teacher:id/iv_back"
    # 课程日历
    my_course_calendar = "com.ruicheng.teacher:id/tv_left_title"
    #
    # 我的课程整条

    def get_my_course_whole(self, i):
        my_course_whole = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget." \
                      "FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget." \
                      "RelativeLayout/android.view.View[2]/android.support.v7.widget.RecyclerView/android.widget." \
                      "LinearLayout["+str(i)+"]/android.view.View/android.widget.RelativeLayout/android." \
                                             "widget.RelativeLayout"
        return my_course_whole
    # 课程名称
    my_course_name = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget." \
                     "FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget." \
                     "RelativeLayout/android.view.View[2]/android.support.v7.widget.RecyclerView/android.widget." \
                     "LinearLayout[1]/android.view.View/android.widget.RelativeLayout/android.widget." \
                     "RelativeLayout/android.widget.TextView"
    # 课程img
    my_course_img = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget." \
                    "FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget." \
                    "RelativeLayout/android.view.View[2]/android.support.v7.widget.RecyclerView/android." \
                    "widget.LinearLayout[1]/android.view.View/android.widget.RelativeLayout/android." \
                    "widget.RelativeLayout/android.widget.ImageView"
    # 课程置顶状态
    my_course_top_state = "com.ruicheng.teacher:id/tv_tag1"
    # 课程直播状态
    my_course_live_on_state = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget." \
                              "FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget." \
                              "RelativeLayout/android.view.View[2]/android.support.v7.widget.RecyclerView/android." \
                              "widget.LinearLayout[2]/android.view.View/android.widget.RelativeLayout/android.widget." \
                              "RelativeLayout/android.widget.TextView[2]"
    # 进度条
    my_course_progress_bar = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget." \
                             "FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget." \
                             "RelativeLayout/android.view.View[2]/android.support.v7.widget.RecyclerView/android." \
                             "widget.LinearLayout[2]/android.view.View/android.widget.RelativeLayout/android.widget." \
                             "RelativeLayout/android.widget.ProgressBar"
    # 回放过期时间
    my_course_playback_expiration_time = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android." \
                                         "widget.FrameLayout/android.widget.LinearLayout/android.widget." \
                                         "FrameLayout/android.widget.RelativeLayout/android.view.View[2]/android." \
                                         "support.v7.widget.RecyclerView/android.widget.LinearLayout[6]/android.view." \
                                         "View/android.widget.RelativeLayout/android.widget.RelativeLayout/android." \
                                         "widget.TextView[3]"
    # 置顶
    my_course_top = "com.ruicheng.teacher:id/tv_top"
    # 删除
    my_course_delete = "com.ruicheng.teacher:id/tv_delete"
    # 取消置顶
    my_course_cancel_top = "com.ruicheng.teacher:id/tv_top"
    # 不能删除的课程
    "com.ruicheng.teacher:id/tv_delete"
    # 线上课/线下课
    # 按钮颜色
    # 已过期课程
    my_course_expired = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget." \
                        "FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget." \
                        "RelativeLayout/android.view.View[2]/android.support.v7.widget.RecyclerView/android." \
                        "widget.LinearLayout[1]/android.view.View/android.widget.RelativeLayout/android.widget." \
                        "RelativeLayout[1]/android.widget.ImageView"
