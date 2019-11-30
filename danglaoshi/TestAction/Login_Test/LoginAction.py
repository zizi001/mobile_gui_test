from danglaoshi.Common import BaseMethod, Settings
from danglaoshi.Data.Elements import PositionLogin, PositionPersonalCenter


def login(user, pwd):
    BaseMethod.to_activity(".Activity.LoginActivity")
    # if BaseMethod.is_exist(PositionLogin.PositionLogin.username):
    #     pass
    # else:
    #     BaseMethod.swipe_left(500)
    #     BaseMethod.sleep(2)
    #     BaseMethod.swipe_left(500)
    #     BaseMethod.click(PositionLogin.PositionLogin.rl_logo)
    BaseMethod.send(PositionLogin.PositionLogin.username, user)
    BaseMethod.click(PositionLogin.PositionLogin.bt_regist_login)
    if BaseMethod.is_exist(PositionLogin.PositionLogin.password):
        BaseMethod.send(PositionLogin.PositionLogin.password, pwd)
        BaseMethod.click(PositionLogin.PositionLogin.bt_login)


def login_out():
    BaseMethod.to_activity(".Activity.SettingActivity")
    BaseMethod.click(PositionLogin.PositionLogin.bt_logout)


def after_login():
    while BaseMethod.is_exist(PositionPersonalCenter.PositionPersonalCenter.tv_i_know):
        if BaseMethod.is_exist(PositionPersonalCenter.PositionPersonalCenter.rl_close):
            BaseMethod.click(PositionPersonalCenter.PositionPersonalCenter.rl_close)
        else:
            BaseMethod.click(PositionPersonalCenter.PositionPersonalCenter.tv_i_know)
    if BaseMethod.is_exist(PositionPersonalCenter.PositionPersonalCenter.tv_btn):
        BaseMethod.click(PositionPersonalCenter.PositionPersonalCenter.tv_btn)
    while BaseMethod.is_exist(PositionPersonalCenter.PositionPersonalCenter.iv_close1):
        BaseMethod.click(PositionPersonalCenter.PositionPersonalCenter.iv_close1)
    BaseMethod.click(PositionPersonalCenter.PositionPersonalCenter.foot_user)
    BaseMethod.sleep(1)
    BaseMethod.swipe_on('up')
    header = BaseMethod.get_text(PositionPersonalCenter.PositionPersonalCenter.header)
    BaseMethod.swipe_on('down')
    headers = header.split('---=====')
    Settings.HEADERS = {'userId': headers[0], 'sessionId': headers[1]}
    BaseMethod.click(PositionPersonalCenter.PositionPersonalCenter.foot_home)


# 清理勋章
def clear_medal():
    if BaseMethod.is_exist(PositionPersonalCenter.PositionPersonalCenter.rl_close):
        BaseMethod.click(PositionPersonalCenter.PositionPersonalCenter.rl_close)
