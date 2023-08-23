# Code by 1ssb
# MIT License
# Req: CUDA-enabled GPU
# mangrove.py

class Mangrove:
    def __init__(self):
        self.variables = {}
        self.depths = {}
        self.data = {}  # Store data values
        self.structure_ordered = False  # Track whether structure is ordered

    def __setattr__(self, name, value):
        if name in ["variables", "depths", "__class__", "data", "structure_ordered"]:
            super().__setattr__(name, value)
        elif name in self.variables:
            raise ValueError(f"Variable {name} is already locked and cannot be reused.")
        else:
            self.variables[name] = value
            super().__setattr__(name, value)

    def __getattr__(self, name):
        if name.startswith('data_') and name[5:] in self.data:
            return self.data[name[5:]]
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

    def bundle(self, cardinal=None, order=None):
        if cardinal is not None and order is not None:
            for depth, data_type in order.items():
                depth = int(depth.split("depth")[-1])
                if depth in self.depths:
                    if data_type in self.depths[depth]["types"]:
                        if len(self.depths[depth]["names"][data_type]) < int(cardinal):
                            # Raise an error if cardinality is not met
                            raise ValueError(f"Cardinality number of {data_type} not met at depth {depth}.")
                    else:
                        raise ValueError(f"Data type {data_type} is not allowed at depth {depth}.")
                else:
                    raise ValueError(f"Depth {depth} must be configured before using it.")
            
            self.structure_ordered = True  # Mark structure as ordered

    def pop(self, variable_name=None):
        if self.structure_ordered:
            if variable_name is None:
                # Print the ordered structure
                structure_str = ""
                for depth, data in sorted(self.depths.items()):
                    for data_type, var_names in data["names"].items():
                        structure_str += ":".join(var_names) + ":"
                print(structure_str[:-1])
            else:
                if variable_name in self.data:
                    return self.data[variable_name]
                else:
                    return f"No data found for variable {variable_name}."
