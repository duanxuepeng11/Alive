--
-- Created by IntelliJ IDEA.
-- User: Administrator
-- Date: 2019/7/8
-- Time: 15:02
-- To change this template use File | Settings | File Templates.
--

a = 5   -- 全局变量
local b = 5  --局部变量

function joke()
    c = 4           --全局变量
    local d = 6    --局部变量
end

joke()
print(c,d)

do
    local a  = 6
    b = 6
    print(a,b)
end
print(a,b)

--赋值语句
--a = "hello".."world"
x,y = 10, 2*3
print(x,y)

x, y = y, x
print(x,y)
--[[
--a. 变量个数 > 值的个数             按变量个数补足nil
--b. 变量个数 < 值的个数             多余的值会被忽略
 ]]

site = {}
site["key"] ="www.runads/com"
print(site["key"])
print(site.key)
tab = {key1="val1",key2="val2" }

print(tab["key1"])
print(tab.key1)
print(tab.key2)

s, e = string.find("www.runoob.com", "runoob")
print(s, e)