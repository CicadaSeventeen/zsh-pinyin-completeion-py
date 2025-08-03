# zsh-pinyin-completion-py
## ZSH拼音补全，pypinyin实现

## 特色：
支持部分其他非ascii语言如俄语的拉丁化补全

可进行用户自定义配置

纯脚本语言写成，方便部署，无需编译

## 使用方法
1、将release中的压缩包放在你希望的位置
2、在zshrc中source completer.zsh
3、在zshrc中设定补全规则为诸如
```
zstyle ':completion:*' completer _commands _polLingua_startswith _complete  _correct _approximate _list
```

## 配置方法：环境变量，注意需要`export`
#### `COMPLETION_TYPE`
进行补全的文字类型，目前支持chinese和unicode

#### `COMPLETION_CONVERTER_PINYIN`
##### 拼音的转换规则：

`full`：全拼（小写）

`Full`：全拼（首字母大写）

`FUll`：全拼（声母大写）

`FULL`：全拼（大写）

`first_letter`：首字母（小写）

`FIRST_LETTER`：首字母（大写）

`initials`：声母（小写）

`Initials`：声母（首字母大写）

`INITIALS`：声母（大写）

##### 默认为`full:Full:FIRST_LETTER:first_letter`

#### `COMPLETION_PINYIN_HETERONYM`
是否对中文启用多音字支持。根据启用的强度区别选项包括：`off`、`auto`、`on`、`all`。默认为`auto`

#### `COMPLETION_CONVERTER_UNICODE`
##### 通用Unicode的转换规则：

`none`：不处理

`FuLl`：全文拉丁化

`full`：全文拉丁化（小写）

`Full`：全文拉丁化（首字母大写）

`FULL`：全文拉丁化（大写）

`First_Letter`：首字母拉丁化

`first_letter`：首字母拉丁化（小写）

`FIRST_LETTER`：首字母拉丁化（大写）

##### 默认为`FuLl`

#### `COMPLETION_UNICODE_LIB`

通用Unicode的拉丁化库，支持`unidecode`和`anyascii`，选择`both`则全部开启。默认为`both`

#### `COMPLETION_CASE_INSENSITIVE`

是否大小写不敏感。设置为`yes`则对一切输入进行大小写模糊匹配。默认为`no`

#### `COMPLETION_INGORE_ASCII`

是否忽视纯ascii文件名，测试功能，用于和shell内置文件补全同时开启。默认为`no`。未来可能移除。

## 其他项目
### for Zsh
https://github.com/adaptee/pinyin-completion 纯python实现，已经15年未维护

https://github.com/petronny/pinyin-completion adaptee的程序的fork和重写，依赖cpp-pinyin库，需要c和cpp编译环境（本人编译成功但运行失败）
### for Bash
https://github.com/AOSC-Dev/bash-pinyin-completion-rs 由AOSC维护，rust写成

https://github.com/emptyhua/bash-pinyin-completion c语言实现，已经5年未维护

https://github.com/adaptee/pinyin-completion 纯python实现，已经15年未维护
