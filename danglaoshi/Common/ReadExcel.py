# coding:utf-8
import xlrd


class ExcelUtil:
    # 构造方法
    def __init__(self, excel_path, sheet_name):
        self.data = xlrd.open_workbook(excel_path)
        self.table = self.data.sheet_by_name(sheet_name)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols

    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            for i in range(self.rowNum - 1):
                s = {}
                # 从第二行取对应values值
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
            return r


'''
四. 进阶-对象实例化

# coding=utf-8
# 读取excel内容
import xlrd


class OperationExcel:
    def __init__(self, file_name=None, sheet_id=None):
        if file_name:
            self.file_name = self.file_name
            self.sheet_id = self.sheet_id

        else:
            self.file_name = '..\dataconfig\interfaceTestCase.xlsx'
            self.sheet_id = 0
        self.data = self.get_data()

    # 获取sheets的内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables

    # 获取单元格的行数
    def get_lines(self):
        tables = self.data
        return tables.nrows

    # 获取某一个单元格的内容
    def get_cell_value(self, row, col):
        return self.data.cell_value(row, col)


if __name__ == '__main__':
    opers = OperationExcel()
    print opers.get_data().nrows
    print opers.get_lines()
    print opers.get_cell_value(1, 3)
'''