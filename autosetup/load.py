from .config import import_dir
from .util import cp_with_backup

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

  move_fish_cofig_file(fishdir=home/'.config/fish', destdir=CURDIR/'fish')
  
if __name__ =='__main__':
  main()