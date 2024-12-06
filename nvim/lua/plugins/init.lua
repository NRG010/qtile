return {
  {
    "stevearc/conform.nvim",
    event = "BufWritePre",
    opts = require "configs.conform",
  },

  {
    "neovim/nvim-lspconfig",
    config = function()
      require "configs.lspconfig"
    end,
  },

  {
    "nvim-treesitter/nvim-treesitter",
    opts = {
      ensure_installed = {
        "vim",
        "lua",
        "vimdoc",

        "c",
        "cpp",
        "rust",

        "bash",
        "fish",

        "python",
      },
    },
  },

  {
    "mrcjkb/rustaceanvim",
    version = "^5",
    lazy = true,
  },

  {
    "mfussenegger/nvim-lint",
    event = "BufWritePre",
    config = function()
      require("lint").linters_by_ft = {
        cpp = { "cppcheck" },
        bash = { "spellcheck" },
        python = { "pylint" },
      }
    end,
  },
}
