import torch
from typing import List, Union, Type, Any, Dict, Optional

class MangroveException(Exception):
    pass

class Mangrove:
    __slots__ = ["depths", "data", "types", "levels"]

    def __init__(self) -> None:
        self.depths: Dict[int, List[Type]] = {0: [int, float, str, torch.Tensor]}  # Depth 0 pre-configured for untyped data
        self.data: Dict[str, Any] = {}
        self.types: Dict[str, Type] = {}
        self.levels: Dict[str, int] = {}

    def config(self, depth: int, types: List[Type]) -> None:
        if depth == 0:
            raise MangroveException("Depth 0 is pre-configured and cannot be modified.")
        self.depths[depth] = types

    def add_data(self, depth: int, data_type: Type, var: List[str], value: Optional[List[Any]] = None) -> None:
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

    def summary(self) -> Dict[str, Dict[str, Union[int, Type]]]:
        if 0 in self.levels.values():
            raise MangroveException("Depth 0 has unconfigured variables.")
        
        return {name: {"depth": self.levels[name], "type": self.types[name]} for name in self.data.keys()}

    def __setattr__(self, name: str, value: Any) -> None:
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
        if name in self.data:
            return self.data[name]
        else:
            raise MangroveException(f"No such attribute: {name}")

    def var(self, depth: Optional[int] = None, data_type: Optional[Type] = None) -> List[str]:
        return [name for name in self.data.keys() if (depth is None or depth == self.levels[name]) and (data_type is None or data_type == self.types[name])]

    def index(self, depth: Optional[int] = None, data_type: Optional[Type] = None) -> Dict[str, Any]:
        return {name: value for name, value in self.data.items() if (depth is None or depth == self.levels[name]) and (data_type is None or data_type == self.types[name])}
    
    def push(self, depth: int, var_name: str) -> None:
        if var_name not in self.data:
            raise MangroveException(f"Variable {var_name} does not exist.")
        
        if self.levels[var_name] != 0:
            raise MangroveException(f"{var_name} is not at depth 0. Cannot push.")
        
        self.levels[var_name] = depth
    
    def tocuda(self, depth: Optional[int] = None, data_type: Optional[Type] = None) -> None:
        if torch.cuda.is_available():
            for name in self.data.keys():
                if (depth is None or depth == self.levels[name]) and (data_type is None or data_type == self.types[name]):
                    value = self.data[name]
                    if isinstance(value, torch.Tensor):
                        self.data[name] = value.cuda()
        else:
            raise MangroveException("A CUDA-enabled GPU is not available on this device.")
