## Code by 1ssb and Abhaas Goyal
# MIT License
# Req: CUDA-enabled GPU
# mangrove.py

import numpy as np
import dask as da
import torch

# mangrove.py
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

    def __getattr__(self, name):
        if name in self.variables:
            return self.variables[name]
        else:
            raise AttributeError(f"{name} not found in Mangrove instance.")

    def __delattr__(self, name):
        if name in self.variables:
            raise ValueError(f"Variable {name} is locked and cannot be deleted.")
        else:
            super().__delattr__(name)

    def config(self, **kwargs):
        for key, value in kwargs.items():
            if key in self.variables:
                raise ValueError(f"Variable {key} is already locked and cannot be reused.")
            else:
                self.variables[key] = value
                super().__setattr__(key, value)



