abbr cls "clear"
abbr sl "ls"
alias cdd "cd $HOME/Desktop"
abbr cdf "fzf-cd-widget"

abbr py "python"
abbr python "python"

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
function loud_command 
  echo $argv[1]; and eval $argv[2]
end
function loud_ssh
  set --local user      $argv[1]
  set --local host      $argv[2]
  set --local host_alias $argv[3]
  if test "$host_alias" = ""
    loud_command "Login to $user@$host" "ssh $user@$host"
  else 
    loud_command "Login to $user@$host_alias" "ssh $user@$host"
  end
end
alias workstation  "loud_ssh  yachen1115  linux3.cs.nctu.edu.tw linux3"
alias workstation_bsd "loud_ssh yachen1115 bsd3.cs.nctu.edu.tw bsd3"
alias nctuplus "loud_ssh yachen1115 plus.nctu.edu.tw NCTU+"

# SSH with different port
function ian_NctuDesktop
  set -l myIP 140.113.68.205
  set -l myPort 22
  set -l userName ian
  echo "login to ian@nctu_desktop"
  ssh -Y $userName@$myIP -p $myPort
end

alias lxc 'echo "login to ian@ii.paga"; and ssh -X ian@ii.paga.moe -p 30000'


# Set fisher as default package manager
#   install fisher automatically
if not functions -q fisher
    set -q XDG_CONFIG_HOME; or set XDG_CONFIG_HOME ~/.config
    curl https://git.io/fisher --create-dirs -sLo $XDG_CONFIG_HOME/fish/functions/fisher.fish
    fish -c fisher
end
# pyenv
status --is-interactive && source (pyenv init -|psub)

# ============= Setup custom $PATH =======================
#set PATH /Library/Frameworks/Python.framework/Versions/3.5/bin $PATH
set -x PATH $HOME/bin $PATH


# ============= Bobthefish - user configuration ==========
set -g theme_color_scheme dracula
set -g theme_display_user yes
set -g theme_display_date yes
set -g theme_date_format "+%H:%M"
set -g theme_newline_cursor yes
set -g theme_nerd_fonts yes

