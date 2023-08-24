# code by abhaasgoyal (Pending)
# Req: CUDA enabled GPU

from mangrove import Mangrove
import torch

mangrove = Mangrove()

# Configure the allowed types for each depth
mangrove.config(depth=1, types=[int, torch.Tensor])
mangrove.config(depth=2, types=[torch.Tensor])

# Add data to the Mangrove instance
# Add five integers at depth 1
mangrove.add_data(depth=1, type=int, var=["x", "y", "z", "w", "v"], value=[1, 2, 3, 4, 5])
# Add five matrices at depth 1
mangrove.add_data(depth=1, type=torch.Tensor, var=["a", "b", "c", "d", "e"], value=[torch.rand(3, 3) for _ in range(5)])
# Add five matrices at depth 2
mangrove.add_data(depth=2, type=torch.Tensor, var=["f", "g", "h", "i", "j"], value=[torch.rand(3, 3) for _ in range(5)])

# Create a binding with cardinality 5 and order int -> matrix -> matrix
mangrove.bind(name="bind1", cardinal=5,
              order={"1": "int", "2": "torch.Tensor", "3": "torch.Tensor"})

# Access the binding
print(mangrove.bind1) # A list of five tuples of the form (int, matrix, matrix)


##### Now write code such that it can handle memory management and deep copies the variables in memory to GPU without making additional copies 
