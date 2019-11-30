# coding:utf-8
'''收藏相关'''


class PositionMyCollection:
    # 练习按钮
    tv_practice = "com.ruicheng.teacher:id/foot_home"
    # 更多
    more_button = "com.ruicheng.teacher:id/tv_left_title"
    # 我的收藏
    my_collection = "com.ruicheng.teacher:id/ll_favoriter"
    # 幼儿园综合素质

    def get_my_collection_list(self, i):
        my_collection_list = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget." \
                        "FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android." \
                        "widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget." \
                        "LinearLayout["+str(i)+"]/android.widget.RelativeLayout"
        return my_collection_list
    # 保教知识
    my_collection_two = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget." \
                        "FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android." \
                        "widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget." \
                        "LinearLayout[1]/android.widget.RelativeLayout"
    # 我的收藏中没有题目
    no_collection = "com.ruicheng.teacher:id/iv_error_bg"
    # 收藏列表title
    collection_list_title = "com.ruicheng.teacher:id/relativeLayout1"
    # 更多 back key
    more_collection_back = "com.ruicheng.teacher:id/iv_back"
    # 收藏列表返回key
    collection_back = "com.ruicheng.teacher:id/iv_back"
    # 我的收藏列表返回key
    my_collection_back = "com.ruicheng.teacher:id/iv_back"
    # 收藏列表xpath
    collection_list = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget." \
                      "FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget." \
                      "RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android." \
                      "widget.RelativeLayout/android.widget.TextView"
    # 我的收藏title
    my_collection_title = "com.ruicheng.teacher:id/tv_titile"
    # 我的收藏中当前题目号
    current_num = "com.ruicheng.teacher:id/tv_usednum"
    # 我的收藏中总题数
    total_num = "com.ruicheng.teacher:id/tv_total"

    # 题目内容
    tv_body = "com.ruicheng.teacher:id/tv_body"
    # 选项id
    rb_btnA = "com.ruicheng.teacher:id/rb_btnA"
    rb_btnB = "com.ruicheng.teacher:id/rb_btnB"
    rb_btnC = "com.ruicheng.teacher:id/rb_btnC"
    rb_btnD = "com.ruicheng.teacher:id/rb_btnD"
    rb_btn = [rb_btnA, rb_btnB, rb_btnC, rb_btnD]

    # 作答数据信息(正确答案是：D 本题共被答141239次，正确率：34.71% 易错项为：A)
    answer_data_information = "com.ruicheng.teacher:id/tv_answer"
    # 解析
    parsing = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android." \
              "widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4." \
              "view.ViewPager/android.widget.RelativeLayout/android.widget.ScrollView/android.widget." \
              "LinearLayout/android.widget.LinearLayout[2]/android.widget.TextView[2]"
    # 解析详情
    parsing_details = "	com.ruicheng.teacher:id/tv_explanation"
    # 题目纠错
    title_error_correction = "com.ruicheng.teacher:id/tv_problems_error"
    # 移除收藏
    collection_remove = "com.ruicheng.teacher:id/rl_remove"


