"""

This module is a set of my vim environment setup codes

usage: import this module and call install_vim_env()

Todo:
    + install vim
    + vim-plug
    + install vim plugins
    + compile vim with lua, python support
    + vim executable under ~/bin/
"""

import sys
import os
sys.path.append("..")
import config
from util_functions import exists_program, user_confirm, require_program, install_program

def install_vim():
    ''' install vim
        must support installing from system pkg manager or self compiling
        OSX user can use brew 
    '''
    if not exists_program('vim'):
        install_program('vim')

def install_vim_plug():
# Vim Plugin manager
        # Use vim-plug as defualt plugin manager 
    print("Install vim-plug,(Plugin manager for vim)")
    require_program(['curl','git','vim'])
    
    os.system('curl -s -fLo {}/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'\
    .format(str(config.HOMEDIR)))

    print("Install and upgrade all vim plugins...",end='')
    # Update all Plugins
    require_program('vim')
    os.system('vim -E -c PlugInstall -c PlugClean -c q -c q')
    print("Done")

def install_vim_env():
    install_vim()
    install_vim_plug()