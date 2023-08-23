import mangrove as mgv

x = mgv.Mangrove()
x.config(var1=10, var2="hello", var3=[1, 2, 3], var4={"a": 1, "b": 2})
print(x.var1) # 10
print(x.var2) # hello
print(x.var3) # [1, 2, 3]
print(x.var4) # {'a': 1, 'b': 2}
x.var1 = 20 # ValueError: Variable var1 is already locked and cannot be reused.
