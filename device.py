# code by abhaasgoyal
# Req: CUDA enabled GPU

from Mangrove import Mangrove as mgv

# Configure the allowed types for each depth
    mangrove.config(depth=1, types=[int])
    mangrove.config(depth=2, types=[list])
    mangrove.config(depth=3, types=[dict])
    
    # Add data to the Mangrove instance
    mangrove.add_data(depth=1, type=int, var=["x"], value=1)
    mangrove.add_data(depth=2, type=list, var=["y"], value=[1, 2])
    mangrove.add_data(depth=3, type=dict, var=["z"], value={"a": 1})
    
    
    # Create a binding
    mangrove.bind(name="bind1", cardinal=1,
                  order={"1": "int", "2": "list", "3": "dict"})
    
    # Access the binding
    print(mangrove.bind1) # [('x', 1), ('y', [1, 2]), ('z', {'a': 1})]
