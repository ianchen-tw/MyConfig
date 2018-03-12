# MyConfig

![Bash promt](./pic/my_bash_promt.png)

My unix configuration file, with auto-setup script inside

## Installation
```sh
git clone https://github.com/ianre657/MyConfig.git ~/MyConfig
cd ~/Myconfig
python3.6 -m autosetup
```

## Config outline

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
