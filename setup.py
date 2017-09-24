# Setup tool for IanChen

import os, os.path
import filecmp
from pathlib import Path
import shutil


print("Initializing")

sysname = os.uname().sysname.upper()

HOMEDIR = Path.home()
#HOMEDIR = Path.cwd().parent
CURDIR = Path.cwd()
print( "Home dir ={}".format(HOMEDIR))


# bash file
if "Darwin".upper() in sysname:
    bash_file = ".bash_profile"
elif "FreeBSD".upper() in sysname:
    bash_file = ".bash_profile"
else:
    print("unknown system type")
    exit(1)

def install_vim_plugin():
    os.system('vim -E  -c PlugInstall -c PlugClean -c q -c q')
    


if __name__ =="__main__":

    # Copy files
    for filename in [ bash_file, '.vimrc' ]:
        filename = Path(filename)
        # Copy files
        if (HOMEDIR/filename).exists() :
            if filecmp.cmp( CURDIR/filename , HOMEDIR/filename )==False:
                # Files not the same, need to backup
                print("Back up: ~/{} as: ~/{}".format(str(filename), str(filename)+'.old'))
                (HOMEDIR/filename).rename( str(HOMEDIR/filename)+'.old')

                print("Create: {}".format(filename))
                shutil.copy2( CURDIR/filename, HOMEDIR/filename)

        else:
            print("Create: {}".format(filename))
            shutil.copy2( CURDIR/filename, HOMEDIR/filename)

    # Vim Plugin manager
        # Use vim-plug as defualt plugin manager 
    print("Install vim-plug,(Plugin manager for vim)")
    os.system('curl -fLo {}/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'.format(str(HOMEDIR)))

    print("Install and upgrade all vim plugins")
    # Update all Plugins
    install_vim_plugin()

    print("Setup finished")
    print(r'''
    .___                _________ .__
    |   |____    ____   \_   ___ \|  |__   ____   ____
    |   \__  \  /    \  /    \  \/|  |  \_/ __ \ /    \
    |   |/ __ \|   |  \ \     \___|   Y  \  ___/|   |  \
    |___(____  /___|  /  \______  /___|  /\___  >___|  /
             \/     \/          \/     \/     \/     \/
    ''')
