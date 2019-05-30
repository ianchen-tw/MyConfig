#Update vim to 7.4. For  compatibility , just duplicate one and change the default path. 
#alias vim='/Users/chenyian/Editor/bin/vim  '

export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8

alias sslab='echo "login to yachen@sslab" && ssh -XY yachen@sslab.cs.nctu.edu.tw'
alias ian_NctuDesktop='echo "login to ian@nctu_desktop" && ssh -XY ian@140.113.68.205'
alias workstation='echo "Login to yachen1115..." && ssh yachen1115@linux3.cs.nctu.edu.tw '
alias workstation_bsd='echo "Login to yachen1115..." && ssh yachen1115@bsd3.cs.nctu.edu.tw '

#terminal colors 
alias grep='grep --color=auto'
alias ls='ls -G'
LS_COLORS="no=00:fi=00:di=01;34:ln=00;36:pi=40;33:so=00;35:bd=40;33;01:cd=40;33;01:or=01;05;37;41:mi=01;05;37;41:ex=00;32:*.cmd=00;3
2:*.exe=00;32:*.com=00;32:*.btm=00;32:*.bat=00;32:*.sh=00;32:*.csh=00;32:*.tar=00;31:*.tgz=00;31:*.arj=00;31:*.taz=00;31:*.lzh=00;31
:*.zip=00;31:*.z=00;31:*.Z=00;31:*.gz=00;31:*.bz2=00;31:*.bz=00;31:*.tz=00;31:*.rpm=00;31:*.cpio=00;31:*.jpg=00;35:*.gif=00;35:*.bmp
=00;35:*.xbm=00;35:*.xpm=00;35:*.png=00;35:*.tif=00;35:"
export LS_COLORS

# bash prompt 
export PS1="\[\e[0;32m\]\h\[\e[0;32m\]: \[\e[0;36m\]\W \[\e[0;31m\][ \[\e[0;33m\]\u \[\e[0;31m\]]  -- \A \n\[\e[0;31m\]$ \[\e[0m\]"


# intructions shortcut
alias cdd='cd ~/Desktop'
alias cls='clear'        
alias sl='ls'
alias e='echo'
alias g++='g++ -std=c++11'
alias py='python3'


#[[ -s "$HOME/.rvm/scripts/rvm" ]] && source "$HOME/.rvm/scripts/rvm" # Load RVM into a shell session *as a function*

# Add usr sapce command
PATH="$HOME/bin:/usr/local/sbin:${PATH}"
export PATH


# GVM : Golang version manager
source /Users/chenyian/.gvm/scripts/gvm

# javaCC java compiler compiler
export PATH="${HOME}/javacc-6.0/bin/:$PATH"

export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
if command -v pyenv 1>/dev/null 2>&1; then
    eval "$(pyenv init -)"
fi
