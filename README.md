# dotconfig

## neovim
### install
```
git clone --depth 1 https://github.com/wbthomason/packer.nvim\
 ~/.local/share/nvim/site/pack/packer/start/packer.nvim


# ~/.config/nvim/lua/plugins.lua
return require('packer').startup(function()
  -- Packer can manage itself
  use 'wbthomason/packer.nvim'
	use 'FrenzyExists/aquarium-vim'
end)

# ~/.config/nvim/init.vim
lua require('plugins')

# open neovim
:PackerSync
```


