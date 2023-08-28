# A Use case on how to use Mangroves

import torch
from mangroves.mangrove import Mangrove, MangroveException

def main():
    try:
        print("Initializing Mangrove object...")
        mangrove = Mangrove()

        print("Configuring depth 1...")
        mangrove.config(1, [int, float, torch.Tensor])
        print("Depth 1 configured.")

        print("Adding data to depth 1...")
        mangrove.add_data(1, int, ["age"], [25])
        mangrove.add_data(1, float, ["height"], [5.9])
        print("Data added to depth 1.")

        print("Adding tensor data to depth 0 (pre-configured)...")
        mangrove.add_data(0, torch.Tensor, ["tensor_data"], [torch.tensor([1, 2, 3])])
        print("Tensor data added to depth 0.")

        print("Directly accessing variable 'age'...")
        print("Accessing directly:", mangrove.age)

        print("Updating the 'age' variable...")
        mangrove.age = 26
        print("Age updated.")

        print("Accessing summary...")
        summary = mangrove.summary()
        print("Summary:", summary)

        print("Getting variables at depth 1...")
        print("Variables at depth 1:", mangrove.var(depth=1))

        print("Getting variables of type int...")
        print("Variables of type int:", mangrove.var(data_type=int))

        print("Indexing at depth 1...")
        print("Indexing at depth 1:", mangrove.index(depth=1))

        print("Pushing 'tensor_data' to depth 1...")
        mangrove.push(1, "tensor_data")
        print("'tensor_data' pushed to depth 1.")

        print("Moving all tensor variables to CUDA...")
        mangrove.tocuda(data_type=torch.Tensor)
        print("All tensor variables moved to CUDA.")

        # Retrieving tensor_data from CUDA and adding it to depth 1
        print("Retrieving 'tensor_data' back from CUDA...")
        tensor_data_cpu = mangrove.tensor_data.cpu()
        print("Retrieved 'tensor_data' back from CUDA.")

        print("Adding retrieved 'tensor_data' to depth 1...")
        mangrove.add_data(1, torch.Tensor, ["retrieved_tensor_data"], [tensor_data_cpu])
        print("Retrieved 'tensor_data' added to depth 1.")

        print("Adding tensor data to depth 0 (pre-configured)...")
        mangrove.add_data(0, torch.Tensor, ["tensor_data"], [torch.tensor([1, 2, 3])])
        print("Tensor data added to depth 0.")
        
        # Test shift operation
        print("Shifting 'tensor_data' from depth 0 to depth 1...")
        mangrove.shift(to=1, variable_name="tensor_data")
        print("'tensor_data' shifted to depth 1.")

        print("Attempting to shift 'age' to depth that doesn't support its type...")
        try:
            mangrove.shift(to=2, variable_name="age")
        except MangroveException as e:
            print("Expected error occurred:", e)
        
        print("Shifting 'age' back to depth 0...")
        mangrove.shift(to=0, variable_name="age")
        print("'age' shifted to depth 0.")

    except MangroveException as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()

