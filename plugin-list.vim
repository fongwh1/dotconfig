call plug#begin('~/.config/nvim/plugged/')

Plug 'junegunn/fzf.vim'
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }

" NERD Tree - tree explorer
" https://github.com/scrooloose/nerdtree
" http://usevim.com/2012/07/18/nerdtree/
" (loaded on first invocation of the command)
Plug 'scrooloose/nerdtree', { 'on': 'NERDTreeToggle' }

" nerdtree-git-plugin - show git status in NERD Tree
" https://github.com/Xuyuanp/nerdtree-git-plugin
Plug 'Xuyuanp/nerdtree-git-plugin'

" Excellent git wrapper
" https://github.com/tpope/vim-fugitive
Plug 'tpope/vim-fugitive'

" Tagbar
" https://github.com/majutsushi/tagbar
Plug 'majutsushi/tagbar'

" Airline
" status line beatifier
" Plug 'vim-airline/vim-airline'
" Plug 'vim-airline/vim-airline-themes'

" lightline status bar
Plug 'itchyny/lightline.vim'

call plug#end()

runtime! ./plugin-custom/*.vim
