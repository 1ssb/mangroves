# Code by 1ssb
# MIT License
# Req: CUDA-enabled GPU
# mangrove.py

class Mangrove:
    def __init__(self):
        self.data = {}  # Store data as a dictionary of dictionaries
        self.addresses = {}  # Store variable addresses

    def config(self, depth=None, data_types=None, data=None):
        if depth is None or data_types is None or data is None:
            raise ValueError("Missing required parameters: depth, data_types, data")
        
        if depth in self.data:
            raise ValueError(f"Depth {depth} is already configured.")
        
        self.data[depth] = {}
        
        for data_type, data_dict in data.items():
            if data_type not in data_types:
                raise ValueError(f"Data type {data_type} is not allowed at depth {depth}.")
            
            for variable_name, variable_data in data_dict.items():
                if variable_name in self.data[depth]:
                    raise ValueError(f"Variable {variable_name} is already configured at depth {depth}.")
                
                self.data[depth][variable_name] = variable_data
                self.addresses[variable_name] = id(variable_data)
                setattr(self, variable_name, variable_data)  # Lock variable name as attribute

    def pop(self, depth=None):
        if depth is None:
            raise ValueError("Missing required parameter: depth")
        
        if depth not in self.data:
            raise ValueError(f"Depth {depth} is not configured.")
        
        return self.data[depth]

    def data(self, depth=None, data_type=None, variable_name=None):
        if depth is None:
            raise ValueError("Missing required parameter: depth")
        
        if variable_name is None:  # Return all data at the given depth
            if depth not in self.data:
                raise ValueError(f"Depth {depth} is not configured.")
            return self.data[depth]
        
        if data_type is not None:  # Access variable by name and data type
            if depth not in self.data or variable_name not in self.data[depth]:
                raise ValueError(f"Variable {variable_name} not found at depth {depth}.")
            return self.data[depth][variable_name]
        
        raise ValueError("Missing required parameter: data_type")

    def adrs(self):
        return {f"{depth}: {var}": hex(self.addresses[var]) for var in self.addresses}

    def summary(self):
        summary_info = {}
        for depth, depth_data in self.data.items():
            summary_info[depth] = {}
            for data_type, var_dict in depth_data.items():
                summary_info[depth][data_type] = list(var_dict.keys())
        return summary_info

# Example usage
mangrove_instance = Mangrove()

# Configure data at depth 1
mangrove_instance.config(depth=1, data_types=["int", "list"], data={
    "int_data": 42,
    "list_data": [1, 2, 3]
})

# Configure data at depth 2
mangrove_instance.config(depth=2, data_types=["str", "dict"], data={
    "str_data": "Hello",
    "dict_data": {"key": "value"}
})

# Access data at depth 1
print(mangrove_instance.pop(depth=1))  # Output: {'int_data': 42, 'list_data': [1, 2, 3]}

# Access data of a specific type at depth 2
print(mangrove_instance.data(depth=2, data_type="str"))  # Output: {'str_data': 'Hello'}

# Access specific variable by name and data type
print(mangrove_instance.data(depth=1, data_type="int", variable_name="int_data"))  # Output: 42

# Access variable directly by attribute name
print(mangrove_instance.int_data)  # Output: 42

# Print summary of all variables at various depths and types
print(mangrove_instance.summary())
