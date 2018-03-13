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
import subprocess as sp

from ..globalinfo import HOMEDIR, CURDIR, system_name
from ..util import exists_program, user_confirm, require_program, install_program
from ..util import cp_with_backup

install_dict = {
    'fish': False,
    'omf': False,
}

def install_fish():
    # For Ubuntu, the "Ubuntu project shift" is not up-to-date
    #  Add repo that maintained by the fish developers
    if system_name == 'Ubuntu':
        return_code = sp.Popen(\
                ['sudo','add-apt-repository', 'ppa:fish-shell/release-2'],
            ).wait()
        print("return code = : {}".format(return_code))
        if return_code == 0:
            os.system("sudo apt-get update")
    install_program("fish",no_confirm=True)

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
    print("installing omf")
    if exists_program('fish'):
        # install omf: fish package manager
        require_program('curl')
        
        omf_success = True
        try:
            print("Installing omf - the fish package manager...",end='')
            url = "'https://get.oh-my.fish'"
            os.system("curl -Lsfk {} --output {}/install_omf.fish".format(url, CURDIR))
            print("Done")

            print("install omf in {}/.local/share/omf".format(HOMEDIR))
            print("configuratuion file is in {}/.config/omf".format(HOMEDIR ))
            os.system("fish install_omf.fish \
                    --noninteractive \
                    --path={}/.local/share/omf \
                    --config={}/.config/omf".format( HOMEDIR, HOMEDIR))
        except:
            omf_success = False
        finally:
            if os.path.isfile('{}/install_omf.fish'.format(CURDIR)):
                os.remove('{}/install_omf.fish'.format(CURDIR))
            if omf_success:
                print("Successfully installed omf")

        if not omf_exist_package('bobthefish'):
            print("install bobthefish theme...", end='')
            os.system('fish -c "omf install bobthefish"')
            print('Done')

def move_fish_cofig_file(fishdir, destdir):
    # fish functions
    dir_to_copy = ['functions','conf.d']
    for directory in dir_to_copy:
        for file in os.listdir('{fishdir}/{dir}'.format(fishdir=fishdir, dir=directory)):
            cp_with_backup(src_file='{}/{}/{}'.format(fishdir, directory,file)
                        ,des_folder='{}/{}'.format(destdir,directory),ask_if_conflict=False)

def ask():
    def is_omf_installed():
        if os.path.isdir('{home}/.config/omf'.format(home=HOMEDIR)):
            return True
        else:
            return False

    if not exists_program( 'fish' ):
        if user_confirm("install fish shell - a command line shell for the 90s? (yes/no) [YES]", default_ans='YES') is True:            
            install_dict['fish'] = True
        # Check existing omf 
        if install_dict['fish'] is True :
            if is_omf_installed():
                if user_confirm('Found existing omf directory, reinstall it? (yes/no) [no]') is True:
                    install_dict['omf'] = True
            elif user_confirm("Install omf - fish package manager (yes/no) [YES]", default_ans='YES') is True:
                install_dict['omf'] = True

    # user have fish installed already
    if exists_program('fish') and not is_omf_installed():
        if  user_confirm("Install omf - fish package manager (yes/no) [YES]", default_ans='YES') is True:
            install_dict['omf'] = True

def install():
    if install_dict['fish'] is True:
        install_fish()
        move_fish_cofig_file(fishdir='./fish', destdir='{home}/.config/fish/'.format(home=HOMEDIR))
    if install_dict['omf'] is True:
        install_omf()

if __name__ == "__main__":
    ask()
    install()