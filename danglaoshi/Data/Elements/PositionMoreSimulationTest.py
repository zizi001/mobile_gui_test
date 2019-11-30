# coding:utf-8
class PositionMoreSimulationTest:
    # 更多
    tv_left_title = "com.ruicheng.teacher:id/tv_left_title"
    # 模考大赛
    rl_mokao = "com.ruicheng.teacher:id/rl_mokao"
    # 我的模考
    ll_my_mokao = "com.ruicheng.teacher:id/ll_my_mokao"

    # 模考列表标题
    def mokao_list_title_xpath(self, i):
        mokao_title = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/" \
                      "android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/" \
                      "android.view.View/android.support.v7.widget.RecyclerView/" \
                      "android.widget.RelativeLayout["+str(i)+"]/" \
                      "android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[1]"
        return mokao_title

    # 模考列表时间
    def mokao_list_time_xpath(self, i):
        mokao_time = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/" \
                    "android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/" \
                    "android.view.View/android.support.v7.widget.RecyclerView/" \
                    "android.widget.RelativeLayout[" + str(i) + "]/" \
                    "android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[2]"
        return mokao_time

    # 模考列表状态
    def mokao_list_status_xpath(self, i):
        mokao_status = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/" \
                      "android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/" \
                      "android.view.View/android.support.v7.widget.RecyclerView/" \
                      "android.widget.RelativeLayout[" + str(i) + "]/" \
                      "android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[3]"
        return mokao_status

    # 模考详情页题目（内容中的）
    tv_title_content = "com.ruicheng.teacher:id/tv_title_content"
    # 模考详情页时间
    tv_time_day = "com.ruicheng.teacher:id/tv_time_day"
    # 模考详情页状态
    textConfirm = "com.ruicheng.teacher:id/textConfirm"

    # 学段
    def period_xpath(self, i):
        period = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/" \
                 "android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/" \
                 "android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/" \
                 "android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/" \
                 "android.view.View/android.widget.FrameLayout["+str(i)+"]/android.widget.TextView"
        return period
    # 单学段
    one_period_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/" \
                       "android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/" \
                       "android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/" \
                       "android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/" \
                       "android.view.View/android.widget.FrameLayout/android.widget.TextView"
    # 科目
    def subject_xpath(self, i):
        subject = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/" \
                 "android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/" \
                 "android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/" \
                 "android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/" \
                 "android.view.View/android.widget.FrameLayout["+str(i)+"]/android.widget.TextView"
        return subject

    # 学段类型选择确定
    btn_buy_input_message = "com.ruicheng.teacher:id/btn_buy_input_message"
    # 报完成功后页面头部
    tv_titile = "com.ruicheng.teacher:id/tv_titile"
    # 试卷标题
    tv_title = "com.ruicheng.teacher:id/tv_title"
    # 试卷状态
    tv_start = "com.ruicheng.teacher:id/tv_start"
    # 返回
    iv_back = "com.ruicheng.teacher:id/iv_back"
    # 模考引导
    iv_guide_mokao = "com.ruicheng.teacher:id/iv_guide_mokao"
    # 当前题号
    tv_usednum = "com.ruicheng.teacher:id/tv_usednum"
    # 选项A
    rb_btnA = "com.ruicheng.teacher:id/rb_btnA"
    # 交卷
    tv_assignment = "com.ruicheng.teacher:id/tv_assignment"
    # 确定交卷 & 查看成绩
    md_buttonDefaultPositive = "com.ruicheng.teacher:id/md_buttonDefaultPositive"
    # 消息提示
    md_content = "com.ruicheng.teacher:id/md_content"

