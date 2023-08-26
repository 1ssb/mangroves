# code by 1ssb (Pending)
# Req: CUDA enabled GPU

from mangrove import Mangrove
import torch

m = Mangrove()

# Configure the allowed types for each depth
m.config(depth=1, types=[int, torch.Tensor])
m.config(depth=2, types=[torch.Tensor])

# Add data to the Mangrove instance
# Add five integers at depth 1
m.add_data(depth=1, type=int, var=["x", "y", "z", "w", "v"], value=[1, 2, 3, 4, 5])
# Add five matrices at depth 1
m.add_data(depth=1, type=torch.Tensor, var=["a", "b", "c", "d", "e"], value=[torch.rand(3, 3) for _ in range(5)])
# Add five matrices at depth 2
m.add_data(depth=2, type=torch.Tensor, var=["f", "g", "h", "i", "j"], value=[torch.rand(3, 3) for _ in range(5)])

print(m.f)

##### Write code for tensor manipulation, indexing and copying to GPU without making additional copies using the index dictionary.

