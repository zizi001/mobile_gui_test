# coding:utf-8


class PositionTeacherEvaluation:
    # 课程
    foot_course = "com.ruicheng.teacher:id/foot_course"
    # 进入课程详情(直接根据text"我是一节蜂蜜课程"去定位该课程里面的教师评价)
    teacher_evaluation_course_details = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android." \
                                        "widget.FrameLayout/android.widget.LinearLayout/android.widget." \
                                        "FrameLayout/android.widget.RelativeLayout/android.widget." \
                                        "FrameLayout/android.widget.RelativeLayout/android.view.View[2]/android." \
                                        "support.v7.widget.RecyclerView/android.widget.RelativeLayout[3]/android." \
                                        "widget.RelativeLayout/android.widget.TextView[1]"
    # 老师简介
    teacher_introduction = "com.ruicheng.teacher:id/rb_teacher"
    # 全部评价

    def get_all_evaluation(self, i):
        all_evaluation = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget." \
                     "FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget." \
                     "RelativeLayout/android.view.View[2]/android.widget.FrameLayout/android.widget." \
                     "LinearLayout/android.widget.ListView/android.widget.RelativeLayout["+str(i)+"]/android." \
                     "widget.RelativeLayout/android.widget.RelativeLayout/android.widget.TextView[2]"
        return all_evaluation
    # 评分 3.9
    teacher_evaluation_score = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android." \
                               "widget.FrameLayout/android.widget.LinearLayout/android.widget." \
                               "FrameLayout/android.widget.RelativeLayout/android.widget." \
                               "LinearLayout/android.widget.RelativeLayout[1]/android.widget." \
                               "RelativeLayout/android.widget.TextView"
    # 教师名称
    teacher_name = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android." \
                   "widget.FrameLayout/android.widget.LinearLayout/android.widget." \
                   "FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android." \
                   "widget.RelativeLayout[1]/android.widget.TextView[1]"
    # 教师简介
    teacher_profile = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android." \
                      "widget.FrameLayout/android.widget.LinearLayout/android.widget." \
                      "FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android." \
                      "widget.RelativeLayout[1]/android.widget.TextView[2]"
    # 教师评价信息
    teacher_evaluation_content = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android." \
                                 "widget.FrameLayout/android.widget.LinearLayout/android.widget." \
                                 "FrameLayout/android.widget.RelativeLayout/android.widget." \
                                 "LinearLayout/android.widget.RelativeLayout[1]/android.widget.TextView[3]"
    # 教师评价title
    teacher_evaluation_title = "com.ruicheng.teacher:id/tv_titile"
    # 教师评价back key
    teacher_evaluation_back = "com.ruicheng.teacher:id/iv_back"
    # 历史评价
    teacher_historical_evaluation = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android." \
                                    "widget.FrameLayout/android.widget.LinearLayout/android.widget." \
                                    "FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android." \
                                    "widget.RelativeLayout[2]/android.widget.TextView[1]"
    # XX条评论
    comments_number = "com.ruicheng.teacher:id/tv_comments_num"
    # 用户评论内容
    user_evaluation_content = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android." \
                              "widget.FrameLayout/android.widget.LinearLayout/android.widget." \
                              "FrameLayout/android.widget.RelativeLayout/android.widget." \
                              "LinearLayout/android.view.View/android.support.v7.widget." \
                              "RecyclerView/android.widget.LinearLayout[1]/android.widget." \
                              "LinearLayout/android.widget.TextView"
    # 评价用户
    evaluation_user = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android." \
                      "widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android." \
                      "widget.RelativeLayout/android.widget.LinearLayout/android.view.View/android." \
                      "support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android." \
                      "widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[1]"
    # 用户个人评价星星
    user_evaluation_star = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android." \
                           "widget.FrameLayout/android.widget.LinearLayout/android.widget." \
                           "FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android." \
                           "view.View/android.support.v7.widget.RecyclerView/android.widget." \
                           "LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.view.View"
    # 用户评价时间
    user_evaluation_time = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget." \
                           "FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android." \
                           "widget.RelativeLayout/android.widget.LinearLayout/android.view.View/android." \
                           "support.v7.widget.RecyclerView/android." \
                           "widget.LinearLayout[1]/android.widget.LinearLayout/android." \
                           "widget.LinearLayout/android.widget.TextView[2]"






