# -*- coding:utf-8 -*-
#banner的点击执行
from danglaoshi.Common import BaseMethod
from danglaoshi.Data.Elements import PositionThreelogin
import time


def Threelogin_click():
    BaseMethod.to_activity(".Activity.LoginActivity")
    BaseMethod.sleep(3)
    BaseMethod.click(PositionThreelogin.PositionThreelogin.qq_sign_in)
    BaseMethod.sleep(3)
    BaseMethod.click_xpath(PositionThreelogin.PositionThreelogin.mobileqq)