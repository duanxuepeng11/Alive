--
-- Created by IntelliJ IDEA.
-- User: Administrator
-- Date: 2019/7/8
-- Time: 14:26
-- To change this template use File | Settings | File Templates.
-- 单行注释

--[[
 多行注释
  --]]
print("aaadsaaa")

--[[
8大数据类型:
nil 这个最简单，只有值nil属于该类，表示一个无效值（在条件表达式中相当于false）。
boolean
number  表示双精度类型的实浮点数
string  字符串由一对双引号或单引号来表示
function    由 C 或 Lua 编写的函数
userdata    表示任意存储在变量中的C数据结构
thread  表示执行的独立线路，用于执行协同程序
table   Lua 中的表（table）其实是一个"关联数组"（associative arrays），数组的索引可以是数字、字符串或表类型。在 Lua 里，table 的创建是通过"构造表达式"来完成，最简单构造表达式是{}，用来创建一个空表。

 ]]
print(type("Hello world"))      --> string
print(type(10.4*3))             --> number
print(type(print))              --> function
print(type(type))               --> function
print(type(true))               --> boolean
print(type(nil))                --> nil
print(type(type(X)))            --> string

--对于全局变量和 table，nil 还有一个"删除"作用，给全局变量或者 table 表里的变量赋一个 nil 值，等同于把它们删掉，执行下面代码就知：
tab1 = { key1 = "val1", key2 = "val2", "val3" }
for k, v in pairs(tab1) do
    print(k .. " - " .. v)
end

tab1.key1 = nil
for k, v in pairs(tab1) do
    print(k .. " - " .. v)
end

print(type(X))
print(type(X)==nil)
print(type(X)=="nil")

html = [[
<html>
<head></head>
<body>
    <h1>aaa</h1>
    <a href="http://www.runoob.com/">菜鸟教程</a>
</body>
</html>
]]
print(html)
print("2" + 6)
--字符串连接
print("2" .. 4)

print(#html)

--table 表
local tbl1 = {}
local tbl2 = {"apple","orange","grape" }

a = {}
a["key"] = "value"
key = 10
a[key] = 22
a[key] = a[key] + 11
for k,v in pairs(a) do
    print(k .. "    :   " .. v)
end

for k,v in pairs(tbl2) do
    print("key",k,v)
end
print("***********************")
print(tbl2[2])
print(tbl2.key)


-- table3.lua
a3 ={}
for i=1,10 do
    a3[i] = i
end

print(a3)

a3["key"] = "val"
print(a3["key"])
print(a3["none"])
print(a3[2])

--function 函数
function factorial1(n)
    if n ==0 then
        return 1
    else
        return n * factorial1(n - 1)
    end
end

print(factorial1(5))
factorial2 = factorial1
print(factorial2(5))


-- 匿名函数
function testFun(tab,fun)
    for k,v in pairs(tab) do
        print(fun(k,v))
    end
end

tab = {key1="val1",key2="val2" }
testFun(tab,
    function(key,val)
    return key.."="..val;
    end
    )

--[[
--在 Lua 里，最主要的线程是协同程序（coroutine）。它跟线程（thread）差不多，拥有自己独立的栈、局部变量和指令指针，可以跟其他协同程序共享全局变量和其他大部分东西。
--
--线程跟协程的区别：线程可以同时多个运行，而协程任意时刻只能运行一个，并且处于运行状态的协程只有被挂起（suspend）时才会暂停。

 ]]






