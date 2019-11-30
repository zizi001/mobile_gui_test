# 模考大赛
from danglaoshi.Common import BaseMethod
import unittest
from danglaoshi.TestAction.Login_Test import LoginAction
from danglaoshi.Data.Elements.PositionPersonalInformation import PositionPersonalInformation
from ddt import ddt, data, unpack


@ddt
class PersonalInformationCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        BaseMethod.driver_open(True)
        LoginAction.login("13100000991", "123456")
        LoginAction.after_login()

    def setUp(self):
        pass

    def tearDown(self):
        BaseMethod.sleep(1)
        BaseMethod.to_activity(".Activity.MainActivity")
        BaseMethod.sleep(1)

    @classmethod
    def tearDownClass(cls):
        LoginAction.login_out()
        BaseMethod.driver_close()

    # @unittest.skip('')
    def test_nickname_phone(self):
        position_personal_info = PositionPersonalInformation()
        BaseMethod.click(elem_detail=position_personal_info.foot_user)
        nickname_out = BaseMethod.get_text(elem_detail=position_personal_info.tv_nickname)
        phone_out = BaseMethod.get_text(elem_detail=position_personal_info.tv_nickname_id)
        BaseMethod.click(elem_detail=position_personal_info.rl_myuser)
        nickname_in = BaseMethod.get_text(elem_detail=position_personal_info.tv_nickname)
        self.assertEqual(nickname_in, nickname_out, "用户中心的昵称："+nickname_out+" != 个人信息的昵称："+nickname_in)
        BaseMethod.click(position_personal_info.tv_change_phone)
        phone_in = BaseMethod.get_text(elem_detail=position_personal_info.et_phone)
        self.assertEqual(phone_in, phone_out, "用户中心的手机号：" + phone_out + " != 个人信息的手机号：" + phone_in)
        BaseMethod.click(elem_detail=position_personal_info.iv_back)
        BaseMethod.click(elem_detail=position_personal_info.iv_back)

    # @unittest.skip('')
    def test_change_picture(self):
        position_personal_info = PositionPersonalInformation()
        BaseMethod.click(elem_detail=position_personal_info.foot_user)
        BaseMethod.click(elem_detail=position_personal_info.rl_myuser)
        BaseMethod.sleep(1)
        BaseMethod.click(elem_detail=position_personal_info.tv_head_picture_name)
        picture_source1 = BaseMethod.get_text(elem_detail=position_personal_info.bt_take_photo)
        self.assertEqual(picture_source1, '拍照', '头像来源无：拍照')
        picture_source2 = BaseMethod.get_text(elem_detail=position_personal_info.bt_pick_photo)
        self.assertEqual(picture_source2, '从相册中选择', '头像来源无：从相册中选择')
        BaseMethod.click(elem_detail=position_personal_info.bt_cancel)
        BaseMethod.click(elem_detail=position_personal_info.iv_back)

    # @unittest.skip('')
    @data('', '1', 'ab', '呵呵3', '呵呵3', '呵呵呵呵', '12345678', '123456789')
    def test_change_nickname(self, nickname):
        position_personal_info = PositionPersonalInformation()
        BaseMethod.click(elem_detail=position_personal_info.foot_user)
        BaseMethod.click(elem_detail=position_personal_info.rl_myuser)
        nickname_old = BaseMethod.get_text(elem_detail=position_personal_info.tv_nickname)
        BaseMethod.click(elem_detail=position_personal_info.tv_nickname)
        BaseMethod.send(elem_detail=position_personal_info.et_nickname, value=nickname)
        BaseMethod.sleep(1)
        BaseMethod.click(elem_detail=position_personal_info.tv_left_title)
        BaseMethod.sleep(1)
        if nickname.__len__() in range(2, 9):
            pass
        else:
            title = BaseMethod.get_text(elem_detail=position_personal_info.tv_titile)
            self.assertEqual(title, '修改昵称', '新昵称的长度不在2-8个字中间，保存后，页面不在修改昵称页面')
            BaseMethod.click(elem_detail=position_personal_info.iv_back)
        nickname_new_in = BaseMethod.get_text(elem_detail=position_personal_info.tv_nickname)
        BaseMethod.click(elem_detail=position_personal_info.iv_back)
        nickname_new_out = BaseMethod.get_text(elem_detail=position_personal_info.tv_nickname)
        if nickname.__len__() in range(2, 9):
            self.assertEqual(nickname_new_in, nickname, '个人信息中的新昵称：'+nickname_new_in+' != 输入的新昵称：'+nickname)
            self.assertEqual(nickname_new_out, nickname, '用户中心中的新昵称：' + nickname_new_out + ' != 输入的新昵称：' + nickname)
        else:
            self.assertEqual(nickname_new_in, nickname_old,
                             '输入昵称为：'+nickname+'时，个人信息昵称预期不变即：'+nickname_old+'当前为：'+nickname_new_in)
            self.assertEqual(nickname_new_out, nickname_old,
                             '输入昵称为：' + nickname + '时，用户中心昵称预期不变即：' + nickname_old + '当前为：' + nickname_new_out)

    # @unittest.skip('')
    def test_change_sex(self):
        position_personal_info = PositionPersonalInformation()
        BaseMethod.click(elem_detail=position_personal_info.foot_user)
        BaseMethod.click(elem_detail=position_personal_info.rl_myuser)
        sex_old = BaseMethod.get_text(elem_detail=position_personal_info.tv_gender)
        BaseMethod.click(elem_detail=position_personal_info.tv_gender)
        if sex_old == '未设置':
            pass
        else:
            BaseMethod.swipe_up_small()
            BaseMethod.sleep(2)
        BaseMethod.click(elem_detail=position_personal_info.tv_confirm)
        sex_new = BaseMethod.get_text(elem_detail=position_personal_info.tv_gender)
        if sex_old == '男':
            self.assertEqual(sex_new, '女', '原性别为：' + sex_old + '，预期为：女，现状为：' + sex_new)
        else:
            self.assertEqual(sex_new, '男', '原性别为：'+sex_old+'，预期为：男，现状为：'+sex_new)
        BaseMethod.click(elem_detail=position_personal_info.iv_back)

    # @unittest.skip('')
    @data(('', '', False), ('17712341234', '', False), ('', '1234', False),
          ('17712341234', '1324', False), ('17712341234', '66666666', True))
    @unpack
    def test_change_phone(self, phone, code, result):
        position_personal_info = PositionPersonalInformation()
        BaseMethod.click(elem_detail=position_personal_info.foot_user)
        phone_out_before = BaseMethod.get_text(elem_detail=position_personal_info.tv_nickname_id)
        BaseMethod.click(elem_detail=position_personal_info.rl_myuser)
        BaseMethod.click(elem_detail=position_personal_info.tv_change_phone)
        phone_in_before = BaseMethod.get_text(elem_detail=position_personal_info.et_phone)
        BaseMethod.click(elem_detail=position_personal_info.bt_binding)
        BaseMethod.sleep(1)
        BaseMethod.send(elem_detail=position_personal_info.et_phone, value=phone)
        BaseMethod.send(elem_detail=position_personal_info.et_verify_code, value=code)
        BaseMethod.click(elem_detail=position_personal_info.bt_binding)
        BaseMethod.sleep(2)
        if not result:
            BaseMethod.click(elem_detail=position_personal_info.iv_back)
        else:
            BaseMethod.click(elem_detail=position_personal_info.tv_change_phone)
        phone_in_after = BaseMethod.get_text(elem_detail=position_personal_info.et_phone)
        BaseMethod.click(elem_detail=position_personal_info.iv_back)
        BaseMethod.click(elem_detail=position_personal_info.iv_back)
        phone_out_after = BaseMethod.get_text(elem_detail=position_personal_info.tv_nickname_id)
        if result:
            BaseMethod.click(elem_detail=position_personal_info.foot_user)
            BaseMethod.click(elem_detail=position_personal_info.rl_myuser)
            BaseMethod.click(elem_detail=position_personal_info.tv_change_phone)
            BaseMethod.click(elem_detail=position_personal_info.bt_binding)
            BaseMethod.sleep(1)
            BaseMethod.send(elem_detail=position_personal_info.et_phone, value='13100000991')
            BaseMethod.send(elem_detail=position_personal_info.et_verify_code, value='66666666')
            BaseMethod.click(elem_detail=position_personal_info.bt_binding)
            BaseMethod.sleep(1)
            BaseMethod.click(elem_detail=position_personal_info.iv_back)
            BaseMethod.click(elem_detail=position_personal_info.iv_back)
        self.assertEqual(phone_out_before, phone_in_before, '修改前的手机号内外不同')
        self.assertEqual(phone_in_after, phone_out_after, '修改后的手机号内外不同')
        if result:
            self.assertEqual(phone, phone_out_after, '修改手机号失败')
        else:
            self.assertEqual(phone_out_before, phone_out_after, '修改手机号失败')

    @data(('', '', False), ('123456', '', False), ('', '123456789', False),
          ('123456', '11', False), ('123456', '123456789', True))
    @unpack
    def test_change_pwd(self, old_pwd, new_pwd, result):
        position_personal_info = PositionPersonalInformation()
        BaseMethod.click(elem_detail=position_personal_info.foot_user)
        BaseMethod.click(elem_detail=position_personal_info.rl_myuser)
        BaseMethod.click(elem_detail=position_personal_info.tv_change_ps)
        BaseMethod.send(elem_detail=position_personal_info.et_old_password, value=old_pwd)
        BaseMethod.send(elem_detail=position_personal_info.et_new_password, value=new_pwd)
        BaseMethod.click(elem_detail=position_personal_info.bt_confirm)
        BaseMethod.sleep(1)
        LoginAction.login_out()
        BaseMethod.sleep(1)
        if result:
            LoginAction.login('13100000991', new_pwd)
        else:
            LoginAction.login('13100000991', '123456')
        BaseMethod.sleep(1)
        actual_activity = BaseMethod.current_activity()
        if result:
            BaseMethod.click(elem_detail=position_personal_info.foot_user)
            BaseMethod.click(elem_detail=position_personal_info.rl_myuser)
            BaseMethod.click(elem_detail=position_personal_info.tv_change_ps)
            BaseMethod.send(elem_detail=position_personal_info.et_old_password, value=new_pwd)
            BaseMethod.send(elem_detail=position_personal_info.et_new_password, value='123456')
            BaseMethod.click(elem_detail=position_personal_info.bt_confirm)
            BaseMethod.sleep(1)
            BaseMethod.click(elem_detail=position_personal_info.iv_back)
        self.assertEqual(actual_activity, '.Activity.MainActivity', '修改密码后登录失败')


if __name__ == '__main__':
    unittest.main()
