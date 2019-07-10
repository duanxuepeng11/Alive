import json

name_emb = {'a':'1111','b':'2222','c':'3333','d':'4444'}
print(type(name_emb))
jsObj = json.dumps(name_emb)
print(type(jsObj))
print(name_emb)

print(jsObj)

jsLoads = json.loads(jsObj)
print(type(jsLoads))


"""
dumps      -> 讲dic字典转成str
loads       ->将str字符串转成dic字典类型
dump        ->将dic字典写入文件(2中方式 ,1中遍历,1种直接dump写入)
                    # solution 1  先转化成str写入
                    jsObj = json.dumps(name_emb)    
                    with open(emb_filename, "w") as f:  
                        f.write(jsObj)  
                        f.close()  
                        
                    # solution 2   直接将dict写入
                    json.dump(name_emb, open(emb_filename, "w"))
                    
load        ->加载数据,用于从json文件中读取数据。

"""