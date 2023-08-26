# A Use case on how to use Mangroves

import torch
from mangroves.mangrove import Mangrove, MangroveException

def main():
    try:
        print("Initializing Mangrove object...")
        mangrove = Mangrove()

        print("Configuring depth 1...")
        mangrove.config(1, [int, float])
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

    except MangroveException as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
