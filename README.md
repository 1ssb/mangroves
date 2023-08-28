# Mangrove1.0: A Dynamic Data Management System for Advanced AI Applications

Unlock a new paradigm of data management with Mangrove—a high-density, multi-dimensional data structure engineered to streamline variable handling across various depths and types. Mangrove simplifies data management in Robotics, NLP, computer vision and other AI applications by providing a versatile and efficient way to handle variables of varying types and depths. By using Mangrove, you can focus more on your AI model development and less on data organization.

## Description
Mangrove is a utility data structure designed to manage various types of data within multi-layered superstructures, denoted by 'depths.' It offers high-fidelity operations, including the ability to transfer values to the GPU for accelerated computing. As the program runs, Mangrove naturally organizes data in a structured manner based on its importance and requirements. It can move priority tensors to the GPU for computation and later retrieve them, adding them back as attributes within the same instance. This provides an end-to-end management utility well-suited for large-scale, episodic training processes and data acquisition systems, making it highly versatile and applicable to a range of use cases.

## Key Features
- **Dynamic Configuration**: Use the `config()` function to easily specify data type constraints for various depths. The system prevents incompatible configurations.
- **Data Ingestion**: With `add_data()`, you can add new variables dynamically while ensuring they meet the established type and depth requirements.
- **Insightful Summaries**: The `summary()` method provides a quick, detailed overview of your data's types, depths, and more.
- **Dynamic Access**: Use Pythonic `__getattr__` and `__setattr__` methods for on-the-fly variable access, with robust error handling.
- **Result Caching**: We use caching to store local information to prevent too many Dictionary lookups.

## Special Functionalities
- **Seamless GPU Acceleration**: The `tocuda` method effortlessly transfers your data to a CUDA-enabled GPU.
- **Dynamic Depth Management**: The `push` functionality enables you to adjust variable depths on-the-fly, optimizing your data organization.
- **Depth 0**: A special layer for untyped data, providing a flexible foundation for early-stage projects.

## Methods
- `config()`: Define type constraints for variable depths.
- `add_data()`: Add variables dynamically, with automatic type and depth checks.
- `summary()`: Get an insightful snapshot of the state of your data.
- `__getattr__` and `__setattr__`: Dynamic variable access with robust error handling.
- `tocuda()`: Streamline the transfer of variables to CUDA-enabled GPUs.
- `push()`: Modify the depth of a variable dynamically.
- `shift()`: Move any variable to a destination depth.

## Requirements

- CUDA-enabled GPU
- Python 3.x
- Torch >=1.8
- Sympy
  
## Installation

### Option 1: Use the PyPI library

```bash
pip install mangroves
```

### Option 2: Clone the GitHub Repository

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

## Usage

You can now import the Mangroves library in your Python code and use them directly for instantiation. A set of use cases is provided below:

```python
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

```

## License

The package is licensed under the MIT License.

#### Acknowledgment: Thanks to Mr. Abhaas Goyal ([@abhaasgoyal](https://github.com/abhaasgoyal)) for productive conversations. 

## Contributions

We welcome contributions to Mangrove! If you're looking to contribute, you can do so in the following ways:

### Bug Reports and Feature Requests
If you find a bug or have an idea for a new feature, please start by opening an issue in the GitHub repository. This allows us to collaborate and ensure that the issue is reproducible and distinct.

### Code Contributions
1. Fork the repository to your own GitHub account.
2. Clone the repository to your local machine.
3. Create a new branch for your changes.
4. Make your changes and commit them with a clear and descriptive message.
5. Push the changes back to your fork on GitHub.
6. Create a Pull Request from your fork to the original repository.

Before submitting a Pull Request, please ensure that your code adheres to the style guidelines of the project and that any tests are passing. Your contributions, whether they're small documentation updates or new features, are highly appreciated! Kindly update `unit_tests.py` with your own cases and make sure it maintains backward compatibility.

### Contact

If you have specific questions about contributing or you've identified a sensitive or urgent issue, you can reach out via email at [Subhransu.Bhattacharjee@anu.edu.au](mailto:Subhransu.Bhattacharjee@anu.edu.au).

## Citation

If you find this code useful in your research, please cite as:

```latex
@misc{Mangrove2023,
  author = {Subhransu S. Bhattacharjee},
  title = {Mangrove: A Dynamic Data Management Engine for Advanced AI Applications},
  year = {2023},
  note = {GitHub repository},
  howpublished = {\url{https://github.com/1ssb/mangroves}}
}
```
