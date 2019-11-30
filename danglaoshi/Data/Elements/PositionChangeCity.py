# 报考城市相关页面元素
class PositionChangeCity:
    # 我
    foot_user = "com.ruicheng.teacher:id/foot_user"
    # 报考城市
    tv_city = "com.ruicheng.teacher:id/tv_city"

    # 省 （i 从 1 开始）
    def province_xpath(self, i):
        province = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/" \
                   "android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/" \
                   "android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[" + str(i) + "]/" \
                   "android.widget.RelativeLayout/android.widget.TextView"
        return province

    # 市（i 从 1 开始）
    def city_xpath(self, i, straight_city=False):
        if not straight_city:
            city = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/" \
                   "android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/" \
                   "android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[" + str(i) + "]/" \
                   "android.widget.RelativeLayout/android.widget.TextView"
        else:
            city = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/" \
                   "android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/" \
                   "android.support.v7.widget.RecyclerView/android.widget.RelativeLayout/" \
                   "android.widget.RelativeLayout/android.widget.TextView"
        return city
    # 缓存
    tv_cachesize = "com.ruicheng.teacher:id/tv_cachesize"
    # 确定清除缓存
    md_buttonDefaultPositive = "com.ruicheng.teacher:id/md_buttonDefaultPositive"
