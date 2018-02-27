"""

This module is a set of my fish shell environment setup codes

usage: import this module and call install()

Todo:
    + install fish
    + install omf
    + install theme : bobthefish
    + move setting files
"""
import sys
import os
sys.path.append("..")
import config
import subprocess as sp
from util_functions import exists_program, user_confirm, require_program, install_program
from util_functions import cp_with_backup

def install_fish():
    if not exists_program( 'fish' ):
    # For Ubuntu, the "Ubuntu project shift" is not up-to-date
    #  Add repo that maintained by the fish developers
        if config.system_name == 'Ubuntu':
            return_code = sp.Popen(\
                    ['sudo','add-apt-repository', 'ppa:fish-shell/release-2'],
                ).wait()
            print("return code = : {}".format(return_code))
            if return_code == 0:
                os.system("sudo apt-get update")
        install_program("fish")

def omf_exist_package( pkg_name ):
    '''Check if plugin exist in omf packcages 
        This function use multiple python version implementation for fun :)
    '''
    vinfo = sys.version_info[0:2]
    if vinfo < (3,5):
        queryps = sp.Popen([ 'fish', '-c', 'omf list'], stdout=sp.PIPE)
        msg = queryps.communicate()[0].decode("utf-8").split()
    elif vinfo == (3,5):
        # "run" function is added in 3.5
        msg = sp.run(['fish','-c','omf list'], stdout=sp.PIPE).stdout
        msg = msg.decode('utf-8').split()
    elif vinfo >= (3,6):
        # "encoding: arg is added in 3.6
        msg = sp.run(['fish','-c','omf list'], stdout=sp.PIPE, encoding='utf-8').stdout.split()
    
    return pkg_name in msg

def install_omf():
    if exists_program('fish'):
        if os.path.isdir('{home}/.config/omf'.format(home=config.HOMEDIR)):
            msg = "Found existing omf directory, reinstall it? (yes/no) [no]"
            if user_confirm(msg) is False:
                return
        elif user_confirm("Install omf - fish package manager (yes/no) [no]") is False:
            return 
        # install omf: fish package manager
        require_program('curl')
        url = "'https://get.oh-my.fish'"
        os.system("curl -Lsfk {} --output {}/install_omf.fish".format(url, config.CURDIR))
        print("Done")

        print("install omf in {}/.local/share/omf".format(config.HOMEDIR))
        print("configuratuion file is in {}/.config/omf".format(config.HOMEDIR ))
        os.system("fish install_omf.fish \
                --noninteractive \
                --path={}/.local/share/omf \
                --config={}/.config/omf".format( config.HOMEDIR, config.HOMEDIR))

        if not omf_exist_package('bobthefish'):
            print("install bobthefish theme...", end='')
            os.system('fish -c "omf install bobthefish"')
            print('Done')

def move_fish_cofig_file(fishdir, destdir):
    # fish functions
    from pathlib import Path
    dir_to_copy = ['functions','conf.d']
    for directory in dir_to_copy:
        #print('dir:'+directory)
        for file in os.listdir('{fishdir}/{dir}'.format(fishdir=fishdir, dir=directory)):
            #print('    file:'+str(Path(file)))
            print("destination: {}".format(destdir))
            cp_with_backup(src_file='{}/{}/{}'.format(fishdir, directory,file)
                        ,des_folder='{}/{}'.format(destdir,directory))

    #print(os.listdir(fishdir))

def install():
    install_fish()
    install_omf()
    move_fish_cofig_file(fishdir='./newfish', destdir='{home}/.config/fish/'.format(home=config.HOMEDIR))

if __name__ == "__main__":
    install()