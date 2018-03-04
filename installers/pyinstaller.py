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

def install_pip3():
    if not exists_program( 'pip3' ):
        if user_confirm("Install pip? (yes/no) [no]:")is True:
            require_program('curl')

            print("Downloading 'get-pip.py'...", end='')
            url = "'https://bootstrap.pypa.io/get-pip.py'"
            os.system("curl -sfk {} --output {}/get-pip.py".format(url, CURDIR))
            print("Done")

            print("ROOT password is required for installing pip")
            python_ver = sys.version_info
            cur_py = "python{}.{}".format(python_ver.major, python_ver.minor)
            os.system("sudo -k {} {}/get-pip.py".format(cur_py,CURDIR))
            print("Remove temporary file :'get-pip.py'")
            os.system("sudo rm -f {}/get-pip.py".format(CURDIR))
            print("Installed pip successfully")

def install_pipenv():
    ''' pipenv - the offcial python packaging tool
    '''
    if cur_system == 'Darwin': # OSX
        install_program('pipenv')
    else:
        sp.run(['pip','install','pipenv']);

def install_pyenv():
    ''' pyenv - controll different version of python interpreter
    Note: do not delete the git repo which cloned from remote
    '''
    if cur_system == 'Darwin':
        install_program('pyenv')
    else:
        sp.run(['git','clone','https://github.com/pyenv/pyenv.git', '{home}/.pyenv'.format(home=config.HOMEDIR)])

def install():
    install_pip3()
    install_pipenv()
    install_pyenv()