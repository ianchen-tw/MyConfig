# color definition
set -g yellow ( set_color  yellow )
set -g red ( set_color  red )
set -g blue ( set_color  blue)
set -g green (set_color green)
set -g normal (set_color normal)
set -g brmagenta (set_color brmagenta)

function fish_prompt -d "Write out the prompt"
    

    # variables
    set -l cwd $green(prompt_pwd)$normal
    set -l cur_time $red(date +%H:%M)$normal

    # Git
    set -l git_branch $yellow" ("(git branch ^/dev/null | sed -n '/\* /s///p')") $normal"

    set -l is_ssh ''
    # SSH
    if test $SSH_CLIENT; or test $SSH_TTY;
        set is_ssh $brmagenta'SSH) '$yellow
    end

    echo -s $is_ssh $cwd $red ''  $git_branch $red ' ' $cur_time
    echo -s -n $blue '-> '$normal

end

function fish_right_prompt -d "Write out the right hand-side promt"
    set -l hostname $green(hostname|cut -d . -f 1)$normal
    set -l username $yellow(whoami)$normal
    echo -s -n $username  $yellow'@'$normal  $hostname
end


