import mangrove as mgv

x = mgv.Mangrove()
x.var1 = 10
print(x.var1) # 10
x.var1 = 20 # ValueError: Variable var1 is already locked and cannot be reused.
