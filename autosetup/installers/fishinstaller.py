"""

This module is a set of my fish shell environment setup codes

usage: import this module and call install()

Todo:
    + install fish
    + install fisher
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
    'fisher': False,
}

def install_fish():
    # For Ubuntu, the "Ubuntu project shift" is not up-to-date
    #  Add repo that maintained by the fish developers
    if system_name == 'Ubuntu':
        return_code = sp.Popen(\
                ['sudo','add-apt-repository', 'ppa:fish-shell/release-2', '-y'],
            ).wait()
        print("return code = : {}".format(return_code))
        if return_code == 0:
            os.system("sudo apt-get update")
    install_program("fish",no_confirm=True)

def fisher_exist_package( pkg_name ):
    '''Check if plugin exist in fisher packcages 
        This function use multiple python version implementation for fun :)
    '''
    vinfo = sys.version_info[0:2]
    if vinfo < (3,5):
        queryps = sp.Popen([ 'fish', '-c', 'fisher ls'], stdout=sp.PIPE)
        msg = queryps.communicate()[0].decode("utf-8").split()
    elif vinfo == (3,5):
        # "run" function is added in 3.5
        msg = sp.run(['fish','-c','fisher ls'], stdout=sp.PIPE).stdout
        msg = msg.decode('utf-8').split()
    elif vinfo >= (3,6):
        # "encoding: arg is added in 3.6
        msg = sp.run(['fish','-c','fisher'], stdout=sp.PIPE, encoding='utf-8').stdout.split()
    
    return pkg_name in msg

def install_fisher():
    print("installing fisherman")
    if exists_program('fish'):
        # install fisher: fish package manager
        require_program('curl')
        
        fisher_success = True
        try:
            print("Installing Fisherman - the fish package manager...",end='')
            location = "{}/.config/fish/functions/fisher.fish".format( HOMEDIR)
            cmd= "curl -fLo {} --create-dirs https://git.io/fisher".format(location)
            os.system(cmd)
            print("Done")

            print("install fisher in {}".format(location))
        except:
            fisher_success = False
        finally:
            if fisher_success:
                print("Successfully installed fisherman")

        default_plugins = [ 'fzf', 'omf/theme-bobthefish', 'pyenv']
        plugins = ' '.join(default_plugins)
        os.system('fish -c "fisher {}"'.format(plugins))

def move_fish_cofig_file(fishdir, destdir,backup=True):
    # fish functions
    dir_to_copy = ['functions','conf.d']
    for directory in dir_to_copy:
        for file in os.listdir('{fishdir}/{dir}'.format(fishdir=fishdir, dir=directory)):
            cp_with_backup(src_file='{}/{}/{}'.format(fishdir, directory,file)
                        ,des_folder='{}/{}'.format(destdir,directory),ask_if_conflict=False,backup=backup)
   # move config.fish
    cp_with_backup(src_file='{}/config.fish'.format(fishdir)
                        ,des_folder='{}'.format(destdir),ask_if_conflict=True, backup=backup)
def ask():
    def is_fisher_installed():
        if os.path.isfile('{home}/.config/fish/functions/fisher.fish'.format(home=HOMEDIR)):
            return True
        else:
            return False

    if not exists_program( 'fish' ):
        if user_confirm("install fish shell - a command line shell for the 90s? (yes/no) [YES]", default_ans='YES') is True:            
            install_dict['fish'] = True
        # Check existing fisher 
        if install_dict['fish'] is True :
            if is_fisher_installed():
                if user_confirm('Found existing fisherman directory, reinstall it? (yes/no) [no]') is True:
                    install_dict['fisher'] = True
            elif user_confirm("Install fisher - fish package manager (yes/no) [YES]", default_ans='YES') is True:
                install_dict['fisher'] = True

    # user have fish installed already
    if exists_program('fish') and not is_fisher_installed():
        if  user_confirm("Install fisher - fish package manager (yes/no) [YES]", default_ans='YES') is True:
            install_dict['fisher'] = True

def install():
    if install_dict['fish'] is True:
        install_fish()
    if install_dict['fisher'] is True:
        install_fisher()
    move_fish_cofig_file(fishdir='./fish', destdir='{home}/.config/fish/'.format(home=HOMEDIR))

if __name__ == "__main__":
    ask()
    install()
