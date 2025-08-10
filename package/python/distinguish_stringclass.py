import re

def list_distinguish_ascii(list):
#返回：ascii列表和非ascii列表
    non_ascii_list = []
    ascii_list = []
    for string in list:
        try:
            string.encode('ascii')
            ascii_list.append(string)
        except UnicodeEncodeError:
            non_ascii_list.append(string)
    return [ascii_list,non_ascii_list]

def list_distinguish_chinese(list):
    chinese_list = []
    non_chinese_list = []
    for string in list:
        if bool(re.search(r'[\u4e00-\u9fff]', string)):
            chinese_list.append(string)
        else:
            non_chinese_list.append(string)
    return [chinese_list,non_chinese_list]
