# coding:utf-8
'''练习'''


# 科目名称xpath ( i 从 1 开始)
def subject_name_xpath(i):
    subject_name = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/" \
                   "android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/" \
                   "android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/" \
                   "android.view.View/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout["+str(i)+"]/" \
                   "android.widget.RelativeLayout/android.widget.RelativeLayout[1]/" \
                   "android.widget.LinearLayout/android.widget.TextView[1]"
    return subject_name


# 科目版本xpath（ i 从 1 开始）
def subject_version_xpath(i):
    subject_version = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/" \
                   "android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/" \
                   "android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/" \
                   "android.view.View/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout["+str(i)+"]/" \
                   "android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.TextView"
    return subject_version


# 科目显示的闯关进度xpath（ i 从 1 开始）
def subject_speed_xapth(i=1):
    subject_speed = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/" \
                    "android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/" \
                    "android.widget.FrameLayout/android.widget.RelativeLayout/android.view.View/" \
                    "android.support.v7.widget.RecyclerView/android.widget.RelativeLayout["+str(i)+"]/" \
                    "android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/" \
                    "android.widget.LinearLayout[1]/android.widget.TextView[2]"
    return subject_speed


# 科目显示的获得星星xpath（ i 从 1 开始）
def subject_star_xapth(i=1):
    subject_star = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/" \
                    "android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/" \
                    "android.widget.FrameLayout/android.widget.RelativeLayout/android.view.View/" \
                    "android.support.v7.widget.RecyclerView/android.widget.RelativeLayout["+str(i)+"]/" \
                    "android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/" \
                    "android.widget.LinearLayout[2]/android.widget.TextView[2]"
    return subject_star


# 章节名称xpath（ i 从 1 开始）
def chapter_name_xpath(i):
    chapter_name = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/" \
                   "android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/" \
                   "android.widget.RelativeLayout/android.view.View/android.support.v7.widget.RecyclerView/" \
                   "android.widget.RelativeLayout["+str(i)+"]/android.widget.LinearLayout[1]/" \
                    "android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[2]"
    return chapter_name


# 章节知识点总个数xpath（ i 从 1 开始）
def chapter_knowledge_number_xpath(i):
    chapter_knowledge_number = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/" \
                   "android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/" \
                   "android.widget.RelativeLayout/android.view.View/android.support.v7.widget.RecyclerView/" \
                   "android.widget.RelativeLayout["+str(i)+"]/android.widget.LinearLayout[1]/" \
                    "android.widget.LinearLayout[2]/android.widget.LinearLayout[2]/android.widget.TextView[3]"
    return chapter_knowledge_number


# 章节显示的闯关进度xpath（ i 从 1 开始）
def chapter_speed_xpath(i=1):
    subject_speed = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/" \
                    "android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/" \
                    "android.widget.RelativeLayout/android.view.View/android.support.v7.widget.RecyclerView/" \
                    "android.widget.RelativeLayout["+str(i)+"]/android.widget.LinearLayout[1]/" \
                    "android.widget.LinearLayout[2]/android.widget.LinearLayout[2]/android.widget.TextView[1]"
    return subject_speed


# 章节显示的获得星星xpath（ i 从 1 开始）
def chapter_star_xpath(i=1):
    subject_star = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/" \
                    "android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/" \
                    "android.widget.RelativeLayout/android.view.View/android.support.v7.widget.RecyclerView/" \
                    "android.widget.RelativeLayout["+str(i)+"]/android.widget.LinearLayout[1]/" \
                    "android.widget.LinearLayout[2]/android.widget.LinearLayout[2]/android.widget.TextView[4]"
    return subject_star


# 大知识点id
knowledge_big = "com.ruicheng.teacher:id/chapter_title"

# 知识子点id
knowledge_small = "com.ruicheng.teacher:id/checkpoint_title"

# 闯关页面小点点xpath（ i 从 1 开始）
def knowledge_point_xpath(i):
    knowledge_point = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/" \
                      "android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/" \
                      "android.widget.LinearLayout[2]/android.widget.ImageView["+str(i)+"]"
    return knowledge_point


