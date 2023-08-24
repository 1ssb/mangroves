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
    
    def bind(self, name, cardinal, order):
     if name in self.bindings:
        raise ValueError(f"Binding name {name} is already in use")
    # Use a list comprehension to create the binding
     binding = [[(var, value) for var, value in self.data.items()
                if int(depth_str) == self.levels[var] and isinstance(value, eval(type_str))]
               for depth_str, type_str in order.items()]
    # Check if all depths have enough variables to create the binding
     if not all(len(b) >= cardinal for b in binding):
        raise ValueError(f"Binding cannot be created with the given cardinality and order")
    # Create the binding by taking the first `cardinal` variables from each depth
     binding = [tuple(var for var, value in b[:cardinal]) for b in binding]
    # Transpose the binding to create tuples of variables from different depths
     binding = list(zip(*binding))
     self.bindings[name] = binding
    
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
