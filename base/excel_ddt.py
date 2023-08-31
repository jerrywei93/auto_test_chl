import openpyxl
from keywords import KeyUI


"""
excel文件操作步骤
    1、打开Excel文件
    2、打开指定的sheet页
    3、操作指定的单元格或行
"""


def param(value):
    """
    将传入的数据先按 &，再按 = 拆分后存入字典
    :param value:
    :return:
    """
    data = {}
    if value:
        dic = value.split("&")
        for item in dic:
            item = item.split("=", 1)
            data[item[0]] = item[1]
    return data


def excel_execute(file='../excel_data/demo.xlsx', sheet='Sheet1'):
    # 打开Excel文件
    excel = openpyxl.load_workbook(file)

    # 读取指定sheet页
    sheet = excel[sheet]

    # 读取文件的所有内容
    for row in sheet.values:
        # print(f'{row}')

        if type(row[2]) is int:
            data = param(row[4])

            # 根据“动作”列方法名调用KeyUI对应方法
            print(f'第{row[2]}步，开始执行动作：{row[3]}')
            if row[3] == 'open_browser':
                key = KeyUI(**data)
            else:
                getattr(key, row[3])(**data)


if __name__ == "__main__":
    excel_execute(file='../excel_data/demo.xlsx', sheet='Sheet1')
