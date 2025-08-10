local _polLingua_python_path=$(realpath ${${(%):-%x}:h})'/python'
local _polLingua_commands="python3 ${_polLingua_python_path}/main.py auto"
: "${COMPLETION_CMD_DIR_ONLY:=:cd:}"
#COMPLETION_CMD_FILE_ONLY=""
zmodload zsh/parameter
setopt extended_glob

_polLingua_core(){
    local _last_word=$(
    (
        IFS=$'\ \t\n\0'
        eval "set -- $words[CURRENT]"
        printf %q ${argv[-1]}
    ))
    compstate[pattern_match]='*'
    if [[ $_last_word == '' ]];then
        if [[ $COMPLETION_FILE_TYPE == 'file' ]];then
            _files -g '*(-.)' $@
        elif [[ $COMPLETION_FILE_TYPE == 'dir' ]];then
            _files -/ $@
        else
            _files $@
        fi
    else
        if [[ $_last_word == */ ]];then
            local _tmp_dirname=${_last_word%/}
        else
            local _tmp_dirname=$(dirname $_last_word)
            if [[ $words[CURRENT] == '~'* && $_tmp_dirname == "$HOME"* ]];then
                _tmp_dirname='~'${_tmp_dirname#$HOME}
            fi
        fi
        if [[ $_tmp_dirname == '.' ]];then
            if [[ $_last_word == './'* ]];then
                _tmp_dirname='./'
            else
                _tmp_dirname=''
            fi
        elif [[ $_tmp_dirname == '/' ]];then
            :
        else
            _tmp_dirname=$_tmp_dirname'/'
        fi
        local -a corrections
        corrections=( ${(f)${(s:\n:)"$(eval $_polLingua_commands $_last_word $PWD)"}})
        #compadd -f -U -S '/' $corrections[@]
        for _word in ${corrections}
        do
            #local _tmp_showname=$(printf %q $_tmp_dirname$_word)
           if [[ -d $(eval realpath $_tmp_dirname$_word) ]];then
                if [[ $_tmp_dirname == '' ]];then
                    compadd -f -U -S '/' $@ $_word $_tmp_dirname
                else
                    compadd -f -U -S '/' $@ -p $_tmp_dirname $_word
                fi
            else
                if [[ $_tmp_dirname == '' ]];then
                    compadd -f -U -S '' $@ $_word $_tmp_dirname
                else
                    compadd -f -U -S '' $@ -p $_tmp_dirname $_word
                fi
            fi
        done
    fi
    return 1
}

_polLingua_startswith() {
    [[ _matcher_num -gt 2 ]] && return 1
    COMPLETION_FILENAME_MATCH_MODE=startswith _polLingua_core $@
}

_polLingua_equal() {
    [[ _matcher_num -gt 2 ]] && return 1
    COMPLETION_FILENAME_MATCH_MODE=equal _polLingua_core $@
}

_polLingua_file_startswith() {
    [[ _matcher_num -gt 2 ]] && return 1
    COMPLETION_FILE_TYPE=file COMPLETION_FILENAME_MATCH_MODE=startswith _polLingua_core $@
}

_polLingua_file_equal() {
    [[ _matcher_num -gt 2 ]] && return 1
    COMPLETION_FILE_TYPE=file COMPLETION_FILENAME_MATCH_MODE=equal _polLingua_core $@
}

_polLingua_dir_startswith() {
    [[ _matcher_num -gt 2 ]] && return 1
    COMPLETION_FILE_TYPE=dir COMPLETION_FILENAME_MATCH_MODE=startswith _polLingua_core $@
}

_polLingua_dir_equal() {
    [[ _matcher_num -gt 2 ]] && return 1
    COMPLETION_FILE_TYPE=dir COMPLETION_FILENAME_MATCH_MODE=equal _polLingua_core $@
}

_polLingua_smart(){
    [[ _matcher_num -gt 2 ]] && return 1
    if [[ -n $words[1] && ":$COMPLETION_CMD_DIR_ONLY:" == *":$words[1]:"* ]]; then
            _polLingua_dir_startswith $@
    elif [[ -n $words[1] && ":$COMPLETION_CMD_FILE_ONLY:" == *":$words[1]:"* ]];then
            _polLingua_file_startswith $@
    else
        _polLingua_startswith $@
    fi
}
