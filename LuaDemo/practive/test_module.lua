--
-- Created by IntelliJ IDEA.
-- User: Administrator
-- Date: 2019/7/8
-- Time: 15:43
-- To change this template use File | Settings | File Templates.
--
require("module")

print(module.constant)

module.func3()
-- test_module2.lua 文件
-- module 模块为上文提到到 module.lua
-- 别名变量 m
local m = require("module")

print(m.constant)

m.func3()
local path = "/usr/local/lua/lib/libluasocket.so"
local f = loadlib(path, "luaopen_socket")
f()