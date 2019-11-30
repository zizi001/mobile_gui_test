# coding:utf-8
class PositionSetting:
    # 我
    user_center = "com.ruicheng.teacher:id/foot_user"
    # 设置
    ll_setting = "com.ruicheng.teacher:id/ll_setting"
    # 设置title
    setting_title = "com.ruicheng.teacher:id/tv_titile"
    # 设置back
    setting_back = "com.ruicheng.teacher:id/iv_back"
    # 版本更新
    rl_version_update = "com.ruicheng.teacher:id/rl_version_update"
    # 意见反馈
    rl_feedback = "com.ruicheng.teacher:id/rl_feedback"
    # 意见反馈title
    feedback_title = "com.ruicheng.teacher:id/tv_titile"
    # 意见反馈back
    feedback_back = "com.ruicheng.teacher:id/iv_back"
    # 意见反馈内容
    feedback_content = "com.ruicheng.teacher:id/et_content"
    # 意见反馈提交button
    feedback_submit = "com.ruicheng.teacher:id/submmit"
    # 意见反馈提交之后弹框text
    after_submit = "com.ruicheng.teacher:id/md_content"
    # 确定
    md_buttonDefaultPositive = "com.ruicheng.teacher:id/md_buttonDefaultPositive"
    # 取消
    md_buttonDefaultNegative = "com.ruicheng.teacher:id/md_buttonDefaultNegative"
    # 关于我们
    rl_about_us = "com.ruicheng.teacher:id/rl_abouting"
    # 关于我们back
    about_us_back = "com.ruicheng.teacher:id/iv_back"
    # logo

    def get_danglaoshi_logo(self, i):
        danglaoshi_logo = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget." \
                      "FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget." \
                      "RelativeLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout["+str(i)+"]/android." \
                      "widget.ImageView"
        return danglaoshi_logo
    # 版本
    tv_version = "com.ruicheng.teacher:id/tv_version"
    # 官方网站
    official_website = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget." \
                       "FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget." \
                       "RelativeLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android." \
                       "widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView[1]"
    # 网址
    official_website_url = "com.ruicheng.teacher:id/tv_our_net"
    # 官方微博

    def get_official_msg(self, i):
        msg = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget." \
                     "FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android." \
                     "widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget." \
                     "RelativeLayout/android.widget.LinearLayout/android.widget." \
                     "LinearLayout["+str(i)+"]/android.widget.TextView[1]"
        return msg
    # 微博号
    official_weibo_nick = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget." \
                          "FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget." \
                          "RelativeLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android." \
                          "widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.TextView[2]"
    # 官方微信
    official_wechat = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget." \
                      "FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget." \
                      "RelativeLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android." \
                      "widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.TextView[1]"
    # 微信号
    official_wechat_nick = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget." \
                           "FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget." \
                           "RelativeLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android." \
                           "widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.TextView[2]"
    # Copyright

    def get_danglaoshi_rights(self, i):
        danglaoshi_rights = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget." \
                        "FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget." \
                        "RelativeLayout/android.widget.LinearLayout["+str(i)+"]/android.widget.LinearLayout[2]/android." \
                        "widget.TextView"
        return danglaoshi_rights

