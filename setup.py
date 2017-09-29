# Setup tool for IanChen

# Check python version
def check_python_version():
    import sys #temporarily import sys module
    if sys.version_info.major < 3:
        print("require Python 3 to run this code")
        print("run \"python3 setup.py\"")
        exit(1)
check_python_version()

import os, os.path
import filecmp
import shutil
from pathlib import Path # python3 only 

# Global Variables
HOMEDIR = Path.home()
CURDIR = Path.cwd()

os_dependent_names = {
    'FreeBSD':{
        'pkg_manager':'pkg',
        'pkg_install':'install',
        'bash_config_file':'.bash_profile',
        }
    ,'Darwin':{
        'pkg_manager':'brew',
        'pkg_install':'install',
        'bash_config_file':'.bash_profile',
        }
    ,'Ubuntu':{
        'pkg_manager':'apt',
        'pkg_install':'install',
        'bash_config_file':'.bashrc',
        }
    ,'Arch':{
        'pkg_manager':'pacman',
        'pkg_install':'-S',
        'bash_config_file':'.bashrc'
        }
}

def type_check( arg,arg_name,target_type):
    if type(arg) is not target_type:
        raise TypeError('{} require to be {}'.format( arg_name, target_type))


def is_system( sys_name ):
    type_check( sys_name, 'sys_name', str)

    from subprocess import Popen, PIPE 
    proc = Popen(['uname','-v'], stdout=PIPE)
    system_info = proc.stdout.read().decode('utf-8')
    return sys_name.upper() in system_info.upper()

def exists_program( program_name ):
    type_check( program_name, 'program_name', str)
    from shutil import which 
    return which(program_name) is not None 

def user_confirm( question, default_ans='no' ):
    '''Return True if user say yes'''
    type_check( question, 'question', str)
    while True:
        usr_ans = input(question).upper()
        if usr_ans == '': usr_ans = default_ans 

        if usr_ans not in ['YES','Y','NO','N']:
            print('Need to type yes/no')
            continue
        else:
            if usr_ans in ['YES', 'Y']:
                return True
            elif usr_ans in ['NO','N']:
                return False
            else:
                raise Exception("Internal Error, please check the source code")

def require_program(program):
    '''Install "Essential" program for installation
        Exit program if user refuse to install
        use pkg_maneger to install 
    '''
    type_check( program, 'program', str)
    if not exists_program(program):
        print(" It seems that '{}' is not installed on this machine".format(program))
        print("  {} is Needed in order to proceed installation".format(program))
        if user_confirm("Install {}? (yes/no) [no]:".format(program))is True:
            pkg_dict = { 'pkg':pkg_manager
                    ,'install':pkg_install
                    ,'program':program 
                    }
            print("Installing {}...".format(program), end='')
            os.system('sudo {pkg} {install} {program}'.format(**pkg_dict))
            print("Done")
        else:
            exit(1)



if __name__ =="__main__":
    print("Initializing")


    bash_file = '.bash_profile'
    bash_file = '.bashrc'
    for os_type in os_dependent_names.keys():
        if is_system(os_type):
            cur_system = os_dependent_names[os_type]
            bash_file = cur_system['bash_config_file']
            pkg_manager = cur_system['pkg_manager']
            pkg_install = cur_system['pkg_install']
            break

    if bash_file is not ".bash_profile":
        os.system('mv {}/bash_profile {}/bashrc'.format(CURDIR,CURDIR))

    #print("pkg_manager:{}".format(pkg_manager))


    # Copy files
    for filename in [ bash_file, '.vimrc' ]:
        filename = Path(filename)
        # Copy files
        if (HOMEDIR/filename).exists():
            if filecmp.cmp( str(CURDIR/filename), str(HOMEDIR/filename))==False:
                # Files not the same, need to backup
                print("Back up: ~/{} as: ~/{}"\
                        .format(str(filename), str(filename)+'.old'))
                (HOMEDIR/filename).rename( str(HOMEDIR/filename)+'.old')

                print("Create: {}".format(filename))
                shutil.copy2( CURDIR/filename, HOMEDIR/filename)

        else:
            print("Create: {}".format(filename))
            shutil.copy2( CURDIR/filename, HOMEDIR/filename)

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
    os.system('vim -E -c PlugInstall -c PlugClean -c q -c q')
    print("Done")

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
            os.system("sudo -k python3 {}/get-pip.py".format(CURDIR))
            print("Remove temporary file :'get-pip.py'")
            os.system("sudo rm {}/get-pip.py".format(CURDIR))
            print("Installed pip successfully")


