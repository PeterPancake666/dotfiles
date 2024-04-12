return {
  {
    "jay-babu/mason-nvim-dap.nvim",
    event = "VeryLazy",
    dependencies = {
      "williamboman/mason.nvim",
      "mfussenegger/nvim-dap",
    },
  },
  {
    "mfussenegger/nvim-dap",
    event = "VeryLazy",
    dependencies = {
      "nvim-neotest/nvim-nio",
      "rcarriga/nvim-dap-ui",
    },
    config = function()
      local dap = require("dap")
      local dapui = require("dapui")

      dapui.setup()
      dap.listeners.before.attach.dapui_config = function()
        dapui.open()
      end
      dap.listeners.before.launch.dapui_config = function()
        dapui.open()
      end

      vim.keymap.set("n", "<Leader>db", function()
        dap.toggle_breakpoint()
      end)
      vim.keymap.set("n", "<Leader>dr", function()
        dap.continue()
      end)

      dap.adapters.lldb = {
        type = "executable",
        command = "/usr/bin/lldb-vscode", -- adjust as needed, must be absolute path
        name = "lldb",
      }

      dap.configurations.cpp = {
        {
          name = "Launch",
          type = "lldb",
          request = "launch",
          program = function()
            return vim.fn.input("Path to executable: ", vim.fn.getcwd() .. "/", "file")
          end,
          cwd = "${workspaceFolder}",
          stopOnEntry = false,
          args = {},

          runInTerminal = false,
        },
      }
    end,
  },
}
