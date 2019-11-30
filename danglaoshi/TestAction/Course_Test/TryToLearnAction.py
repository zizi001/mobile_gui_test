#from danglaoshi.Common import BaseMethod
# from danglaoshi.Data.Elements.PositionPersonalCenter import PositionPersonalCenter
# from danglaoshi.Data.Elements.PositionCourseList import PositionCourseList
# from danglaoshi.TestAction.PersonalCenter_Test import ExamTypeAction
# #
#
# class TryToLearnAction:
#     def __init__(self):
#         self.position_course_list = PositionCourseList()
#
#     # 判断课程是否存在
#     def find_course(self, course_name):
#         BaseMethod.sleep(1)
#         num = 0
#         while 1:
#             if BaseMethod.is_exist(elem_detail=self.position_course_list.course_name_ids, by='ids', i=num):
#                 course = BaseMethod.get_text(elem_detail=self.position_course_list.course_name_ids, by='ids', i=num)
#                 print('+++++++++++++++' + course)
#                 if course == course_name:
#                     BaseMethod.click(elem_detail=self.position_course_list.course_name_ids, by='ids', i=num)
#                     return True
#                 else:
#                     num = num + 1
#             else:
#                 last_before_swipe = BaseMethod.get_text(elem_detail=self.position_course_list.course_name_ids, by='ids',
#                                                         i=num - 1)
#                 BaseMethod.swipe_on('up', t=1500)
#                 BaseMethod.sleep(1.5)
#                 try:
#                     last_after_swipe = BaseMethod.get_text(elem_detail=self.position_course_list.course_name_ids,
#                                                            by='ids', i=num - 1)
#                 except Exception as error:
#                     print('***********' + str(error))
#                     num = 1
#                     continue
#                 if last_after_swipe == last_before_swipe:
#                     return False
#                 else:
#                     num = 1