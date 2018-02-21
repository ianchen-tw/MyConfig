" set foldmethod=marker foldlevel=0 

" ============================================================================
" vimrc of Ian Chen
" ============================================================================
" VIM-PLUG BLOCK {{{
" ============================================================================
" plugin manager: vim-plug
call plug#begin('~/.vim/plugged')


" neocomplete is a newer version, butvim should compiled with lua support
"Plug 'Shougo/neocomplete'
Plug 'Shougo/neocomplcache.vim'

Plug 'itchyny/lightline.vim'
"Plug 'vim-airline/vim-airline'
"Plug 'vim-airline/vim-airline-themes'
Plug 'scrooloose/nerdtree', { 'on': 'NERDTreeToggle'}
Plug 'jistr/vim-nerdtree-tabs'
Plug 'jlanzarotta/bufexplorer'
Plug 'majutsushi/tagbar',{ 'for': ['ruby','c','c++','python']}
Plug 'tpope/vim-rails' ,{ 'for':'ruby'}
Plug 'junegunn/goyo.vim'

"Colors
Plug 'tomasr/molokai'
Plug 'junegunn/seoul256.vim'
" Lang
if v:version >= 703
    Plug 'vim-ruby/vim-ruby'
endif

call plug#end()
" }}}
" ============================================================================
" BASIC SETTINGS {{{
" ============================================================================
let mapleader=" "
let maplocalleader=" "

syntax enable 		  " enable syntax processing
syntax on			  " open syntax coloring in vim 
scriptencoding=utf8
filetype indent on  "load filetype-specific indent files  , which under  ~/.vim/indent 
set number            " line numbers 
set autoindent 	      " auto-indent when key-int <CR> (carrage return)
set showcmd           " display incomplete commands
set visualbell
set backspace=indent,eol,start 
set mouse=a           " enable mouse in vim 
set history=1000	  " keep 1000 lines of command line history
set cursorline        " show current line 
set ruler 			  " show the cursor position all the time 
set wildmenu		  " visual autocomplete for command menu
set wildmode=full
set incsearch		  " do incremental search
set hlsearch 
set scrolloff=5         " minium nm. of line below and after cursor 
set virtualedit=block   " let corsor goes to Null spaces
set laststatus=2        " status line 
set noshowmode          " disabled cuz,used plugin to show mode 
set tabstop=4
set shiftwidth=4  
set expandtab smarttab
set list
set listchars=tab:\|\ ,
set autoread
set hidden      " switch buffer without saving
silent! set cryptmethod=blowfish2
hi Folded ctermbg=237	ctermfg=11
hi FoldColumn ctermbg=234 ctermfg=203 
"set foldmethod=syntax
set foldcolumn=3
set foldlevel=0

" 80 chars/line
set textwidth=0
if exists('&colorcolumn')
  set colorcolumn=81
  endif


" Colorscheme
if has('gui_running')
    set guifont=Menlo:h14 columns=80 lines=40
    silent! colorscheme seoul256-light
else
    silent! colorscheme seoul256
endif

" }}}
" ============================================================================
" MAPPINGS {{{
" ============================================================================


" Buffe Explorer
nnoremap <leader>e :BufExplorer<CR>

" Goyo
nnoremap <leader>g :Goyo<CR>

nnoremap <leader>t :NERDTreeToggle<CR>

nnoremap <leader>q :q<cr>
nnoremap <leader>s :w<cr>
nnoremap <leader>w :w<cr>

" Buffer
nnoremap ]b :bnext<cr>
nnoremap [b :bprev<cr>
nnoremap <Leader>n :bn<cr>
nnoremap <Leader>p :bp<cr>
nnoremap <Leader>d :bd<CR>
nnoremap <Leader>1 :b1<CR>
nnoremap <Leader>2 :b2<CR>
nnoremap <Leader>3 :b3<CR>
nnoremap <Leader>4 :b4<CR>
nnoremap <Leader>5 :b5<CR>

" jk | Escaping!
inoremap jk <Esc>

" Movement in insert mode
inoremap <C-h> <C-o>h
inoremap <C-l> <C-o>a
inoremap <C-j> <C-o>j
inoremap <C-k> <C-o>k

" add mark ';' after the last character in current line.  
nnoremap <tab> <c-w>W 
nnoremap <Leader>; mqA;<esc>'q 	

noremap <Leader>w <c-w><c-w>
noremap <Leader>o <c-w><c-o>

nnoremap <leader>ev :vsplit $MYVIMRC<cr> <c-w>o  
nnoremap <leader>sv :source $MYVIMRC<cr>

" Fix typo
iabbrev adn and
iabbrev incldue include
iabbrev incdleu include 
iabbrev inlcude include 

"}}}
" ============================================================================
" PULGIN SETTINGS {{{
" ============================================================================

" Lightline
let g:lightline = {
      \ 'colorscheme': 'seoul256',
      \ }

" Goyo
let g:goyo_width = 100


" Tagbar Settings -----
" toggle tagbar display
map <F4> :TagbarToggle<CR>
" " autofocus on tagbar open
let g:tagbar_autofocus = 1


" NeoComplCache--------
"most of them not documented because I'm not sure how they work
" (docs aren't good, had to do a lot of trial and error to make 
" it play nice)
let g:neocomplcache_enable_at_startup = 1
let g:neocomplcache_enable_ignore_case = 1
let g:neocomplcache_enable_smart_case = 1
let g:neocomplcache_enable_auto_select = 1
let g:neocomplcache_enable_fuzzy_completion = 0
let g:neocomplcache_enable_camel_case_completion = 1
let g:neocomplcache_enable_underbar_completion = 0
let g:neocomplcache_fuzzy_completion_start_length = 1
let g:neocomplcache_auto_completion_start_length = 1
let g:neocomplcache_manual_completion_start_length = 0
let g:neocomplcache_min_keyword_length = 1
let g:neocomplcache_min_syntax_length = 1
" complete with workds from any opened file
let g:neocomplcache_same_filetype_lists = {}
let g:neocomplcache_same_filetype_lists._ = '_'


" }}}
" ============================================================================



"=== from  'learn vimscript in a hard way '====
"visual select word
"nnoremap t viw 
nnoremap <leader>" viw<esc>a"<esc>hbi"<esc>lel
inoremap <c-d> <esc>ddi

" p = parameter,parenthesis
onoremap p i(

"===================== from  'learn vimscript in a hard way '====

noremap <F8> :w <CR> :!gcc % -Wall -o %:r<CR>
								 " %:r  Current file name without extension
noremap <F9> :w <CR> :!g++ -std=c++0x % -Wall -o %:r<CR>



"===== C & C++ ======
autocmd Filetype c nnoremap <localleader>c I//<esc> 
autocmd Filetype c,cpp nnoremap <leader>; A;<esc> 
