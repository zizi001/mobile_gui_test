from danglaoshi.Common import BaseMethod
from danglaoshi.Data.Elements import PositionLogin


def register(user, verification_code, pwd):
    BaseMethod.to_activity(".Activity.LoginActivity")
    BaseMethod.send(PositionLogin.PositionLogin.username, user)
    BaseMethod.click(PositionLogin.PositionLogin.bt_regist_login)
    if BaseMethod.is_exist(PositionLogin.PositionLogin.md_buttonDefaultPositive):
        BaseMethod.click(PositionLogin.PositionLogin.md_buttonDefaultPositive)
        BaseMethod.send(PositionLogin.PositionLogin.et_verify_code, verification_code)
        BaseMethod.send(PositionLogin.PositionLogin.et_new_password, pwd)
        BaseMethod.click(PositionLogin.PositionLogin.bt_register)


def register_cancel(user):
    BaseMethod.to_activity(".Activity.LoginActivity")
    BaseMethod.send(PositionLogin.PositionLogin.username, user)
    BaseMethod.click(PositionLogin.PositionLogin.bt_regist_login)
    if BaseMethod.is_exist(PositionLogin.PositionLogin.md_buttonDefaultNegative):
        BaseMethod.click(PositionLogin.PositionLogin.md_buttonDefaultNegative)

