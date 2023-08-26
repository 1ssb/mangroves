import torch
from typing import List, Union, Type, Any, Dict, Optional

class MangroveException(Exception):
    """Custom Exception for the Mangrove class."""
    pass

class Mangrove:
    __slots__ = ["depths", "data", "types", "levels"]

    def __init__(self) -> None:
        # Initialize with depth 0 pre-configured for basic types
        self.depths: Dict[int, List[Type]] = {0: [int, float, str, torch.Tensor]}
        self.data: Dict[str, Any] = {}
        self.types: Dict[str, Type] = {}
        self.levels: Dict[str, int] = {}

    def config(self, depth: int, types: List[Type]) -> None:
        # Configure a new depth level with allowed types
        if depth == 0:
            raise MangroveException("Depth 0 is pre-configured and cannot be modified.")
        self.depths[depth] = types

    def add_data(self, depth: int, data_type: Type, var: List[str], value: Optional[List[Any]] = None) -> None:
        # Add data to a specific depth level
        if len(var) != len(value):
            raise MangroveException("Length of variable names and values must match.")
        
        if depth not in self.depths:
            raise MangroveException("Depth not configured. Please configure the depth first.")
        
        if data_type not in self.depths[depth]:
            raise MangroveException(f"Type {data_type} is not allowed at depth {depth}.")
        
        for i, v in enumerate(var):
            if v in self.data:
                raise MangroveException(f"Variable name {v} is already in use.")

            val = value[i] if value else None
            self.data[v] = val
            self.types[v] = data_type
            self.levels[v] = depth

    def summary(self) -> Dict[str, Union[Dict[str, Union[int, Type]], Dict[str, Type]]]:
        # Generate a summary of all variables and their configurations
        configured_vars = {}
        unconfigured_vars = {}

        for name, depth in self.levels.items():
            dtype = self.types[name]
            if depth == 0:
                unconfigured_vars[name] = dtype
            else:
                configured_vars[name] = {"depth": depth, "type": dtype}

        return {'configured': configured_vars, 'unconfigured (depth 0)': unconfigured_vars}

    def __setattr__(self, name: str, value: Any) -> None:
        # Overridden to allow setting value of already-defined variables
        if name in self.__slots__:
            object.__setattr__(self, name, value)
        elif name in self.data:
            dtype = self.types[name]
            if isinstance(value, dtype):
                self.data[name] = value
            else:
                raise MangroveException(f"Value must be of type {dtype}.")
        else:
            raise MangroveException(f"No such attribute: {name}")

    def __getattr__(self, name: str) -> Any:
        # Overridden to allow getting value of already-defined variables
        if name in self.data:
            return self.data[name]
        else:
            raise MangroveException(f"No such attribute: {name}")

    def var(self, depth: Optional[int] = None, data_type: Optional[Type] = None) -> List[str]:
        # Retrieve variable names based on optional depth and type filters
        return [name for name in self.data.keys() if (depth is None or depth == self.levels[name]) and (data_type is None or data_type == self.types[name])]

    def index(self, depth: Optional[int] = None, data_type: Optional[Type] = None) -> Dict[str, Any]:
        # Retrieve variables based on optional depth and type filters
        return {name: value for name, value in self.data.items() if (depth is None or depth == self.levels[name]) and (data_type is None or data_type == self.types[name])}
    
    def push(self, depth: int, var_name: str) -> None:
        # Move a variable from depth 0 to a different depth
        if var_name not in self.data:
            raise MangroveException(f"Variable {var_name} does not exist.")
        
        if self.levels[var_name] != 0:
            raise MangroveException(f"{var_name} is not at depth 0. Cannot push.")
        
        self.levels[var_name] = depth

    def tocuda(self, depth: Optional[int] = None, data_type: Optional[Type] = None) -> None:
        # Move tensor variables to CUDA, if available
        if torch.cuda.is_available():
            for name in self.data.keys():
                if (depth is None or depth == self.levels[name]) and (data_type is None or data_type == self.types[name]):
                    value = self.data[name]
                    if isinstance(value, torch.Tensor):
                        self.data[name] = value.cuda()
        else:
            raise MangroveException("A CUDA-enabled GPU is not available on this device. If nvidia-smi command returns correctly, check for compatibility of nvcc version.")
