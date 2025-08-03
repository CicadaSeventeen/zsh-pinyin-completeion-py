import os
import distinguish_stringclass

list_filename = os.listdir
listdir = list_filename

def listdir_ascii_or_not(path):
    return distinguish_stringclass.list_distinguish_ascii(list_filename(path))

def listdir_chinese_or_not(path):
    return distinguish_stringclass.list_distinguish_chinese(list_filename(path))

def listdir_ascii_and_chinese_or_not(path):
    [ ascii_list , non_ascii_list ] = distinguish_stringclass.list_distinguish_ascii(list_filename(path))
    return [ascii_list] + distinguish_stringclass.list_distinguish_chinese(non_ascii_list)
# [ Ascii, Chinese, Other non-Ascii ]
