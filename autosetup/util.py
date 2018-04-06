import os
import filecmp
import shutil
from shutil import which
from .globalinfo import sudo_install, pkg_manager, pkg_install, pkg_noconfirm


from pathlib import Path
def cp_with_backup( src_file, des_folder, bak_suffix='old', alter_name=None, ask_if_conflict=True):
    '''
        @scr_file : path to filename wich can be constructed by pathlib
        @des_folder : folder to copy to, must be a path to "folder" which doesn't have to exist

        @alter_name : give the new file anotehr name different form the original one
    '''
    if(os.path.isfile(des_folder)):
        raise('argument: des_folder must be a folder, not a filename')
    
    # create destnation directory if not exist
    os.makedirs( des_folder, exist_ok=True)

    src_file = Path(src_file)
    if not os.path.exists(src_file):
        raise FileNotFoundError( "file:{} not exist".format(src_file))
    des_folder = Path( des_folder )
    
    # Determine the output file name 
    des_filename = src_file.name if alter_name is None else alter_name    
     
    # output file name (with)
    if os.path.isdir(des_folder):
        des_file = Path( des_folder, des_filename)
    else:
        des_file = Path( des_folder.parents[0], des_filename)
    
    #print("srcfile:{src}, des_folder:{folder}, des_file:{des}".format(src=src_file, folder=des_folder, des=des_file))
    
    if des_file.exists():
        if filecmp.cmp( str(src_file), str(des_file) ) is False:
            # Files not the same, need to backup
            if ask_if_conflict is False or user_confirm("Already exist {}, overwrite it? (yes/no) [no]:"
                    .format(src_file.name))is True:
                print(" Back up: {oldfile} as: {oldfile}.{bak_suffix}"\
                        .format( oldfile=des_file, bak_suffix=bak_suffix))
                des_file.rename( "{}.{}".format(des_file,bak_suffix))
                print(" Create: {}".format(str(des_file)))
                shutil.copy2( str(src_file), str(des_file))
    else:
        print(" Create: {}".format(str(des_file)))
        shutil.copy2( str(src_file), str(des_file))

    
    # in python3.4
    # shutil don;t support implicit POSIXPath to string 
    


def type_check( arg,arg_name,target_type):
    if type(arg) is not target_type:
        raise TypeError('{} require to be {}'.format( arg_name, target_type))


def exists_program( program_name ):
    type_check( program_name, 'program_name', str)
    return bool(which(program_name)) 

def user_confirm( question, default_ans='NO' ):
    '''Return True if user say yes'''
    type_check( question, 'question', str)
    while True: 
        usr_ans = input(question).upper()
        if usr_ans == '':
            usr_ans = default_ans 

        if usr_ans not in ['YES','Y','NO','N']:
            print('Need to type yes/no')
            continue
        else:
            if usr_ans in ['YES', 'Y']:
                return True
            elif usr_ans in ['NO','N']:
                return False
            else:
                raise Exception("Internal Error, please check the source code")

def install_program(program, no_confirm=False, options=None):
    '''Install specific program from exist package manager
        This function would ask user for installing
    '''
    def install_single_program( program, no_confirm=no_confirm, options=None):
        if not exists_program(program):
            if no_confirm is True or user_confirm("Install {}? (yes/no) [no]:".format(program))is True:
                option_string = ''
                if options != None:
                    option_string = ' '.join(options)
                pkg_dict = { 'pkg':pkg_manager
                        ,'install':pkg_install
                        ,'noconfirm':pkg_noconfirm
                        ,'program':program
                        ,'opt_str': option_string
                        }
                print("Installing {}...".format(program), end='')
                if sudo_install is True:
                    os.system('sudo {pkg} {install} {noconfirm} {program} {opt_str}'.format(**pkg_dict))
                else:
                    os.system('{pkg} {install} {noconfirm} {program} {opt_str}'.format(**pkg_dict))
                print("Done")
            else:
                exit(1)
    if type(program) is str:
        install_single_program(program,no_confirm=no_confirm, options=options)
    elif type(program) is list:
        for p in program:
            install_program(p, no_confirm=no_confirm)
    else:
        raise("Undefined type")
    

def require_program(program, no_confirm=False):
    '''Install "Essential" program for installation
        Exit program if user refuse to install
        use pkg_maneger to install

        @program : program's name or List of program's name
    '''
    def warning_info(program_name):
        if( type(program_name) == list ):
            nname = ", ".join(program_name)
        print(" It seems that '{}' is not installed on this machine".format(nname))
        print("  {} is Needed in order to proceed installation".format(nname))
    if type(program) == str and not exists_program(program):
        warning_info(program)
        install_program(program,no_confirm=no_confirm)
    elif type(program) == list:
        installation_list = []
        for p in program:
            if not exists_program(p): installation_list.append(p)
        if installation_list != []:
            warning_info(installation_list)
            for p in installation_list: install_program(p, no_confirm=no_confirm)

        
if __name__ == "__main__":
    pass