# 开始闯关/未解锁
begin_break_practice = 'com.ruicheng.teacher:id/tv_open'

# 返回
iv_back = "com.ruicheng.teacher:id/iv_back"
# 学段类型
tv_title2 = "com.ruicheng.teacher:id/tv_title2"
# 练习按钮
tv_practice = "com.ruicheng.teacher:id/tv_practice"
# 通关数
tv_pass_num = "com.ruicheng.teacher:id/tv_pass_num"
# 通关总数
tv_pass_total_num = "com.ruicheng.teacher:id/tv_pass_total_num"
# 获得星星数
tv_get_stars_num = "com.ruicheng.teacher:id/tv_get_stars_num"

# 错题练习
tv_wrong_training = "com.ruicheng.teacher:id/tv_wrong_training"
# 智能练习
tv_intelligence_training = "com.ruicheng.teacher:id/tv_intelligence_training"
# 练习记录
tv_training_record = "com.ruicheng.teacher:id/tv_training_record"
# 章节名称
tv_course_name = "com.ruicheng.teacher:id/tv_course_name"
# 课程闯关数
tv_course_pass_num = "com.ruicheng.teacher:id/tv_course_pass_num"
# 课程总关数
tv_course_total_num = "com.ruicheng.teacher:id/tv_course_total_num"
# 课程获得星星数
tv_course_get_stars_num = "com.ruicheng.teacher:id/tv_course_get_stars_num"
# 课程获得总星星数
tv_course_stars_total_num = "com.ruicheng.teacher:id/tv_course_stars_total_num"
# 学习天数
tv_study_days = "com.ruicheng.teacher:id/tv_study_days"
# 闯关次数
tv_pass_times = "com.ruicheng.teacher:id/tv_pass_times"
# 三星通关
tv_stars_pass_num = "com.ruicheng.teacher:id/tv_stars_pass_num"
'''闯关'''
# 开始闯关按钮
tv_open = "com.ruicheng.teacher:id/tv_open"
# 1星
iv_star1 = "com.ruicheng.teacher:id/iv_star1"
# 2星
iv_star2 = "com.ruicheng.teacher:id/iv_star2"
# 3星
iv_star3 = "com.ruicheng.teacher:id/iv_star3"

'''做题'''
# 当前题号
tv_usednum = "com.ruicheng.teacher:id/tv_usednum"
# 总题目数
tv_total = "com.ruicheng.teacher:id/tv_total"
# 当前题目类型
tv_tittle = "com.ruicheng.teacher:id/tv_tittle"
# 当前答对个数
tv_main_title = "com.ruicheng.teacher:id/tv_main_title"


# 选项
def option(answer):
    return "com.ruicheng.teacher:id/rb_btn" + answer


# A
rb_btnA = "com.ruicheng.teacher:id/rb_btnA"
# B
rb_btnB = "com.ruicheng.teacher:id/rb_btnB"
# C
rb_btnC = "com.ruicheng.teacher:id/rb_btnC"
# D
rb_btnD = "com.ruicheng.teacher:id/rb_btnD"

# 多选下一题按键
next_questions ="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/" \
                "android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/" \
                "android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.RelativeLayout/" \
                "android.widget.TextView"

'''答题星星进度'''
# 1星
iv_pass_through_star_01 = "com.ruicheng.teacher:id/iv_pass_through_star_01"
# 2星
iv_pass_through_star_02 = "com.ruicheng.teacher:id/iv_pass_through_star_02"
# 3星
iv_pass_through_star_03 = "com.ruicheng.teacher:id/iv_pass_through_star_03"

# 求安慰
comfort = "com.ruicheng.teacher:id/tv_open"
# 重新挑战
tv_replay = "com.ruicheng.teacher:id/tv_replay"
# 作答结果
tv_result = "com.ruicheng.teacher:id/tv_result"

'''错题解析'''
# 错题解析
tv_erro = "com.ruicheng.teacher:id/tv_erro"
'''全部解析'''
# 全部解析
tv_allerro = "com.ruicheng.teacher:id/tv_allerro"

