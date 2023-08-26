# Mangrove: A Dynamic Data Management System for Advanced AI Applications

Unlock a new paradigm of data management with Mangrove—a high-density, multi-dimensional data structure engineered to streamline variable handling across various depths and types. Mangrove simplifies data management in Robotics, NLP, computer vision and other AI applications by providing a versatile and efficient way to handle variables of varying types and depths. By using Mangrove, you can focus more on your AI model development and less on data organization.

# Description
Mangrove is a utility data structure designed to manage various types of data within multi-layered superstructures, denoted by 'depths.' It offers high-fidelity operations, including the ability to transfer values to the GPU for accelerated computing. As the program runs, Mangrove naturally organizes data in a structured manner based on its importance and requirements. It can move priority tensors to the GPU for computation and later retrieve them, adding them back as attributes within the same instance. This provides an end-to-end management utility well-suited for large-scale, episodic training processes and data acquisition systems, making it highly versatile and applicable to a range of use cases.

## Installation

#### Option 1: Use the PyPI library

```bash
pip install mangroves
```

#### Option 2: Clone the GitHub Repository

1. Open your terminal and run the following command to clone the repository:
    ```bash
    git clone https://github.com/1ssb/mangroves.git
    ```
   
2. Navigate to the cloned repository:
    ```bash
    cd mangroves
    ```

3. Install the package:
    ```bash
    pip install .
    ```

### Usage

You can now import the Mangroves library in your Python code as follows:

```python
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
```


## License

The package is licensed under the MIT License.

## Citation

If you find this code useful in your research, please cite as:

```bash
@misc{Mangrove2023,
  author = {Subhransu S. Bhattacharjee},
  title = {Mangrove: Dynamic Data Management Engine for Advanced AI Applications},
  year = {2023},
  note = {GitHub repository},
  howpublished = {\url{https://github.com/1ssb/mangroves}}
}
```
