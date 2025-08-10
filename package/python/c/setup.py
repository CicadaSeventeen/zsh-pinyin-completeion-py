from setuptools import setup
from Cython.Build import cythonize

setup(
    name="your_project",
    ext_modules=cythonize([
        "pypinyin/**/*.py",      # 递归编译pypinyin目录下所有.py文件
        "unidecode/**/*.py",     # 递归编译unidecode目录下所有.py文件
        "anyascii/**/*.py",      # 递归编译anyascii目录下所有.py文件
        "distinguish_stringclass.py",
        "converter.py",
        "listdir.py",
        "completion.py",
        "listdir_convert.py",    # 注意你写成了listdir_conver.py
        "main.py"
    ], compiler_directives={
        'language_level': 3,
        'boundscheck': False,
        'wraparound': False,
    }),
    zip_safe=False,
)
