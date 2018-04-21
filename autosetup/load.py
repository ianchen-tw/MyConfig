import os

from .config import import_dir
from .util import cp_with_backup, user_confirm

from pathlib import Path
from .globalinfo import CURDIR
from .globalinfo import bash_file

from .installers.fishinstaller import move_fish_cofig_file

home=Path(import_dir)

def main():

  # dotfiles
  for file in ['.vimrc','.tmux.conf', bash_file]:
    if file==bash_file:
      alter_name = '.bash_profile'
    else:
      alter_name = None
    try:
      cp_with_backup(src_file=home/file,des_folder=CURDIR/'dotfiles')
    except FileNotFoundError:
      print("ERROR : cannot find file {}".format(home/file))
  load_fish_configs()


def load_fish_configs():
  move_fish_cofig_file(fishdir=home/'.config/fish', destdir=CURDIR/'fish')
  
  # delete file in package but not currently in user's configuration directories
  dir_to_copy = ['functions','conf.d']
  for directory in dir_to_copy:
    for dest_file in os.listdir( f'{CURDIR}/fish/{directory}' ):
      if not os.path.isfile(f'{home}/.config/fish/{directory}/{dest_file}'):
        print(f"File:{CURDIR}/fish/{directory}/{dest_file}")
        print(f"  exist in target dir but not in src dir:{home}/.config/fish/{directory}")
        if user_confirm('>> delete this file? (yes/no) [no]:')is True:
          os.remove(f'{CURDIR}/fish/{directory}/{dest_file}')


if __name__ =='__main__':
  main()