--
-- Created by IntelliJ IDEA.
-- User: Administrator
-- Date: 2019/7/8
-- Time: 15:39
-- To change this template use File | Settings | File Templates.
--
module ={}

module.constant = "这是一个常量"

function module.func1()
    io.write("这是一个公有函数!\n")
end

local function fun2()
    print("这是一个私有函数")
end

function module.fun3()
    fun2()
end

return module
