# Setup tool for IanChen

import sys
import os, os.path
import subprocess as sp
import filecmp
import shutil

# Personal file
import config


#exit handler
import atexit

# Check python version
def check_python_version():
    if sys.version_info.major < 3:
        print("require Python 3 to run this code")
        print("run \"python3 setup.py\"")
        exit(1)
check_python_version()

if sys.version_info.major >=3:
    from pathlib import Path # python3 only

# Global Variables
CURDIR = Path.cwd()
HOMEDIR = Path(config.SETUP_DIR)

os_dependent_names = config.os_dependent_names

from util_functions import type_check, is_system, exists_program, user_confirm
from util_functions import install_program, require_program

def exit_handler():
    ''' Clean up temporary files 
    '''
    if os.path.isfile('./get-pip.py'):
        os.remove('./get-pip.py')
    if os.path.isfile('./install_omf.fish'):
        os.remove('./install_omf.fish')
atexit.register(exit_handler)


if __name__ =="__main__":
    print("Initializing")

    for os_type in os_dependent_names.keys():
        if is_system(os_type):
            cur_system = os_dependent_names[os_type]
            bash_file = cur_system['bash_config_file']
            pkg_manager = cur_system['pkg_manager']
            pkg_install = cur_system['pkg_install']
            pkg_noconfirm = cur_system['pkg_noconfirm']
            sudo_install = cur_system['sudo_install']
            system_name = os_type
            break

    #print("pkg_manager:{}".format(pkg_manager))


    # Copy files

    # bashrc
    #  bashrc is a special file that program should handle it specially
    #  because in OSX, some emulator use different config file, .bash_profile instead of .bashrc
    bashrc = Path('./bashrc')
    if (HOMEDIR/bash_file).exists():
        if filecmp.cmp( str(CURDIR/'bashrc'), str(HOMEDIR/bash_file))==False:
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
        if (HOMEDIR/filename).exists():
            if filecmp.cmp( str(CURDIR/'dotfiles'/filename), str(HOMEDIR/filename))==False:
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

    # Vim Plugin manager
        # Use vim-plug as defualt plugin manager 
    print("Install vim-plug,(Plugin manager for vim)")
    require_program('curl')
    require_program('git')
    
    os.system('curl -s -fLo {}/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'\
    .format(str(HOMEDIR)))

    print("Install and upgrade all vim plugins...",end='')
    # Update all Plugins
    require_program('vim')
    os.system('vim -E -c PlugInstall -c PlugClean -c q -c q')
    print("Done")

    install_program('tmux')

    print("Setup finished")
    print(r'''
    .___                _________ .__
    |   |____    ____   \_   ___ \|  |__   ____   ____
    |   \__  \  /    \  /    \  \/|  |  \_/ __ \ /    \
    |   |/ __ \|   |  \ \     \___|   Y  \  ___/|   |  \
    |___(____  /___|  /  \______  /___|  /\___  >___|  /
             \/     \/          \/     \/     \/     \/
    ''')

    if not exists_program( 'pip3' ):
        if user_confirm("Install pip? (yes/no) [no]:")is True:
            require_program('curl')

            print("Downloading 'get-pip.py'...", end='')
            url = "'https://bootstrap.pypa.io/get-pip.py'"
            os.system("curl -sfk {} --output {}/get-pip.py".format(url, CURDIR))
            print("Done")

            print("ROOT password is required for installing pip")
            python_ver = sys.version_info
            cur_py = "python{}.{}".format(python_ver.major, python_ver.minor)
            os.system("sudo -k {} {}/get-pip.py".format(cur_py,CURDIR))
            print("Remove temporary file :'get-pip.py'")
            os.system("sudo rm -f {}/get-pip.py".format(CURDIR))
            print("Installed pip successfully")
    

    if not exists_program( 'fish' ):
        # For Ubuntu, the "Ubuntu project shift" is not up-to-date
        #  Add repo that maintained by the fish developers
        if system_name == 'Ubuntu':
            return_code = sp.Popen(\
                    ['sudo','add-apt-repository', 'ppa:fish-shell/release-2'],
                ).wait()
            print("return code = : {}".format(return_code))
            if return_code == 0:
                os.system("sudo apt-get update")
            
        install_program("fish")

    # continue to config fish
    if exists_program('fish') and user_confirm("Install omf - fish package manager (yes/no) [no]") is True:
        # install omf: fish package manager
        require_program('curl')
        url = "'https://get.oh-my.fish'"
        os.system("curl -Lsfk {} --output {}/install_omf.fish".format(url, CURDIR))
        print("Done")

        print("install omf in {}/.local/share/omf")
        print("configuratuion file is in {}/.config/omf")
        os.system("fish install_omf.fish \
                --noninteractive \
                --path={}/.local/share/omf \
                --config={}/.config/omf".format( HOMEDIR, HOMEDIR))

        print("install bobthefish theme...", end='')
        os.system('fish -c "omf install bobthefish"'.format(HOMEDIR))
        print('Done')

        
        
        



