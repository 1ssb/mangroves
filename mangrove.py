# Code by 1ssb
# MIT License
# Req: CUDA-enabled GPU
# mangrove.py

class Mangrove:
    # Use __slots__ to reduce memory usage
    __slots__ = ["depths", "data", "types", "levels", "bindings"]
    
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
        # Use a local variable to store self.data
        data = self.data
        if depth not in self.depths:
            raise ValueError(f"Depth {depth} must be configured before adding data")
        if type not in self.depths[depth]:
            raise ValueError(f"Type {type} is not allowed at depth {depth}")
        for v in var:
            if v in data:
                raise ValueError(f"Variable name {v} is already in use")
            data[v] = value
            self.types[v] = type
            self.levels[v] = depth
    
    def summary(self):
        # Do not use a cache to store the results of the summary
        # Calculate the summary every time the method is called
        result = {name: {"type": type(value).__name__, "depth": self.levels[name]}
                  for name, value in self.data.items()}
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
        # Use object.__setattr__ instead of super().__setattr__
        object.__setattr__(self, name, value)
     elif name in self.data:
        if isinstance(value, self.types[name]):
            self.data[name] = value
        else:
            raise TypeError(f"Value must be of type {self.types[name]}")
     else:
        raise AttributeError(f"No such attribute: {name}")


    
    def __repr__(self):
        return f"<Mangrove object with data: {self.data}>"
