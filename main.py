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

    # Create an instance of the Mangrove class
    instance = Mangrove()

    # Configure the allowed types for each depth
    instance.config(depth=1, types=[int, str])
    instance.config(depth=2, types=[int, str])

    # Add multiple variables
    instance.add_data(depth=1, type=int, var=["x", "y", "z"])
    instance.add_data(depth=1, type=int, var=["a", "b", "c"])
    instance.add_data(depth=2, type=str, var=["var"])

    # Update the existing variables
    instance.x = 10

    # Print the variables for specified depth and data type
    print("Variables at Depth 1 and int Data Type:")
    print(instance.index(depth=1, data_type=int))

    print("Variables at Depth 2 and str Data Type:")
    print(instance.index(depth=2, data_type=str))

if __name__ == "__main__":
    main()
