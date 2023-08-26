# Code by 1ssb
# Initialize Mangrove


m = Mangrove()

# Configure the allowed types for each depth
m.config(depth=1, types=[int, torch.Tensor])
m.config(depth=2, types=[torch.Tensor])

# Add data to the Mangrove instance
m.add_data(depth=1, data_type=int, var=["x", "y", "z", "w", "v"], value=[1, 2, 3, 4, 5])
m.add_data(depth=1, data_type=torch.Tensor, var=["a", "b", "c", "d", "e"], value=[torch.rand(3, 3) for _ in range(5)])
m.add_data(depth=2, data_type=torch.Tensor, var=["f", "g", "h", "i", "j"], value=[torch.rand(3, 3) for _ in range(5)])

# Fetching a value from Mangrove instance
print("m.f: ", m.f)

# Summary
print("Summary: ", m.summary())

# Index: Fetch variables with certain depths or types
print("Index with depth=1 and type=int: ", m.index(depth=1, data_type=int))
print("Index with type=torch.Tensor: ", m.index(data_type=torch.Tensor))

# Var: Get variable names with certain depths or types
print("Var with depth=1: ", m.var(depth=1))
print("Var with type=torch.Tensor: ", m.var(data_type=torch.Tensor))
