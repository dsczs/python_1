tuple1 = (1,2,"a")
print(tuple1)
print(tuple1[0])
print(tuple1[0:2])
try:
    tuple1[0] = 3 #元组不允许修改
except:
    print("error")
    pass
