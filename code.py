import mangrove as mgv

x = mgv.Mangrove()
x.config(depth=1, types=["tensor", "bool"], name=["tensor: tensor1, tensor2", "bool: bool1, bool2"])
x.config(depth=2, types=["int", "str"], name=["int: int1, int2", "str: str1, str2"])
print(x.tensor1) # None
print(x.bool1) # None
print(x.int1) # None
print(x.str1) # None
x.tensor1 = 10 # ValueError: Variable tensor1 is already locked and cannot be reused.
