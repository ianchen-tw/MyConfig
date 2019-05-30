" set foldmethod=marker foldlevel=0 

" ============================================================================
" vimrc of Ian Chen
" ============================================================================
" VIM-PLUG BLOCK {{{
" ============================================================================
" plugin manager: vim-plug
call plug#begin('~/.vim/plugged')

"Plug 'Shougo/neocomplcache.vim'
Plug 'Shougo/neocomplete.vim'
"Plug 'itchyny/lightline.vim'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'scrooloose/nerdtree', { 'on': 'NERDTreeToggle'}
Plug 'jlanzarotta/bufexplorer'
Plug 'jistr/vim-nerdtree-tabs'
Plug 'majutsushi/tagbar',{ 'for': ['ruby','c','cpp','c++', 'python']}
"Plug 'tpope/vim-rails' ,{ 'for':'ruby'}
Plug 'junegunn/goyo.vim'
Plug 'junegunn/fzf', { 'dir': '~/.fzf', 'do': './install --all' }

"Plug 'dag/vim-fish', { 'for': ['fish', 'sh']}


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
set clipboard=unnamed
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
    silent! colorscheme seoul256
else
    silent! colorscheme seoul256
endif

" }}}
" ============================================================================
" MAPPINGS {{{
" ============================================================================


" Buffer Explorer
nnoremap <leader>e :BufExplorer<cr>

" Goyo
nnoremap <leader>g :Goyo<cr>

nnoremap <leader>t :NERDTreeToggle<CR>
nnoremap <leader>q  :q<cr>
nnoremap <leader>s  :update<cr>
nnoremap <leader>w  :update<cr>
nnoremap <c-s>      :update<cr>
nnoremap <c-w>      :update<cr>

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

" nnoremap <leader>ev :vsplit $MYVIMRC<cr> <c-w>o  
" nnoremap <leader>sv :source $MYVIMRC<cr>

" Fix typo
iabbrev adn and
iabbrev incldue include
iabbrev incdleu include 
iabbrev inlcude include 

"}}}
" ============================================================================
" PULGIN SETTINGS {{{
" ============================================================================

" Airline
let g:airline#extensions#tabline#enabled = 1
" Airline theme
let g:airline_theme='bubblegum'
let g:airline_extensions=['tabline']

" Goyo
let g:goyo_width = 100


" Lightline
"let g:lightline = {
"      \ 'colorscheme': 'seoul256',
"      \ }


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



" NeoComplete--------
" Disable AutoComplPop.
let g:acp_enableAtStartup = 0
" Use neocomplete.
let g:neocomplete#enable_at_startup = 1
" Use smartcase.
let g:neocomplete#enable_smart_case = 1
" Set minimum syntax keyword length.
let g:neocomplete#sources#syntax#min_keyword_length = 3

" Define dictionary.
let g:neocomplete#sources#dictionary#dictionaries = {
    \ 'default' : '',
    \ 'vimshell' : $HOME.'/.vimshell_hist',
    \ 'scheme' : $HOME.'/.gosh_completions'
        \ }

" Define keyword.
if !exists('g:neocomplete#keyword_patterns')
    let g:neocomplete#keyword_patterns = {}
endif
let g:neocomplete#keyword_patterns['default'] = '\h\w*'

" Plugin key-mappings.
inoremap <expr><C-g>     neocomplete#undo_completion()
inoremap <expr><C-l>     neocomplete#complete_common_string()

" Recommended key-mappings.
" <CR>: close popup and save indent.
inoremap <silent> <CR> <C-r>=<SID>my_cr_function()<CR>
function! s:my_cr_function()
  return (pumvisible() ? "\<C-y>" : "" ) . "\<CR>"
  " For no inserting <CR> key.
  "return pumvisible() ? "\<C-y>" : "\<CR>"
endfunction
" <TAB>: completion.
inoremap <expr><TAB>  pumvisible() ? "\<C-n>" : "\<TAB>"
" <C-h>, <BS>: close popup and delete backword char.
inoremap <expr><C-h> neocomplete#smart_close_popup()."\<C-h>"
inoremap <expr><BS> neocomplete#smart_close_popup()."\<C-h>"
" Close popup by <Space>.
"inoremap <expr><Space> pumvisible() ? "\<C-y>" : "\<Space>"

" AutoComplPop like behavior.
"let g:neocomplete#enable_auto_select = 1

" Shell like behavior(not recommended).
"set completeopt+=longest
"let g:neocomplete#enable_auto_select = 1
"let g:neocomplete#disable_auto_complete = 1
"inoremap <expr><TAB>  pumvisible() ? "\<Down>" : "\<C-x>\<C-u>"

" Enable omni completion.
autocmd FileType css setlocal omnifunc=csscomplete#CompleteCSS
autocmd FileType html,markdown setlocal omnifunc=htmlcomplete#CompleteTags
autocmd FileType javascript setlocal omnifunc=javascriptcomplete#CompleteJS
autocmd FileType python setlocal omnifunc=pythoncomplete#Complete
autocmd FileType xml setlocal omnifunc=xmlcomplete#CompleteTags

" Enable heavy omni completion.
if !exists('g:neocomplete#sources#omni#input_patterns')
  let g:neocomplete#sources#omni#input_patterns = {}
endif
"let g:neocomplete#sources#omni#input_patterns.php = '[^. \t]->\h\w*\|\h\w*::'
"let g:neocomplete#sources#omni#input_patterns.c = '[^.[:digit:] *\t]\%(\.\|->\)'
"let g:neocomplete#sources#omni#input_patterns.cpp = '[^.[:digit:] *\t]\%(\.\|->\)\|\h\w*::'

" For perlomni.vim setting.
" https://github.com/c9s/perlomni.vim
let g:neocomplete#sources#omni#input_patterns.perl = '\h\w*->\h\w*\|\h\w*::'

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


"===== Python
augroup PythonGroupSetting
  autocmd FileType python setlocal expandtab shiftwidth=2 tabstop=2 smartindent cinwords=if,elif,else,for,while,try,except,finally,def,class,with
augroup END

"===== C & C++ ======
autocmd Filetype c nnoremap <localleader>c I//<esc> 
autocmd Filetype c,cpp nnoremap <leader>; A;<esc> 
