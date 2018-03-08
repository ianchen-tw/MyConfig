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

sys.path.append("..")
import config


from util_functions import exists_program, user_confirm, require_program, install_program

#from setup import CURDIR
from pathlib import Path
CURDIR = Path.cwd()
#print( "pyinstaller cur dir:{}".format(Path.cwd()) )
from config import cur_system

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

            print("ROOT password is required for installing pip")
            python_ver = sys.version_info
            cur_py = "python{}.{}".format(python_ver.major, python_ver.minor)
            os.system("sudo -k {} {}/get-pip.py".format(cur_py,CURDIR))
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
        sp.run(['git','clone','https://github.com/pyenv/pyenv.git', '{home}/.pyenv'.format(home=config.HOMEDIR)])

def ask():
    def ask_and_store(program):
        if user_confirm("Install {}? (yes/no) [yes]:".format(program), default_ans="YES")is True:
            install_dict[program] = True
    if not exists_program( 'pip3' ):
        ask_and_store('pip3')
    ask_and_store('pipenv')
    ask_and_store('pyenv')

def install():
    if install_dict['pip3']:
        install_pip3()
    if install_dict['pipenv']:
        install_pipenv()
    if install_dict['pyenv']:
        install_pyenv()