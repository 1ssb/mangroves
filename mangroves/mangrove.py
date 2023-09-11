import weakref
import torch
from typing import List, Union, Type, Any, Dict, Optional, Tuple

class Mangrove:
    __slots__ = ["depths", "data", "types", "levels", "inosculations"]
    _instances = weakref.WeakValueDictionary()  # WeakValueDictionary to keep track of instances

    def __init__(self) -> None:
        instance_id = id(self)
        if instance_id in Mangrove._instances:
            raise Exception("MangroveException: Cannot reuse variable name for this instance unless deleted.")
        
        Mangrove._instances[instance_id] = self  # Register the new instance
        
        self.depths = {0: [int, float, str, torch.Tensor]}
        self.data = {}
        self.types = {}
        self.levels = {}
        self.inosculations = {}

    def deleter(self) -> None:
        """Remove the instance from the WeakValueDictionary."""
        instance_id = id(self)
        if instance_id in Mangrove._instances:
            del Mangrove._instances[instance_id]
        else:
            existing_instances = list(Mangrove._instances.keys())
            self._raise_exception(f"Instance ID {instance_id} does not exist. Existing instances: {existing_instances}")

    def _raise_exception(self, message: str) -> None:
        """Raise an exception with a custom message."""
        raise Exception(f"MangroveException: {message}")

    def config(self, depth: int, types: List[Type]) -> None:
        if depth == 0:
            self._raise_exception("Depth 0 is pre-configured and cannot be modified.")
        self.depths[depth] = types

    def add_data(self, depth: int, data_type: Type, var: List[str], value: Optional[List[Any]] = None) -> None:
        if len(var) != len(value):
            self._raise_exception("Length of variable names and values must match.")

        if not self.depths.get(depth):
            self._raise_exception(f"Depth {depth} not configured. Please configure the depth first.")
        
        if data_type not in self.depths[depth]:
            self._raise_exception(f"Type {data_type} is not allowed at depth {depth}.")

        for i, v in enumerate(var):
            if v in self.data:
                self._raise_exception(f"Variable name {v} is already in use.")
            self.data[v] = value[i] if value else None
            self.types[v] = data_type
            self.levels[v] = depth

    def inosc(self, depth_variable_pairs: List[Tuple[int, Type]]) -> Tuple[Tuple[int, Type], ...]:
        counts = {}
        for depth, var_type in depth_variable_pairs:
            if depth not in self.depths:
                self._raise_exception(f"Depth {depth} is not configured.")
            if var_type not in self.depths[depth]:
                self._raise_exception(f"Type {var_type} is not allowed at depth {depth}.")
            counts[depth] = counts.get(depth, 0) + 1

        if len(set(counts.values())) > 1:
            self._raise_exception("The number of variables in each depth must match for inosculation.")
        
        inosc_key = tuple(sorted(depth_variable_pairs))
        self.inosculations[inosc_key] = True
        return inosc_key

    def uproot(self, cojoin: Tuple[Tuple[int, Type], ...]) -> List[List[Tuple[str, Any]]]:
        cojoined_data = []
        for depth, var_type in cojoin:
            var_names = [name for name, dtype in self.types.items() if dtype == var_type and self.levels[name] == depth]
            var_values = [self.data[v] for v in var_names]

            if not cojoined_data:
                cojoined_data = [[(name, value)] for name, value in zip(var_names, var_values)]
            else:
                cojoined_data = [existing + [(name, value)] for existing in cojoined_data for name, value in zip(var_names, var_values)]

        return cojoined_data

    def summary(self) -> Dict[str, Union[Dict[str, Union[int, Type]], Dict[str, Type]]]:
        summary_dict = {'configured': {}, 'unconfigured (depth 0)': {}, 'inosculated': {}}
        
        for name, depth in self.levels.items():
            dtype = self.types[name]
            if depth == 0:
                summary_dict['unconfigured (depth 0)'][name] = dtype
            else:
                summary_dict['configured'][name] = {"depth": depth, "type": dtype}

            for inosc_key in self.inosculations:
                if (depth, dtype) in inosc_key:
                    summary_dict['inosculated'].setdefault(str(inosc_key), []).append(name)

        return summary_dict

    def __setattr__(self, name: str, value: Any) -> None:
        if name in self.__slots__:
            object.__setattr__(self, name, value)
        else:
            dtype = self.types.get(name)
            if dtype and isinstance(value, dtype):
                self.data[name] = value
            else:
                self._raise_exception(f"Value must be of type {dtype}.")

    def __getattr__(self, name: str) -> Any:
        if name in self.data:
            return self.data[name]
        self._raise_exception(f"No such attribute: {name}")

    def var(self, depth: Optional[int] = None, data_type: Optional[Type] = None) -> List[str]:
        return [name for name in self.data.keys() if (depth is None or depth == self.levels.get(name, None)) and (data_type is None or data_type == self.types.get(name, None))]

    def index(self, depth: Optional[int] = None, data_type: Optional[Type] = None) -> Dict[str, Any]:
        return {name: value for name, value in self.data.items() if (depth is None or depth == self.levels.get(name, None)) and (data_type is None or data_type == self.types.get(name, None))}

    def push(self, depth: int, var_name: str) -> None:
        if self.levels.get(var_name, None) != 0:
            self._raise_exception(f"{var_name} is not at depth 0. Cannot push.")
        self.levels[var_name] = depth

    def tocuda(self, depth: Optional[int] = None, data_type: Optional[Type] = None) -> None:
        if torch.cuda.is_available():
            for name in self.data.keys():
                if (depth is None or depth == self.levels.get(name, None)) and (data_type is None or data_type == self.types.get(name, None)):
                    value = self.data[name]
                    if isinstance(value, torch.Tensor):
                        self.data[name] = value.cuda()
        else:
            self._raise_exception("A CUDA-enabled GPU is not available on this device.")

    def shift(self, to: int, variable_name: str) -> None:
        data_type = self.types.get(variable_name, None)
        if data_type is None:
            self._raise_exception(f"Variable {variable_name} does not exist.")
        if to == 0 or data_type in self.depths.get(to, []):
            self.levels[variable_name] = to
        else:
            self._raise_exception(f"Type {data_type} is not allowed at depth {to}.")
