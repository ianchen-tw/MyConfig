alias cls "clear"
alias cdd "cd $HOME/Desktop"
alias cdf "fzf-cd-widget"

alias py "python"
alias python3 "python3.5"
alias python "python3"
alias python3.6 "python3.6-32"


# ===========================
# ███████╗ ███████╗ ██╗  ██╗
# ██╔════╝ ██╔════╝ ██║  ██║
# ███████╗ ███████╗ ███████║
# ╚════██║ ╚════██║ ██╔══██║
# ███████║ ███████║ ██║  ██║
# ╚══════╝ ╚══════╝ ╚═╝  ╚═╝
# ===========================
# SSH login configuration
#  loud_ssh : ~./config/fish/functions/loud_ssh.fish
#   |- description : Setup ssh connection LOUDLY ( only use port 22)
#   |- usage : <username> <host> <host_alias(optional)>
alias workstation  "loud_ssh  yachen1115  linux3.cs.nctu.edu.tw linux3"
alias workstation_bsd "loud_ssh yachen1115 bsd3.cs.nctu.edu.tw bsd3"
alias nctuplus "loud_ssh yachen1115 plus.nctu.edu.tw NCTU+"

# SSH with different port
alias ian_NctuDesktop 'echo "login to ian@nctu_desktop"; and ssh ian@140.113.67.102 -p 8022'



# ============= Setup custom $PATH =======================
set PATH /Library/Frameworks/Python.framework/Versions/3.5/bin $PATH
set PATH $HOME/bin $PATH


# ============= Bobthefish - user configuration ==========
set -g theme_display_user yes
set -g theme_display_date yes
set -g theme_date_format "+%H:%M"
set -g theme_newline_cursor yes
set -g theme_nerd_fonts yes
set -g theme_color_scheme base-16
#set -g theme_display_hostname yes
set -g theme_color_scheme dark

rvm default
