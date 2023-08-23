# main.py
from mangrove import Mangrove  # Import the Mangrove class from mangrove.py

# Detailed use case scenario
def main():
    x = Mangrove()

    # Configure depth and data types
    x.config(depth=1, types=["tensor", "bool"], name=["tensor: tensor1, tensor2", "bool: bool1, bool2"])
    x.config(depth=2, types=["int", "str"], name=["int: int1, int2", "str: str1, str2"])

    # Print configured data structure
    x.pop()

    # Configure bundling and order
    order = {"depth1": "tensor", "depth2": "tensor", "depth1": "int"}
    x.bundle(cardinal="2", order=order)

    # Access data using x.data.variable_name
    print(x.data_tensor1_1)  # Access data using x.data.variable_name syntax

if __name__ == "__main__":
    main()
