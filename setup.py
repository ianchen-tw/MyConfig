# Setup tool for IanChen

import sys
import os, os.path
import filecmp
import shutil
import atexit

# Personal file
import config

from config import CURDIR, HOMEDIR
from config import bash_file
from config import cur_system, sudo_install, system_name
from config import pkg_manager, pkg_install, pkg_noconfirm

from util_functions import type_check, exists_program, user_confirm
from util_functions import install_program, require_program, cp_with_backup

from installers import pyinstaller
from installers import fishinstaller
from installers import viminstaller

# Check python version
def check_python_version():
    if sys.version_info < (3,5):
        print("require Python 3.5 to run this code")
        print("run \"python3 setup.py\"")
        exit(1)

if sys.version_info.major >=3:
    from pathlib import Path # python3 only

def exit_handler():
    ''' Clean up temporary files 
    '''
    #pyinstaller.py
    if os.path.isfile('./get-pip.py'):
        os.remove('./get-pip.py')

    if os.path.isfile('./install_omf.fish'):
        os.remove('./install_omf.fish')

    # viminstaller.py
    if os.path.isdir('./vim_src'):
        shutil.rmtree('./vim_src')
    

os_dependent_names = config.os_dependent_names

def show_batch():
    print(r'''
        .___                _________ .__
        |   |____    ____   \_   ___ \|  |__   ____   ____
        |   \__  \  /    \  /    \  \/|  |  \_/ __ \ /    \
        |   |/ __ \|   |  \ \     \___|   Y  \  ___/|   |  \
        |___(____  /___|  /  \______  /___|  /\___  >___|  /
                \/     \/          \/     \/     \/     \/
        ''')

def main():
    print("Initializing")
    check_python_version()
    atexit.register(exit_handler)

    # bashrc
    #  bashrc is a special file that program should handle it specially
    #  because in OSX, some emulator use different config file, .bash_profile instead of .bashrc
    cp_with_backup( src_file='./bashrc',des_folder=str(HOMEDIR), alter_name=bash_file)

    # other dotfiles
    for filename in [ '.vimrc' ]:
        filename = Path(filename)
        cp_with_backup(src_file=CURDIR/'dotfiles'/filename,des_folder=HOMEDIR)

    install_program('tmux')
    require_program(['curl','git'])

    # ask to install
    viminstaller.ask()
    pyinstaller.ask()
    fishinstaller.ask()

    # install

    viminstaller.install()
    pyinstaller.install()
    fishinstaller.install()

    print("Setup finished")
    show_batch()

if __name__ =="__main__":
    main()