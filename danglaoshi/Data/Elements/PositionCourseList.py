# 课程列表 & 课程表 & 赠品
class PositionCourseList:
    # 导航--朕知道了
    i_know = "com.ruicheng.teacher:id/iv_guide_2"
    # 课程
    foot_course = "com.ruicheng.teacher:id/foot_course"

    # 课程标题xpath
    def course_name_xpath(self, i):
        course_name = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/' \
                      'android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/' \
                      'android.widget.FrameLayout/android.widget.RelativeLayout/android.view.View[2]/' \
                      'android.support.v7.widget.RecyclerView/android.widget.RelativeLayout['+str(i)+']/' \
                      'android.widget.RelativeLayout/android.widget.TextView[1]'
        return course_name

    # 课程详情文字
    tv_titile = "com.ruicheng.teacher:id/tv_titile"
    # 课程标题ids
    course_name_ids = "com.ruicheng.teacher:id/iv_title"
    # 返回
    iv_back = "com.ruicheng.teacher:id/iv_back"
    # 课程详情--课程表
    rb_course = "com.ruicheng.teacher:id/rb_course"
    # 课程表中的课时名称
    tv_tittle = "com.ruicheng.teacher:id/tv_tittle"
    # 赠品入口
    tv_gift_num = "com.ruicheng.teacher:id/tv_gift_num"

    # 赠品入口处赠品类型
    def gift_type_out_xpath(self, i):
        gift_type_out = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/" \
                        "android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/" \
                        "android.widget.RelativeLayout/android.view.View[2]/android.widget.LinearLayout/" \
                        "android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[3]/" \
                        "android.widget.LinearLayout/android.view.View/" \
                        "android.widget.FrameLayout["+str(i)+"]/android.widget.TextView"
        return gift_type_out
    # 赠品名称
    gift_name ="com.ruicheng.teacher:id/tv_titile_dialog"
    # 赠品类型
    gift_type = "com.ruicheng.teacher:id/tv_status_dialog"
    # 关闭
    iv_close = "com.ruicheng.teacher:id/iv_close"

