--
-- Created by IntelliJ IDEA.
-- User: Administrator
-- Date: 2019/7/8
-- Time: 15:19
-- To change this template use File | Settings | File Templates.
--
function average(...)
    result = 0
    local arg={...}
    for i,v in ipairs(arg) do
        result = result + v
    end
    print("总共传入 " .. select("#",...) .. " 个数")
    return result/select("#",...)
end

function average2(...)
    result = 0
    local arg={...}
    for i,v in ipairs(arg) do
        result = result + v
    end
    print("总共传入 " .. #arg .. " 个数")
    return result/#arg
end

print("平均值为",average(10,5,3,4,5,6))
print("平均值为",average2(10,5,3,4,5,6))

function fwrite(fmt, ...)  ---> 固定的参数fmt
    return io.write(string.format(fmt, ...))
end

fwrite("runoob\n")       --->fmt = "runoob", 没有变长参数。
fwrite("%d%d\n", 1, 2)   --->fmt = "%d%d", 变长参数为 1 和 2

--[[
-- 通常在遍历变长参数的时候只需要使用 {…}，然而变长参数可能会包含一些 nil，那么就可以用 select 函数来访问变长参数了：select('#', …) 或者 select(n, …)
--
--select('#', …) 返回可变参数的长度
--select(n, …) 用于访问 n 到 select('#',…) 的参数
 ]]
do
    function foo(...)
        for i = 1, select('#', ...) do  -->获取参数总数
            local arg = select(i, ...); -->读取参数
            print("arg", arg);
        end
    end

    foo(1, 2, 3, 4);
end
