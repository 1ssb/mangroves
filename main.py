# test_mangrove.py
from mangrove import Mangrove  # Import the Mangrove class from mangrove.py

def main():
    # Create an instance of Mangrove
    experiment_data = Mangrove()

    # Configure depth and data types
    experiment_data.config(
        depth=1, 
        types=["tensor", "bool"], 
        name=["tensor: tensor1, tensor2", "bool: bool1, bool2"]
    )
    experiment_data.config(
        depth=2, 
        types=["int", "str"], 
        name=["int: int1, int2", "str: str1, str2"]
    )

    # Print configured data structure
    experiment_data.pop()

    # Configure bundling and order
    order = {"depth1": "tensor", "depth2": "tensor", "depth1": "int"}
    experiment_data.bundle(cardinal="2", order=order)

    # Access data using x.data.variable_name
    print(experiment_data.data_tensor1_1)  # Access data using x.data.variable_name syntax

    # Print bundle dictionary
    print(experiment_data.dict())

    # Print variable memory addresses
    print(experiment_data.adrs())

if __name__ == "__main__":
    main()
