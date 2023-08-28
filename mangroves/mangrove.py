import torch
from typing import List, Union, Type, Any, Dict, Optional

class MangroveException(Exception):
    """Custom Exception for the Mangrove class."""
    pass

class Mangrove:
    __slots__ = ["depths", "data", "types", "levels"]

    def __init__(self) -> None:
        self.depths = {0: [int, float, str, torch.Tensor]}
        self.data = {}
        self.types = {}
        self.levels = {}

    def config(self, depth: int, types: List[Type]) -> None:
        if depth == 0:
            raise MangroveException("Depth 0 is pre-configured and cannot be modified.")
        self.depths[depth] = types

    def add_data(self, depth: int, data_type: Type, var: List[str], value: Optional[List[Any]] = None) -> None:
        if len(var) != len(value):
            raise MangroveException("Length of variable names and values must match.")
        
        depth_types = self.depths.get(depth, None)
        if depth_types is None:
            raise MangroveException("Depth not configured. Please configure the depth first.")
        
        if data_type not in depth_types:
            raise MangroveException(f"Type {data_type} is not allowed at depth {depth}.")

        for i, v in enumerate(var):
            try:
                _ = self.data[v]
                raise MangroveException(f"Variable name {v} is already in use.")
            except KeyError:
                val = value[i] if value else None
                self.data[v] = val
                self.types[v] = data_type
                self.levels[v] = depth

    def summary(self) -> Dict[str, Union[Dict[str, Union[int, Type]], Dict[str, Type]]]:
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
        if name in self.__slots__:
            object.__setattr__(self, name, value)
        else:
            try:
                dtype = self.types[name]
                if isinstance(value, dtype):
                    self.data[name] = value
                else:
                    raise MangroveException(f"Value must be of type {dtype}.")
            except KeyError:
                raise MangroveException(f"No such attribute: {name}")

    def __getattr__(self, name: str) -> Any:
        try:
            return self.data[name]
        except KeyError:
            raise MangroveException(f"No such attribute: {name}")

    def var(self, depth: Optional[int] = None, data_type: Optional[Type] = None) -> List[str]:
        return list(name for name in self.data.keys() if (depth is None or depth == self.levels.get(name, None)) and (data_type is None or data_type == self.types.get(name, None)))

    def index(self, depth: Optional[int] = None, data_type: Optional[Type] = None) -> Dict[str, Any]:
        return {name: value for name, value in self.data.items() if (depth is None or depth == self.levels.get(name, None)) and (data_type is None or data_type == self.types.get(name, None))}

    def push(self, depth: int, var_name: str) -> None:
        try:
            if self.levels[var_name] != 0:
                raise MangroveException(f"{var_name} is not at depth 0. Cannot push.")
            self.levels[var_name] = depth
        except KeyError:
            raise MangroveException(f"Variable {var_name} does not exist.")
        
    def tocuda(self, depth: Optional[int] = None, data_type: Optional[Type] = None) -> None:
        if torch.cuda.is_available():
            for name in self.data.keys():
                if (depth is None or depth == self.levels.get(name, None)) and (data_type is None or data_type == self.types.get(name, None)):
                    value = self.data[name]
                    if isinstance(value, torch.Tensor):
                        self.data[name] = value.cuda()
        else:
            raise MangroveException("A CUDA-enabled GPU is not available on this device. If nvidia-smi command returns correctly, check for compatibility of nvcc version.")

    def shift(self, to: int, variable_name: str) -> None:
        try:
            data_type = self.types[variable_name]
            if to == 0 or data_type in self.depths.get(to, []):
                self.levels[variable_name] = to
            else:
                raise MangroveException(f"Type {data_type} is not allowed at depth {to}.")
        except KeyError:
            raise MangroveException(f"Variable {variable_name} does not exist.")
