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
import autosetup.config as config
import shutil
from ..util_functions import exists_program, user_confirm, require_program, install_program

# Environmanet settings
vim_info_get = False
vim_feature_table = {}

install_dict = {
    'vim':False,
    'vim_build_from_source':False,
    'vim_plug': False,
}

def parse_vim_feature():
    ''' parse vim --version into dictionary

        @return value: a dict of { "feature_name" -> True/False, ... }
    '''
    msg = sp.run(['vim','--version'], stdout=sp.PIPE, encoding='utf-8').stdout.split('\n')
    for line_id,line in enumerate(msg):
        if line.startswith('+'):
            msg = msg[line_id:]
            break
    #msg = msg[5:] # delete the starting lines 
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

if exists_program('vim') and vim_info_get is False:
    vim_feature_table = parse_vim_feature()
    vim_info_get = True

# -- Self define functions

def install_vim_build_from_source():
    require_program('git')

    if config.system_name == 'Ubuntu':
        install_program(['lua5.2','liblua5.2-dev'], no_confirm=True)

    build_vim_success = True
    # os.chdir is not a good way because exceptrion may occur
    try:
        sp.run(['git','clone','https://github.com/vim/vim.git', 'vim_src'])
        os.chdir('./vim_src')
        sp.run(['./configure',
                '--with-features=huge',
                '--enable-multibyte',
                '--enable-luainterp=yes',
                '--enable-fail-if-missing', 
                '--prefix={HOME}'.format(HOME=config.HOMEDIR)])
        sp.run(['make', 'install' ,'clean'])
        os.chdir(os.pardir)
    except:
        build_vim_success = False
    finally:
        if os.path.isdir('./vim_src'):
            shutil.rmtree('./vim_src')
        if build_vim_success:
            print("Compile vim Successfully.")
        else:
            print("Failed to compile vim")

def install_vim_pkg_manager():
    ''' install vim from client's package manager
    '''
    if not exists_program('vim'):
        install_program('vim',no_confirm=True)            

def install_vim_plug():
    ''' script  to install vim-plug 
    '''
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


def ask():
    if (not exists_program('vim')) and user_confirm( "install vim? (yes/no) [Yes]:", default_ans='YES' ):
        install_dict['vim'] = True
        if user_confirm('compile vim wiht lua support? (this would add a directory to ~/bin/vim) (yes/no) [No]:'):
            install_dict['vim_build_from_source'] = True
    if exists_program('vim') and vim_feature_table['lua'] is False:
        print("Vim is installed but not compiled with lua support")
        if user_confirm('compile vim wiht lua support? (this would add a directory to ~/bin/vim) (yes/no) [No]:'):
            install_dict['vim'] = True
            install_dict['vim_build_from_source'] = True
    if install_dict['vim'] is True:
        if user_confirm('Install vim-plug,(Plugin manager for vim) (yes/no) [yes]', default_ans='YES'):
            install_dict['vim_plug'] = True

def install():
    if install_dict['vim_build_from_source']:
        install_vim_build_from_source()
    elif install_dict['vim']:
        install_vim_pkg_manager()

    if install_dict['vim_plug'] is True:
        install_vim_plug()

if __name__ == "__main__":
    parse_vim_feature()
    import pprint
    pprint.pprint(vim_feature_table)