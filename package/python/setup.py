# setup.py

from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize
import os
import fnmatch

# --- 配置部分 ---

# 项目名称
PROJECT_NAME = "your_project_name"

# 项目版本
PROJECT_VERSION = "0.1"

# 项目描述
PROJECT_DESCRIPTION = "A project compiled with Cython"

# 包含源代码的根目录
SOURCE_DIR = "."  # 假设 setup.py 在项目根目录

# --- 辅助函数 ---

def find_pyx_and_py_files(directory):
    """递归查找目录下所有的 .pyx 和 .py 文件（排除 __init__.py 和 setup.py 本身）"""
    extensions = []
    for root, _, files in os.walk(directory):
        # 跳过 'build' 和 'dist' 等目录（如果存在）
        if 'build' in root.split(os.sep) or 'dist' in root.split(os.sep):
            continue

        for file in files:
            if file.endswith(('.pyx', '.py')) and file not in ('__init__.py', 'setup.py'):
                # 构造文件的完整路径
                full_path = os.path.join(root, file)

                # 计算模块名：相对于 SOURCE_DIR 的路径，去掉扩展名，并将路径分隔符替换为 '.'
                rel_path = os.path.relpath(full_path, SOURCE_DIR)
                module_name = os.path.splitext(rel_path)[0].replace(os.sep, '.')

                extensions.append(Extension(module_name, [full_path]))
    return extensions

# --- 要忽略的标准库/内置模块列表 (你提供的列表中的一部分) ---
# Cython 不会处理这些，它们必须在运行时环境存在
IGNORED_IMPORTS = {
    '__future__', '__main__', '_abc', '_ast', '_bisect', '_bz2',
    '_codecs', '_collections', '_collections_abc', '_compression',
    '_distutils_hack', '_frozen_importlib', '_frozen_importlib_external',
    '_functools', '_imp', '_io', '_json', '_lzma', '_opcode',
    '_opcode_metadata', '_operator', '_random', '_signal', '_sitebuiltins',
    '_sre', '_stat', '_thread', '_tokenize', '_typing', '_warnings',
    '_weakref', '_weakrefset', 'abc', 'ast', 'bisect', 'builtins', 'bz2',
    'codecs', 'collections', 'collections.abc', 'contextlib', 'copy',
    'copyreg', 'dis', 'encodings', 'encodings.aliases', 'encodings.utf_8',
    'encodings.utf_8_sig', 'enum', 'errno', 'fnmatch', 'functools',
    'genericpath', 'glob', 'grp', 'importlib', 'importlib._abc',
    'importlib._bootstrap', 'importlib._bootstrap_external',
    'importlib.machinery', 'importlib.resources',
    'importlib.resources._common', 'importlib.resources._functional',
    'importlib.resources.abc', 'importlib.util', 'inspect', 'io',
    'itertools', 'json', 'json.decoder', 'json.encoder', 'json.scanner',
    'keyword', 'linecache', 'lzma', 'marshal', 'math', 'ntpath', 'opcode',
    'operator', 'os', 'os.path', 'pathlib', 'pathlib._abc',
    'pathlib._local', 'posix', 'posixpath', 'pwd', 'random', 're',
    're._casefix', 're._compiler', 're._constants', 're._parser',
    'reprlib', 'shutil', 'site', 'stat', 'sys', 'tempfile', 'time',
    'token', 'tokenize', 'types', 'typing', 'warnings', 'weakref',
    'zipimport', 'zlib'
}

# --- 要声明的第三方依赖 ---
# 这些需要在目标环境通过 pip 安装
THIRD_PARTY_DEPENDENCIES = [
    'pypinyin',
    'anyascii',
    'unidecode',
    # 如果 completion, converter, distinguish_stringclass, listdir, listdir_convert 是你的本地 .py 文件，则不需要在这里声明
    # 如果它们是第三方的，则需要添加到这里
]

# --- 主逻辑 ---

# 1. 查找所有需要编译的源文件
extensions = find_pyx_and_py_files(SOURCE_DIR)

# 2. 使用 Cython 编译扩展
# compiler_directives={'language_level': "3"} 设置 Python 3 语法
# 如果你的代码使用了类型注解，可能还需要其他指令
cythonized_extensions = cythonize(
    extensions,
    compiler_directives={'language_level': "3"},
    # 如果需要调试信息，可以添加 build_dir='build' 等选项
)

# 3. 设置 setuptools
setup(
    name=PROJECT_NAME,
    version=PROJECT_VERSION,
    description=PROJECT_DESCRIPTION,
    # 自动发现 packages (如果你的项目结构是标准的包结构)
    packages=find_packages(where=SOURCE_DIR),
    # 指定包的根目录
    package_dir={'': SOURCE_DIR},
    # 提供编译好的扩展模块
    ext_modules=cythonized_extensions,
    # 声明 Python 依赖 (如果你的代码需要特定版本)
    python_requires='>=3.6',
    # 声明第三方依赖，这样用户安装你的包时会自动安装这些依赖
    install_requires=THIRD_PARTY_DEPENDENCIES,
    # 如果你的项目包含数据文件，可能需要配置 package_data 或 MANIFEST.in
    # package_data={...},
    # 如果你希望生成的 wheel 是平台特定的（因为它包含了编译的 .so 文件）
    zip_safe=False,
)

print(f"Found and will cythonize {len(extensions)} modules.")
