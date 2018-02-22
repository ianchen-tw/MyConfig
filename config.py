# python 3.5
from pathlib import Path

# default setting
#SETUP_DIR = Path.home()
SETUP_DIR = Path.cwd().parent

os_dependent_names = {
    'FreeBSD':{
        'pkg_manager':'pkg',
        'pkg_install':'install',
        'pkg_noconfirm':'--yes',
        'sudo_install':True,
        'bash_config_file':'.bash_profile',
        }
    ,'Darwin':{
        'pkg_manager':'brew',
        'pkg_install':'install',
        'pkg_noconfirm':'', # not config yet
        'sudo_install':False,
        'bash_config_file':'.bash_profile',
        }
    ,'Ubuntu':{
        'pkg_manager':'apt',
        'pkg_install':'install',
        'pkg_noconfirm':'--assume-yes',
        'sudo_install':True,
        'bash_config_file':'.bash_profile',
        }
    ,'Arch':{
        'pkg_manager':'pacman',
        'pkg_install':'-S',
        'pkg_noconfirm':'--noconfirm',
        'sudo_install':True,
        'bash_config_file':'.bashrc'
        }
}



