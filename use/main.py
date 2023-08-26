# A Use case on how to use Mangroves

import torch
from mangrove import Mangrove, MangroveException  # Assuming the class is saved in a file called 'mangrove.py'

def main():
    try:
        # Initialize Mangrove object
        mangrove = Mangrove()

        # Configure depth 1 to support integers and floats
        mangrove.config(1, [int, float])

        # Add data to depth 1
        mangrove.add_data(1, int, ["age"], [25])
        mangrove.add_data(1, float, ["height"], [5.9])

        # Add tensor data to depth 0 (pre-configured)
        mangrove.add_data(0, torch.Tensor, ["tensor_data"], [torch.tensor([1, 2, 3])])

        # Access variable directly
        print("Accessing directly: ", mangrove.age)

        # Update the age variable directly
        mangrove.age = 26

        # Access summary
        summary = mangrove.summary()
        print("Summary: ", summary)

        # Get variables with a particular depth and type
        print("Variables at depth 1: ", mangrove.var(depth=1))
        print("Variables of type int: ", mangrove.var(data_type=int))

        # Index to get specific data
        print("Indexing at depth 1: ", mangrove.index(depth=1))

        # Push tensor_data to depth 1
        mangrove.push(1, "tensor_data")

        # Move all tensor variables to CUDA
        mangrove.tocuda(data_type=torch.Tensor)

    except MangroveException as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
