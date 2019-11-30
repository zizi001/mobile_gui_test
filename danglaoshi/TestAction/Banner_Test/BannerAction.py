# -*- coding:utf-8 -*-
#banner的点击执行
from danglaoshi.Common import BaseMethod
from danglaoshi.Data.Elements import PositionBanner
import time


def banner_exist():
    if BaseMethod.is_exist(PositionBanner.PositionBanner.banner):
        BaseMethod.click(PositionBanner.PositionBanner.banner)
        BaseMethod.sleep(3)
        BaseMethod.click(PositionBanner.PositionBanner.return_ck)


def banner_broadcast():
    b = BaseMethod.get_text(PositionBanner.PositionBanner.curnum)
    if b == 1:
        BaseMethod.click(PositionBanner.PositionBanner.banner)
        BaseMethod.sleep(3)
        BaseMethod.click(PositionBanner.PositionBanner.return_ck)





