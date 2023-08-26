# Code by 1ssb

import torch

class Mangrove:
    __slots__ = ["depths", "data", "types", "levels"]
    
    def __init__(self):
        self.depths = {}
        self.data = {}
        self.types = {}
        self.levels = {}
        
    def config(self, depth, types):
        if depth > 1 and (depth-1) not in self.depths:
            raise ValueError(f"Depth {depth-1} must be configured before depth {depth}")
        self.depths[depth] = types
    
    def add_data(self, depth, data_type, var, value=None):
        if depth not in self.depths:
            raise ValueError(f"Depth {depth} must be configured before adding data")
        if data_type not in self.depths[depth]:
            raise ValueError(f"Type {data_type} is not allowed at depth {depth}")
            
        if value is not None and len(var) != len(value):
            raise ValueError("Length of var and value lists should match")
            
        for i, v in enumerate(var):
            if v in self.data:
                raise ValueError(f"Variable name {v} is already in use")
            
            val = value[i] if value is not None else None
            self.data[v] = val
            self.types[v] = data_type
            self.levels[v] = depth
    
    def summary(self):
        return {name: {"type": type(value).__name__, "depth": self.levels[name]} for name, value in self.data.items()}
    
    def __setattr__(self, name, value):
        if name in self.__slots__:
            object.__setattr__(self, name, value)
        elif name in self.data:
            if isinstance(value, self.types[name]):
                self.data[name] = value
            else:
                raise TypeError(f"Value must be of type {self.types[name]}")
        else:
            raise AttributeError(f"No such attribute: {name}")

    def __getattr__(self, name):
        if name in self.data:
            return self.data[name]
        else:
            raise AttributeError(f"No such attribute: {name}")
    
    def __repr__(self):
        return f"<Mangrove object with data: {self.data}>"
    
    def var(self, depth=None, data_type=None):
        result = []
        for name, value in self.data.items():
            if (depth is None or depth == self.levels[name]) and (data_type is None or isinstance(value, data_type)):
                result.append(name)
        return result
    
    def index(self, depth=None, data_type=None):
        result = {}
        for name, value in self.data.items():
            if (depth is None or depth == self.levels[name]) and (data_type is None or isinstance(value, data_type)):
                result[name] = value
        return result
