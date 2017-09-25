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

print("Initializing")

sysname = os.uname().sysname.upper()
HOMEDIR = Path.home()
#HOMEDIR = Path.cwd().parent
CURDIR = Path.cwd()


# bash file
if "Darwin".upper() in sysname:
    bash_file = ".bash_profile"
elif "FreeBSD".upper() in sysname:
    bash_file = ".bash_profile"
    pkg_manager = 'pacman'
else:
    bash_file = ".bashrc"
    os.system('mv {}/bash_profile {}/bashrc'.format(CURDIR,CURDIR))
    print("unknown system type, use .bashrc")

    

def program_exists( program_name ):
    if type( program_name ) is not str:
        raise TypeError('arg:program_name need to be string type')
    from shutil import which 
    return which(program_name) is not None 


if __name__ =="__main__":

    # Copy files
    for filename in [ bash_file, '.vimrc' ]:
        filename = Path(filename)
        # Copy files
        if (HOMEDIR/filename).exists() :
            if filecmp.cmp( str(CURDIR/filename) , str(HOMEDIR/filename) )==False:
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
    os.system('curl -s -fLo {}/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'\
    .format(str(HOMEDIR)))

    print("Install and upgrade all vim plugins")
    # Update all Plugins
    os.system('vim -E -c PlugInstall -c PlugClean -c q -c q')

    print("Setup finished")
    print(r'''
    .___                _________ .__
    |   |____    ____   \_   ___ \|  |__   ____   ____
    |   \__  \  /    \  /    \  \/|  |  \_/ __ \ /    \
    |   |/ __ \|   |  \ \     \___|   Y  \  ___/|   |  \
    |___(____  /___|  /  \______  /___|  /\___  >___|  /
             \/     \/          \/     \/     \/     \/
    ''')

    if not program_exists( 'pip3' ):

        while True:
            usr_ans = input( "Install pip? (yes/no) [no]:").upper()
            if usr_ans == '': usr_ans = 'N'

            if usr_ans not in ['YES','Y','NO','N']:
                continue
            else:
                if usr_ans in ['YES', 'Y']:
                    if not program_exists('curl'):
                        raise Exception('Need to install curl')
                    print("Downloading 'get-pip.py'...")
                    os.system("curl -sfk 'https://bootstrap.pypa.io/get-pip.py'\
                            --output {}/get-pip.py".format(CURDIR))

                    print("ROOT password is required to installing pip")
                    os.system("sudo -k python3 {}/get-pip.py".format(CURDIR))
                    print("Installed pip successfully")
                    print("Remove get-pip.py")
                    os.system("sudo rm {}/get-pip.py".format(CURDIR))
                    break

                elif usr_ans in ['NO','N']:
                    break




