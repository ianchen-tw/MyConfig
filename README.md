# MyConfig
my unix config file

## Installation
#### Mac
1. install `Homebrew`
```sh
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
2. `brew install python3`
3. `python3 setup.py`

#### Freebsd
```sh
sudo pkg install python3
python3 setup.py
```
#### Ubuntu
```sh
sudo apt-get python3
python3 setup.py
```

## Config outline
#### Bash 
bash prompt (`PS1`) :

![Bash promt](./pic/my_bash_promt.png)
#### Vim

1. Plugin Manager : [`vim-plug`](https://github.com/junegunn/vim-plug)

###### key mapping
1. use `space` as `leader key`
2. type `jk` in insert mode is equal to `<ESC>`
 + casual keymapping
    + `<leader> - w` : change window
    + `<leader> - n` : Next opened file
    + `<leader> - p` : Previous opended file
 + plugins 
    + `<leader> - t` : toggle `Nerd tree`
    + `<leader> - e` : toggle `Buf explorer`
    + `<leader> - g` : toggle `Goyo`(zen mode) 
    + `F4`: toggle `tagbar`


## further Maunal configs
1. build `vim` with `lua` support in order to use vim plugin : [`Shougo/neocomplete`](https://github.com/Shougo/neocomplete.vim) 
