## Code by 1ssb and abhaasgoyal
# MIT License
# Req: CUDA-enabled GPU

import numpy as np
import dask as da
import torch

# mangrove.py
class Mangrove:
    def __init__(self):
        self.variables = {}
        self.depths = {}
        self.__class__ = "mangrove"
        self.data = {}

    def __setattr__(self, name, value):
        if name in ["variables", "depths", "__class__", "data"]:
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

    def config(self, depth=None, types=None, name=None):
        if depth is not None:
            if depth not in self.depths:
                if depth > 1 and depth - 1 not in self.depths:
                    raise ValueError(f"Depth {depth - 1} must be configured before configuring depth {depth}.")
                self.depths[depth] = {"types": [], "names": {}}
            if types is not None:
                self.depths[depth]["types"] = types
            if name is not None:
                for item in name:
                    data_type, var_names = item.split(":")
                    data_type = data_type.strip()
                    if data_type not in self.depths[depth]["types"]:
                        raise ValueError(f"Data type {data_type} is not allowed at depth {depth}.")
                    var_names = var_names.split(",")
                    for var_name in var_names:
                        var_name = var_name.strip()
                        if var_name in self.variables:
                            raise ValueError(f"Variable {var_name} is already locked and cannot be reused.")
                        else:
                            self.variables[var_name] = None
                            super().__setattr__(var_name, None)
                            if data_type not in self.depths[depth]["names"]:
                                self.depths[depth]["names"][data_type] = []
                            self.depths[depth]["names"][data_type].append(var_name)

    def pop(self, variable_name=None):
        if variable_name is None:
            for depth, data in sorted(self.depths.items()):
                print(f"Depth: {depth}: ", end="")
                for data_type, var_names in data["names"].items():
                    print(f"[type: {data_type}: variable_names:{{{', '.join(var_names)}}}]; ", end="")
                print()
        else:
            if variable_name in self.data:
                print(self.data[variable_name])
            else:
                print(f"No data found for variable {variable_name}.")

