# A Use case on how to use Mangroves

import torch
from mangroves.mangrove import Mangrove

def main():
    try:
        # 1. Initializing the Mangrove object
        print("Initializing Mangrove object...")
        mangrove = Mangrove()
        
        # 2. Configuring depths
        print("Configuring depth 1...")
        mangrove.config(1, [int, float, torch.Tensor])
        print("Depth 1 configured.")
        
        # 3. Adding data to depths
        print("Adding data to depth 1...")
        mangrove.add_data(1, int, ["age"], [25])
        mangrove.add_data(1, float, ["height"], [5.9])
        print("Data added to depth 1.")

        print("Adding tensor data to depth 0 (pre-configured)...")
        mangrove.add_data(0, torch.Tensor, ["tensor_data"], [torch.tensor([1, 2, 3])])
        print("Tensor data added to depth 0.")

        # 4. Creating inosculation
        print("Creating inosculation between int variables at depth 1 and tensor variables at depth 0...")
        inosc_key = mangrove.inosc([(1, int), (0, torch.Tensor)])
        print(f"Inosculation created with key: {inosc_key}")

        # 5. Uprooting cojoined data
        print("Uprooting cojoined data based on inosculation...")
        cojoined_data = mangrove.uproot(inosc_key)
        print(f"Cojoined data: {cojoined_data}")

        # 6. Fetching variable names and their values
        print("Fetching variable names for depth 1...")
        var_names_depth1 = mangrove.var(1)
        print(f"Variable names at depth 1: {var_names_depth1}")

        print("Fetching index of variables...")
        index_data = mangrove.index()
        print(f"Index data: {index_data}")

        # 7. Pushing a variable from depth 0 to depth 1
        print("Pushing 'tensor_data' from depth 0 to depth 1...")
        mangrove.push(1, "tensor_data")
        
        # 8. Shifting a variable from one depth to another
        print("Shifting 'age' from depth 1 to depth 0...")
        mangrove.shift(0, 'age')

        # 9. Using `tocuda` to move tensors to GPU, if available
        print("Attempting to move tensors to GPU...")
        mangrove.tocuda()
        
        # 10. Displaying a summary
        print("Displaying Mangrove summary...")
        summary = mangrove.summary()
        print(f"Summary: {summary}")

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()


