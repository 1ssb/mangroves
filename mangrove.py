# Code by 1ssb
# MIT License
# Req: CUDA-enabled GPU
# mangrove.py

import torch

class Mangrove:
    def __init__(self):
        self.depths = {}
        self.data = {}
        self.types = {}
        self.levels = {}
        self.bindings = {}
    
    def config(self, depth, types):
        if depth > 1 and (depth-1) not in self.depths:
            raise ValueError(f"Depth {depth-1} must be configured before depth {depth}")
        self.depths[depth] = types
    
    def add_data(self, depth, type, var, value=None):
        if depth not in self.depths:
            raise ValueError(f"Depth {depth} must be configured before adding data")
        if type not in self.depths[depth]:
            raise ValueError(f"Type {type} is not allowed at depth {depth}")
        for v in var:
            if v in self.data:
                raise ValueError(f"Variable name {v} is already in use")
            self.data[v] = value
            self.types[v] = type
            self.levels[v] = depth
    
    def bind(self, name, cardinal, order):
        if name in self.bindings:
            raise ValueError(f"Binding name {name} is already in use")
        binding = []
        for depth_str, type_str in order.items():
            depth = int(depth_str)
            type = eval(type_str)
            if depth not in self.depths:
                raise ValueError(f"Depth {depth} is not configured")
            if type not in self.depths[depth]:
                raise ValueError(f"Type {type} is not allowed at depth {depth}")
            count = 0
            for var, value in self.data.items():
                if count >= cardinal:
                    break
                if self.levels[var] == depth and isinstance(value, type):
                    binding.append((var, value))
                    count += 1
        self.bindings[name] = binding
    
    def summary(self):
        result = {}
        for name, value in self.data.items():
            result[name] = {"type": type(value).__name__, "depth": self.levels[name]}
        return result
    
    def __getattr__(self, name):
        if name in self.data:
            return self.data[name]
        elif name in self.bindings:
            return self.bindings[name]
        else:
            raise AttributeError(f"No such attribute: {name}")
    
    def __setattr__(self, name, value):
        if name in ["depths", "data", "types", "levels", "bindings"]:
            super().__setattr__(name, value)
        elif name in self.data:
            if isinstance(value, self.types[name]):
                self.data[name] = value
            else:
                raise TypeError(f"Value must be of type {self.types[name]}")
        else:
            raise AttributeError(f"No such attribute: {name}")
    
    def __repr__(self):
        return f"<Mangrove object with data: {self.data}>"
