## Code by 1ssb and Abhaas Goyal
# MIT License
# Req: CUDA-enabled GPU

import numpy as np
import dask as da

class Mangrove:
    def __init__(self):
        self.variables = {}

    def __setattr__(self, name, value):
        if name == "variables":
            super().__setattr__(name, value)
        elif name in self.variables:
            raise ValueError(f"Variable {name} is already locked and cannot be reused.")
        else:
            self.variables[name] = value
            super().__setattr__(name, value)

mgv = Mangrove()
mgv.var1 = 10
print(mgv.var1) # 10
mgv.var1 = 20 # ValueError: Variable var1 is already locked and cannot be reused.

