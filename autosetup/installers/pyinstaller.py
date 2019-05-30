"""

This module is a set of my python environment setup codes

usage: import this module and call install()

Todo:
    + pyenv: for using multiple pyhton version
    + pip:
    + virtualenv or venv
    + install my usually used pips
    + jupyter setup

"""
import sys
import os
import subprocess as sp

from ..globalinfo import HOMEDIR, CURDIR
from ..globalinfo import cur_system
from ..util import exists_program, user_confirm, require_program, install_program


install_dict ={
    'pip3' : False,
    'pipenv': False,
    'pyenv': False,
}

def install_pip3():
    if not exists_program( 'pip3' ):
        require_program('curl')
        pip_success = True
        try:
            print("Downloading 'get-pip.py'...", end='')
            url = "'https://bootstrap.pypa.io/get-pip.py'"
            os.system("curl -sfk {} --output {}/get-pip.py".format(url, CURDIR))
            print("Done")

            python_ver = sys.version_info
            cur_py = "python{}.{}".format(python_ver.major, python_ver.minor)
            os.system("sudo {} {}/get-pip.py".format(cur_py,CURDIR))
        except:
            pip_success = False
        finally:
            print("Remove temporary file :'get-pip.py'")
            os.system("sudo rm -f {}/get-pip.py".format(CURDIR))
        if pip_success:
            print("Installed pip successfully")

def install_pipenv():
    ''' pipenv - the offcial python packaging tool
    '''
    if cur_system == 'Darwin': # OSX
        install_program('pipenv')
    else:
        sp.run(['pip','install','--user','pipenv']);

def install_pyenv():
    ''' pyenv - controll different version of python interpreter
    Note: do not delete the git repo which cloned from remote
    '''
    if cur_system == 'Darwin':
        install_program('pyenv')
    else:
        sp.run(['git','clone','https://github.com/pyenv/pyenv.git', '{home}/.pyenv'.format(home=HOMEDIR)])

def ask():
    def ask_and_store(program):
        if user_confirm("Install {}? (yes/no) [yes]:".format(program), default_ans="YES")is True:
            install_dict[program] = True
    def empty_dir(directory):
        if os.listdir(directory)== []:
            return True
        else:
            return False 

    if not exists_program( 'pip3' ):
        ask_and_store('pip3')
    if install_dict['pip3'] is True and not exists_program('pipenv'):
        ask_and_store('pipenv')
    
    pyenv_dir = '{home}.pyenv'.format(home=HOMEDIR)
    if os.path.isdir( pyenv_dir) and not empty_dir(pyenv_dir):
        if user_confirm( 'pyenv : found an existing dir, overwrite it? (yes/no) [NO]',default_ans="NO")is True:
            install_dict['pyenv'] = True
        else:
            ask_and_store('pyenv')

def install():
    if install_dict['pip3']:
        install_pip3()
    if install_dict['pipenv']:
        install_pipenv()
    if install_dict['pyenv']:
        install_pyenv()
