# Code by 1ssb
# MIT License
# Req: CUDA-enabled GPU
# mangrove.py

class Mangrove:
    # A novel data structure for networked indexation in evolving real-time systems
    def __init__(self):
        # Initialize the attributes of the class
        self.variables = {} # A dictionary that stores the names and values of the locked variables
        self.depths = {} # A dictionary that stores the configuration of each depth level
        self.__class__ = "mangrove" # A string that identifies the class name
        self.data = {} # A dictionary that stores the actual data for each variable

    def __setattr__(self, name, value):
        # Override the default behavior of setting an attribute
        if name in ["variables", "depths", "__class__", "data"]:
            # Allow setting the predefined attributes
            super().__setattr__(name, value)
        elif name in self.variables:
            # Raise an error if the name is already locked
            raise ValueError(f"Variable {name} is already locked and cannot be reused.")
        else:
            # Set the name and value in the variables attribute and as an attribute of the class
            self.variables[name] = value
            super().__setattr__(name, value)

    def __getattr__(self, name):
        # Override the default behavior of getting an attribute
        if name in self.variables:
            # Return the value from the variables attribute
            return self.variables[name]
        else:
            # Raise an error if the name is not found
            raise AttributeError(f"{name} not found in Mangrove instance.")

    def __delattr__(self, name):
        # Override the default behavior of deleting an attribute
        if name in self.variables:
            # Raise an error if the name is locked
            raise ValueError(f"Variable {name} is locked and cannot be deleted.")
        else:
            # Delete the attribute from the class
            super().__delattr__(name)

    def config(self, depth=None, types=None, name=None):
        # Configure the depth levels, the data types, and the variable names for each level
        if depth is not None:
            # Check if the depth level is valid and create a new entry in the depths attribute if not exists
            if depth not in self.depths:
                if depth > 1 and depth - 1 not in self.depths:
                    raise ValueError(f"Depth {depth - 1} must be configured before configuring depth {depth}.")
                self.depths[depth] = {"types": [], "names": {}}
            if types is not None:
                # Set the allowed data types for the depth level
                self.depths[depth]["types"] = types
            if name is not None:
                # Set the variable names for each data type for the depth level
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
        # Print the data for a given variable name or print the summary of all depth levels and their configurations
        if variable_name is None:
            # Print the summary of all depth levels and their configurations
            for depth, data in sorted(self.depths.items()):
                print(f"Depth: {depth}: ", end="")
                for data_type, var_names in data["names"].items():
                    print(f"[type: {data_type}: variable_names:{{{', '.join(var_names)}}}]; ", end="")
                print()
        else:
            # Print the data for a given variable name or raise an error if not found
            if variable_name in self.data:
                print(self.data[variable_name])
            else:
                print(f"No data found for variable {variable_name}.")
    
    def bundle(self, cardinal=None, order=None):
        # Order the data types at each depth level according to their cardinality and their input sequence 
        if cardinal is not None and order is not None:
            # Check if the cardinality and the order of the data types are correct and raise an error if not
            for depth, data_type in order.items():
                depth = int(depth.split("depth")[-1])
                if depth in self.depths:
                    if data_type in self.depths[depth]["types"]:
                        if len(self.depths[depth]["names"][data_type]) != cardinal:
                            raise ValueError(f"Cardinal number of {data_type} has not been configured in depth {depth}.")
                    else:
                        raise ValueError(f"Data type {data_type} is not allowed at depth {depth}.")
                else:
                    raise ValueError(f"Depth {depth} must be configured before using it.")
