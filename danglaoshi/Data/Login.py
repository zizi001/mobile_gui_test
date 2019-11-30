# coding:utf-8
from danglaoshi.Common import ReadExcel

if __name__ == "__main__":
    filePath = "LoginCase.xlsx"
    sheetName = u"Sheet1"
    data = ReadExcel.ExcelUtil(filePath, sheetName)
    print(data.dict_data())
