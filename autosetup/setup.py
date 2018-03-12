# main entry point for the autosetup system
# Setup tool from IanChen

import sys
import os, os.path
import filecmp
import shutil
import subprocess as sp

from .globalinfo import git_email, git_username

# Personal file
from . import globalinfo as config

from .globalinfo import CURDIR, HOMEDIR
from .globalinfo import bash_file
from .globalinfo import cur_system, sudo_install, system_name
from .globalinfo import pkg_manager, pkg_install, pkg_noconfirm

from .util import type_check, exists_program, user_confirm
from .util import install_program, require_program, cp_with_backup

from .installers import pyinstaller
from .installers import fishinstaller
from .installers import viminstaller

# Check python version
def check_python_version():
    if sys.version_info < (3,5):
        print("require Python 3.5 to run this code")
        print("run \"python3 setup.py\"")
        exit(1)

if sys.version_info.major >=3:
    from pathlib import Path # python3 only
    

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


    # Set git info
    print('[git user identity setting]')
    cur_git_user_name = sp.run(['git','config','user.name'], stdout=sp.PIPE, encoding='utf-8').stdout
    cur_git_email = sp.run(['git','config','user.email'], stdout=sp.PIPE, encoding='utf-8').stdout
    if cur_git_user_name != config.git_username:
        # change name
        sp.run(['git','config','--global','user.name',config.git_username])
    if cur_git_email != config.git_email:
        # change email 
        sp.run(['git','config','--global','user.email', config.git_email])


    print("Setup finished")
    show_batch()

if __name__ =="__main__":
    main()