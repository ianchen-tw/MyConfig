"""

This module is a set of my vim environment setup codes

usage: import this module and call install_vim_env()

Todo:
    + install vim
    + vim-plug
    + install vim plugins
    + compile vim with lua, python support
    + vim executable under ~/bin/
"""

import sys
import os
import subprocess as sp
sys.path.append("..")
import config
import shutil
from util_functions import exists_program, user_confirm, require_program, install_program


# Environmanet settings
vim_info_get = False
vim_feature_table = {}
def parse_vim_feature():
    ''' parse vim --version into dictionary

        @return value: a dict of { "feature_name" -> True/False, ... }
    '''
    msg = sp.run(['vim','--version'], stdout=sp.PIPE, encoding='utf-8').stdout.split('\n')
    msg = msg[5:] # delete the starting lines 
    final_id = 0
    for line_idx,line in enumerate(msg):
        if ':' in line:
            final_id = line_idx
            break
    feature_lines = msg[:final_id] # delete the extra infomations
    features = []
    for line in feature_lines:
        features += line.split()
    feature_dict = {}
    for feature_str in features:
        support = {'+':True, '-':False}
        feature_dict[feature_str[1:]] = support[feature_str[0]] 
    return feature_dict

if vim_info_get is False:
    vim_feature_table = parse_vim_feature()
    vim_info_get = True

# -- Self define functions

def build_vim_from_source():
    sp.run(['git','clone','https://github.com/vim/vim.git'])
    os.chdir('./vim')
    sp.run(['./configure',
            '--with-features=huge',
            '--enable-multibyte',
            '--enable-luainterp=yes',
            '--enable-fail-if-missing', 
            '--prefix={HOME}'.format(HOME=config.HOMEDIR)])
    sp.run(['make', 'install' ,'clean'])
    os.chdir(os.pardir)
    shutil.rmtree('./vim')


def install_vim():
    ''' install vim
        must support installing from system pkg manager or self compiling
        OSX user can use brew 
    '''

    if not exists_program('vim'):
        install_program('vim')
    # exist vim, check specific feature support
    elif vim_feature_table['lua'] is False:
        print("**Current vim version is not compiled with lua support**")
        if user_confirm('Compile vim with lua support? (3~5 min required) (yes/no) [no] '):
            print("compile vim from source...")
            build_vim_from_source
            

def install_vim_plug():
# Vim Plugin manager
        # Use vim-plug as defualt plugin manager 
    print("Install vim-plug,(Plugin manager for vim)")
    require_program(['curl','git','vim'])
    
    os.system('curl -s -fLo {}/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'\
    .format(str(config.HOMEDIR)))

    print("Install and upgrade all vim plugins...",end='')
    # Update all Plugins
    require_program('vim')
    os.system('vim -E -c PlugInstall -c PlugClean -c q -c q')
    print("Done")


def install():
    install_vim()
    install_vim_plug()