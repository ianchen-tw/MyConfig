"""

This module is a set of my tmux environment setup codes

Todo:
    + install tmux
    + move tmux config file
"""

import sys
import os
import subprocess as sp
import shutil

from ..globalinfo import HOMEDIR, CURDIR
from ..globalinfo import system_name
from ..util import exists_program, user_confirm, install_program, cp_with_backup

install_dict = {
    'tmux':False,
}

def ask():
    if (not exists_program('tmux')) and user_confirm( "install tmux? (yes/no) [Yes]:", default_ans='YES' ):
        install_dict['tmux'] = True
        

def install():
    if install_dict['tmux']:
        install_program('tmux', no_confirm=True)
        cp_with_backup(src_file=CURDIR/'dotfiles/.tmux.conf',des_folder=HOMEDIR)

