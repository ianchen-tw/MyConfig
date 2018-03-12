from pathlib import Path #python3.5 required
from subprocess import Popen, PIPE

# default setting
#SETUP_DIR = Path.home()
global SETUP_DIR, CURDIR, HOMEDIR
SETUP_DIR = Path.cwd().parent
CURDIR = Path.cwd()
HOMEDIR = Path(SETUP_DIR)
# global vars would be setted later
global cur_system, sudo_install, system_name
global pkg_manager, pkg_install, pkg_noconfirm

#---------------
# User settings 
#---------------
global git_username, git_email
from .config import git_email
from .config import git_username


# --------------------
# Do not alter contents after this line
#---------------------

os_dependent_names = {
    'FreeBSD':{
        'pkg_manager':'pkg',
        'pkg_install':'install',
        'pkg_noconfirm':'--yes',
        'sudo_install':True,
        'bash_config_file':'.bash_profile',
        }
    ,'Darwin':{ # OSX
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
    ,'Manjaro':{
        'pkg_manager':'pacman',
        'pkg_install':'-S',
        'pkg_noconfirm':'--noconfirm',
        'sudo_install':True,
        'bash_config_file':'.bashrc'
        }
}

def init():
    ''' Initialize global variables
    '''
    #print("computing system type...")
    def is_system( sys_name ):
        from subprocess import Popen, PIPE 
        proc = Popen(['uname','-a'], stdout=PIPE)
        system_info = proc.stdout.read().decode('utf-8')
        return sys_name.upper() in system_info.upper()
    
    for os_type in os_dependent_names.keys():
        if is_system(os_type):
            global cur_system, sudo_install, system_name, bash_file
            global pkg_manager, pkg_install, pkg_noconfirm
            
            cur_system = os_dependent_names[os_type]
            bash_file = cur_system['bash_config_file']
            pkg_manager = cur_system['pkg_manager']
            pkg_install = cur_system['pkg_install']
            pkg_noconfirm = cur_system['pkg_noconfirm']
            sudo_install = cur_system['sudo_install']
            system_name = os_type
            break

init()
