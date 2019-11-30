# coding:utf-8
class PositionMyCoupons:
    # 我
    user_center = "com.ruicheng.teacher:id/foot_user"
    # 优惠券
    ll_coupon = "com.ruicheng.teacher:id/ll_coupon"
    # 优惠券个数
    tv_coupon_num = "com.ruicheng.teacher:id/tv_conpon_num"
    # 优惠券text xpath
    coupon_text = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget." \
                  "FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget." \
                  "RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android." \
                  "widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android." \
                  "widget.LinearLayout[2]/android.widget.TextView[2]"
    # 优惠券title
    coupon_title = "com.ruicheng.teacher:id/tv_titile"
    # 优惠券返回key
    coupon_back = "com.ruicheng.teacher:id/iv_back"
    # 没有优惠券 空空如也
    no_coupon = "com.ruicheng.teacher:id/textView28"
    # 增加优惠券+
    coupon_add = "com.ruicheng.teacher:id/tv_left_title"
    # 优惠券面额text xpath
    coupon_amount = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget." \
                    "FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android." \
                    "widget.RelativeLayout/android.widget.FrameLayout/android.widget." \
                    "RelativeLayout/android.view.View/android.support.v7.widget.RecyclerView/android." \
                    "widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget." \
                    "RelativeLayout/android.widget.LinearLayout/android.widget.TextView[2]"
    # 优惠券关联课程名称xpath
    coupon_course_name = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget." \
                         "FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget." \
                         "RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android." \
                         "view.View/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android." \
                         "widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView[1]"

    # 优惠券有效期
    coupon_validity = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget." \
                      "FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget." \
                      "RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view." \
                      "View/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android." \
                      "widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView[2]"
    # 一整条优惠券(用来点击然后进入课程)

    def get_whole_coupons(self, i):
        whole_coupon = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget." \
                   "FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget." \
                   "RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view." \
                   "View/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout["+str(i)+"]/android." \
                   "widget.RelativeLayout/android.view.View"
        return whole_coupon, i
    # 吐司 Not Found ??
    # 优惠券关联进入相关课程
