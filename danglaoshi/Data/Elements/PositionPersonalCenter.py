# coding:utf-8
'''个人中心'''


class PositionPersonalCenter:
    # 教师资格证xpath
    teacher_qualification_certificate = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/" \
                                        "android.widget.FrameLayout/android.widget.LinearLayout/" \
                                        "android.widget.FrameLayout/android.widget.RelativeLayout/" \
                                        "android.widget.LinearLayout[2]/android.support.v7.widget.RecyclerView/" \
                                        "android.widget.RelativeLayout[1]/android.widget.RelativeLayout/" \
                                        "android.widget.RelativeLayout/android.widget.TextView[1]"
    # 教师招聘xpath
    teacher_recruitment = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/" \
                          "android.widget.FrameLayout/android.widget.LinearLayout/" \
                          "android.widget.FrameLayout/android.widget.RelativeLayout/" \
                          "android.widget.LinearLayout[2]/android.support.v7.widget.RecyclerView/" \
                          "android.widget.RelativeLayout[2]/android.widget.RelativeLayout/" \
                          "android.widget.RelativeLayout/android.widget.TextView[1]"
    # 中学xpath
    middle_school = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/" \
                    "android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/" \
                    "android.widget.LinearLayout[2]/android.support.v7.widget.RecyclerView/" \
                    "android.widget.RelativeLayout[1]/android.widget.RelativeLayout/" \
                    "android.widget.RelativeLayout/android.widget.TextView"
    # 小学xpath
    primary_school = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/" \
                     "android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/" \
                     "android.widget.LinearLayout[2]/android.support.v7.widget.RecyclerView/" \
                     "android.widget.RelativeLayout[2]/android.widget.RelativeLayout/" \
                     "android.widget.RelativeLayout/android.widget.TextView"
    # 幼儿园xpath
    kindergarten = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/" \
                   "android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/" \
                   "android.widget.LinearLayout[2]/android.support.v7.widget.RecyclerView/" \
                   "android.widget.RelativeLayout[3]/android.widget.RelativeLayout/" \
                   "android.widget.RelativeLayout/android.widget.TextView"
    # 我
    foot_user = "com.ruicheng.teacher:id/foot_user"
    # sessionId和userId保存
    header = "com.ruicheng.teacher:id/tv_id"
    # 学段类型
    tv_testtype = "com.ruicheng.teacher:id/tv_testtype"
    # 签到确认（两个按键同名）
    tv_i_know = "com.ruicheng.teacher:id/tv_i_know"
    #勋章关闭
    rl_close = 'com.ruicheng.teacher:id/rl_close'
    # 赠课确认
    tv_btn = "com.ruicheng.teacher:id/tv_btn"
    # 练习
    foot_home = "com.ruicheng.teacher:id/foot_home"
    # 弹窗关闭
    iv_close1 = "com.ruicheng.teacher:id/iv_close1"


