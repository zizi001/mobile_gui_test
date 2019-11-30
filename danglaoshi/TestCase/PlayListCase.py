# 直播列表 & 回放列表
from danglaoshi.Common import BaseMethod
import unittest
from danglaoshi.TestAction.Login_Test import LoginAction
from danglaoshi.Data.Elements import PositionPlayList
from danglaoshi.TestAction.Course_Test import PlayListAction
from ddt import ddt, data, unpack


@ddt
class PlayListCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        BaseMethod.driver_open(True)
        LoginAction.login("13100000902", "123456")
        LoginAction.after_login()

    def setUp(self):
        self.position_play_list = PositionPlayList.PositionPlayList()
        self.play_list_action = PlayListAction.PlayListAction()

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        LoginAction.login_out()
        BaseMethod.driver_close()

    def test_live_list(self):
        self.play_list_action.go_in_play_list()
        BaseMethod.click(elem_detail=self.position_play_list.rb_living)
        self.play_list_action.click_lesson_name('大大大测试课')
        BaseMethod.sleep(3)
        name_in = BaseMethod.get_text(elem_detail=self.position_play_list.textView1)
        BaseMethod.click(elem_detail=self.position_play_list.iv_back)
        BaseMethod.click(elem_detail=self.position_play_list.md_buttonDefaultNegative)
        self.assertTrue(BaseMethod.is_exist(elem_detail=self.position_play_list.textView1))
        BaseMethod.click(elem_detail=self.position_play_list.iv_back)
        BaseMethod.click(elem_detail=self.position_play_list.md_buttonDefaultPositive)
        BaseMethod.click(elem_detail=self.position_play_list.iv_back)
        BaseMethod.click(elem_detail=self.position_play_list.iv_back)
        self.assertEqual(name_in, "大大大测试课", "正在直播的课程正确")

    def test_playback_list(self):
        self.play_list_action.go_in_play_list()
        BaseMethod.click(elem_detail=self.position_play_list.rb_vod)
        self.play_list_action.click_lesson_name("职业能力倾向测验")
        tips = BaseMethod.get_text(elem_detail=self.position_play_list.tips)
        BaseMethod.click(elem_detail=self.position_play_list.md_buttonDefaultPositive)
        BaseMethod.click(elem_detail=self.position_play_list.iv_back)
        BaseMethod.click(elem_detail=self.position_play_list.iv_back)
        self.assertEqual(tips, "正在努力生成回放中...", "无回放提示消息错误")

    def test_lesson_attachment(self):
        self.play_list_action.go_in_play_list()
        BaseMethod.click(elem_detail=self.position_play_list.rb_vod)
        self.play_list_action.click_lesson_attachment("职业能力倾向测验")
        tips = BaseMethod.get_text(elem_detail=self.position_play_list.tips)
        BaseMethod.click(elem_detail=self.position_play_list.md_buttonDefaultNegative)
        BaseMethod.click(elem_detail=self.position_play_list.iv_back)
        BaseMethod.click(elem_detail=self.position_play_list.iv_back)
        self.assertEqual(tips, "您当前处于WIFI网络，该课时讲义大小：772.68kb，是否下载？", "课件下载信息提示错误")


if __name__ == '__main__':
    unittest.main()
