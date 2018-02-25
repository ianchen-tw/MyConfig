"""

This module is a set of my fish shell environment setup codes

usage: import this module and call install_fish_env()

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

def install_omf():
    if exists_program('fish') and user_confirm("Install omf - fish package manager (yes/no) [no]") is True:
        # install omf: fish package manager
        require_program('curl')
        url = "'https://get.oh-my.fish'"
        os.system("curl -Lsfk {} --output {}/install_omf.fish".format(url, config.CURDIR))
        print("Done")

        print("install omf in {}/.local/share/omf")
        print("configuratuion file is in {}/.config/omf")
        os.system("fish install_omf.fish \
                --noninteractive \
                --path={}/.local/share/omf \
                --config={}/.config/omf".format( config.HOMEDIR, config.HOMEDIR))

        print("install bobthefish theme...", end='')
        os.system('fish -c "omf install bobthefish"')
        print('Done')

def install_fish_env():
    install_fish()
    install_omf()
    