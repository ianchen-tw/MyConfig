import os
import config

def is_system( sys_name ):
    type_check( sys_name, 'sys_name', str)

    from subprocess import Popen, PIPE 
    proc = Popen(['uname','-v'], stdout=PIPE)
    system_info = proc.stdout.read().decode('utf-8')
    return sys_name.upper() in system_info.upper()


def type_check( arg,arg_name,target_type):
    if type(arg) is not target_type:
        raise TypeError('{} require to be {}'.format( arg_name, target_type))



def exists_program( program_name ):
    type_check( program_name, 'program_name', str)
    from shutil import which 
    return which(program_name) is not None 

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


os_dependent_names = config.os_dependent_names
for os_type in os_dependent_names.keys():
    if is_system(os_type):
        cur_system = os_dependent_names[os_type]
        bash_file = cur_system['bash_config_file']
        pkg_manager = cur_system['pkg_manager']
        pkg_install = cur_system['pkg_install']
        pkg_noconfirm = cur_system['pkg_noconfirm']
        sudo_install = cur_system['sudo_install']
        break

def install_program(program, no_confirm=False):
    '''Install specific program from exist package manager
        This function would ask user for installing
    '''
    type_check( program, 'program', str)
    if not exists_program(program):
        if no_confirm==True or user_confirm("Install {}? (yes/no) [no]:".format(program))is True:
            pkg_dict = { 'pkg':pkg_manager
                    ,'install':pkg_install
                    ,'noconfirm':pkg_noconfirm
                    ,'program':program 
                    }
            print("Installing {}...".format(program), end='')
            if sudo_install is True:
                os.system('sudo {pkg} {install} {noconfirm} {program}'.format(**pkg_dict))
            else:
                os.system('{pkg} {install} {noconfirm} {program}'.format(**pkg_dict))
            print("Done")
        else:
            exit(1)

def require_program(program):
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
        install_program(program)
    elif type(program) == list:
        installation_list = []
        for p in program:
            if not exists_program(p): installation_list.append(p) 
        warning_info(installation_list)
        for p in installation_list: install_program(p, no_confirm=True)
        
        
