# test_mangrove.py
from mangrove import Mangrove  # Import the Mangrove class from mangrove.py

def main():
    mangrove = Mangrove()
    
    # Configure the allowed types for each depth
    mangrove.config(depth=1, types=[int])
    mangrove.config(depth=2, types=[list])
    mangrove.config(depth=3, types=[dict])
    
    # Add data to the Mangrove instance
    mangrove.add_data(depth=1, type=int, var=["x"], value=1)
    mangrove.add_data(depth=2, type=list, var=["y"], value=[1, 2])
    mangrove.add_data(depth=3, type=dict, var=["z"], value={"a": 1})
    
    
    # Create a binding
    mangrove.bind(name="bind1", cardinal=1, order={"1": "int", "2": "list", "3": "dict"})
    
    # Access the binding
    print(mangrove.bind1) # [('x', 'y', 'z')]

    # Access and modify the data attributes
    print(mangrove.x) # 1
    mangrove.x = 2
    print(mangrove.x) # 2
    
    # Get a summary of the data stored in the tree
    summary = mangrove.summary()
    print(summary) # {'x': {'type': 'int', 'depth': 1}, 'y': {'type': 'list', 'depth': 2}, 'z': {'type': 'dict', 'depth': 3}}
    
    # Create another Mangrove instance
    mangrove_instance = Mangrove()
    mangrove_instance.config(depth=1, types=[int])
    mangrove_instance.add_data(depth=1, type=int, var=["g"])
    
    # Access and modify the data attribute
    print(mangrove_instance.g) # None
    mangrove_instance.g = 1
    print(mangrove_instance.g) # 1

    m = Mangrove()
    m.config(1, ["int", "str"])
    m.config(2, ["float"])
    m.add_data(1, "int", ["x", "y"], 0)
    m.add_data(1, "str", ["name"], "John")
    m.add_data(2, "float", ["z"], 0.0)
    m.add_data(2, "float", ["q"], 3.0)
    
    depths = ["1", "2"]
    data_types = ["int", "float"]
    
    result = m.bind(depths=depths, data_types=data_types)
    print(result)

if __name__ == "__main__":
    main()
