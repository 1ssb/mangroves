# Code by 1ssb
# MIT License
# Req: CUDA-enabled GPU
# mangrove.py

class Mangrove:
    def __init__(self):
        self.variables = {}
        self.depths = {}
        self.data = {}
        self.structure_ordered = False
        self.bundles = {}  # Store bundles as a dictionary
        self.addresses = {}  # Store variable addresses

    def __setattr__(self, name, value):
        if name in ["variables", "depths", "__class__", "data", "structure_ordered", "bundles", "addresses"]:
            super().__setattr__(name, value)
        elif name in self.variables:
            raise ValueError(f"Variable {name} is already locked and cannot be reused.")
        else:
            self.variables[name] = value
            self.addresses[name] = id(value)  # Store variable's memory address
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
                            self.addresses[var_name] = None
                            super().__setattr__(var_name, None)
                            if data_type not in self.depths[depth]["names"]:
                                self.depths[depth]["names"][data_type] = []
                            self.depths[depth]["names"][data_type].append(var_name)

    def bundle(self, cardinal=None, order=None):
        if cardinal is not None and order is not None:
            bundle_dict = {}
            for depth, data_type in order.items():
                depth = int(depth.split("depth")[-1])
                if depth in self.depths:
                    if data_type in self.depths[depth]["types"]:
                        if len(self.depths[depth]["names"][data_type]) < int(cardinal):
                            raise ValueError(f"Cardinality number of {data_type} not met at depth {depth}.")
                    else:
                        raise ValueError(f"Data type {data_type} is not allowed at depth {depth}.")
                else:
                    raise ValueError(f"Depth {depth} must be configured before using it.")
                
                bundle_dict[f"bundle {depth}"] = data_type  # Store bundle info

            self.bundles = bundle_dict
            self.structure_ordered = True

    def pop(self, variable_name=None):
        if self.structure_ordered:
            if variable_name is None:
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

    def dict(self):
        return self.bundles  # Return the bundle dictionary

    def adrs(self):
        return {f"{depth}: {var}": hex(self.addresses[var]) for var, depth in self.variables.items()}

