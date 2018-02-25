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
from util_functions import install_program, require_program

from installers import pyinstaller
from installers import fishinstaller
from installers import viminstaller

# Check python version
def check_python_version():
    if sys.version_info.major < 3:
        print("require Python 3 to run this code")
        print("run \"python3 setup.py\"")
        exit(1)

if sys.version_info.major >=3:
    from pathlib import Path # python3 only

def exit_handler():
    ''' Clean up temporary files 
    '''
    if os.path.isfile('./get-pip.py'):
        os.remove('./get-pip.py')
    if os.path.isfile('./install_omf.fish'):
        os.remove('./install_omf.fish')

# Global Variables
#CURDIR = Path.cwd()
#HOMEDIR = Path(config.SETUP_DIR)
os_dependent_names = config.os_dependent_names


def main():
    print("Initializing")
    check_python_version()
    atexit.register(exit_handler)
    
    #print("pkg_manager:{}".format(pkg_manager))

    # Copy files

    # bashrc
    #  bashrc is a special file that program should handle it specially
    #  because in OSX, some emulator use different config file, .bash_profile instead of .bashrc
    if (HOMEDIR/bash_file).exists():
        if filecmp.cmp( str(CURDIR/'bashrc'), str(HOMEDIR/bash_file)) is False:
            # Files not the same, need to backup
            if user_confirm("Already exist {}, overwrite it? (yes/no) [no]:"\
                    .format(bash_file))is True:
                print("Back up: ~/{} as: ~/{}"\
                        .format(str(bash_file), str(bash_file)+'.old'))
                (HOMEDIR/bash_file).rename( str(HOMEDIR/bash_file)+'.old')

            # in python3.4
            # shutil don;t support implicit POSIXPath to string 
            print("Create: {}".format(bash_file))
            shutil.copy2( str(CURDIR/'bashrc'), str(HOMEDIR/bash_file))

    else:
        print("Create: {}".format(bash_file))
        shutil.copy2( str(CURDIR/'bashrc'), str(HOMEDIR/bash_file))

    # other dotfiles
    for filename in [ '.vimrc' ]:
        filename = Path(filename)
        # Copy files
        if (HOMEDIR/filename).exists(): # pylint: disable=E1101
            if filecmp.cmp( str(CURDIR/'dotfiles'/filename), str(HOMEDIR/filename)) is False:
                # Files not the same, need to backup
                if user_confirm("Already exist {}, overwrite it? (yes/no) [no]:"\
                        .format(filename))is True:
                    print("Back up: ~/{} as: ~/{}"\
                            .format(str(filename), str(filename)+'.old'))
                    (HOMEDIR/filename).rename( str(HOMEDIR/'dotfiles'/filename)+'.old')

                # in python3.4
                # shutil don;t support implicit POSIXPath to string 
                print("Create: {}".format(filename))
                shutil.copy2( str(CURDIR/'dotfiles'/filename), str(HOMEDIR/filename))

        else:
            print("Create: {}".format(filename))
            shutil.copy2( str(CURDIR/'dotfiles'/filename), str(HOMEDIR/filename))


    install_program('tmux')

    pyinstaller.install_python_env()

    print("Setup finished")
    print(r'''
    .___                _________ .__
    |   |____    ____   \_   ___ \|  |__   ____   ____
    |   \__  \  /    \  /    \  \/|  |  \_/ __ \ /    \
    |   |/ __ \|   |  \ \     \___|   Y  \  ___/|   |  \
    |___(____  /___|  /  \______  /___|  /\___  >___|  /
             \/     \/          \/     \/     \/     \/
    ''')

if __name__ =="__main__":
    main()