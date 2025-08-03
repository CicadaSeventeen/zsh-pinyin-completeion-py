_polLingua_python_path=$(realpath ${${(%):-%x}:h})'/python'
_polLingua_startswith() {
    [[ _matcher_num -gt 2 ]] && return 1
    local _last_word=$(
    (
        IFS=$'\ \t\n\0'
        eval "set -- $words[CURRENT]"
        echo ${argv[-1]}
    ))
    _tags corrections files
    compstate[pattern_match]='*'
    local -a corrections
    if [[ $_last_word == '' ]];then
        corrections=( ${(f)${(s:\n:)"$(find . -maxdepth 1 -mindepth 1 -printf '%f\n')"}} )
    else
        corrections=( ${(f)${(s:\n:)"$(python3 ${_polLingua_python_path}/main_startswith.py $_last_word $PWD)"}})
    fi
    compadd -U "${corrections[@]}"
    return 0
}

_polLingua_equal() {
    [[ _matcher_num -gt 2 ]] && return 1
    local _last_word=$(
    (
        IFS=$'\ \t\n\0'
        eval "set -- $words[CURRENT]"
        echo ${argv[-1]}
    ))
    _tags files
    compstate[pattern_match]='*'
    local -a corrections
    if [[ $_last_word == '' ]];then
        corrections=( ${(f)${(s:\n:)"$(find . -maxdepth 1 -mindepth 1 -printf '%f\n')"}} )
    else
        corrections=( ${(f)${(s:\n:)"$(python3 ${_polLingua_python_path}/main_startswith.py $_last_word $PWD)"}})
    fi
    compadd -U "${corrections[@]}"
    return 0
}
