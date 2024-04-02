return {
	"catppuccin/nvim",
	lazy = false,
	name = "catppuccin",
	priority = 1000,
	config = function()
		vim.opt.termguicolors = true
		vim.cmd.colorscheme("catppuccin")
	end,
}
