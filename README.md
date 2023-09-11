# Mangrove: A Dynamic Data Management System for Advanced AI Applications

Unlock streamlined data management with Mangrove, a multi-dimensional structure that simplifies variable handling across Robotics, NLP, computer vision and graphics. Focus more on model development and less on data organization.

## Description
Mangrove is a utility data structure designed to manage various types of data within multi-layered superstructures, denoted by 'depths.' It offers high-fidelity operations, including the ability to transfer values to the GPU for accelerated computing. As the program runs, Mangrove naturally organizes data in a structured manner based on its importance and requirements. It can move priority tensors to the GPU for computation and later retrieve them, adding them back as attributes within the same instance. This provides an end-to-end management utility well-suited for large-scale, episodic training processes and data acquisition systems, making it highly versatile and applicable to a range of use cases.

## Key Features
- **Dynamic Configuration**: Use the `config()` function to easily specify data type constraints for various depths. The system prevents incompatible configurations.
- **Data Ingestion**: With `add_data()`, you can add new variables dynamically while ensuring they meet the established type and depth requirements.
- **Insightful Summaries**: The `summary()` method provides a quick, detailed overview of your data's types, depths, and more.
- **Dynamic Access**: Use Pythonic `__getattr__` and `__setattr__` methods for on-the-fly variable access, with robust error handling.
- **Result Caching**: We use caching to store local information to prevent too many Dictionary lookups.

## Special Functionalities
- **Seamless GPU Acceleration**: The `tocuda()` method effortlessly transfers your data to a CUDA-enabled GPU.
- **Dynamic Depth Management**: The `push()` functionality enables you to adjust variable depths on-the-fly, optimizing your data organization.
- **Depth 0**: A special layer for untyped data, providing a flexible foundation for early-stage projects.
- **Inosculation**: This function allows for direct value manipulation across depths, enabling more intricate data-flow patterns. The term "inosculation" is used to signify the merging or interlocking of elements, akin to the way natural systems like trees or capillaries inosculate.
- **Uprooting**: The uproot method allows you to move a variable from its current depth to the root (depth 0), facilitating easier access for testing.

## Methods
- `config()`: Define type constraints for variable depths.
- `add_data()`: Add variables dynamically, with automatic type and depth checks.
- `summary()`: Get an insightful snapshot of the state of your data.
- `__getattr__` and `__setattr__`: Dynamic variable access with robust error handling.
- `tocuda()`: Streamline the transfer of variables to CUDA-enabled GPUs.
- `push()`: Modify the depth of a variable dynamically.
- `inosc()`: Directly manipulate values across depths.
- `uproot()`: Move variables to root depth.
- `shift()`: Move any variable to a destination depth.

## Requirements
- CUDA-enabled GPU
- Python 3.x
- Torch >=1.8
- Sympy
  
## Installation

```bash
pip install mangroves
```

In python environemnt utilise the class as:

```python
# Import the Mangrove library
from mangroves.mangrove import Mangrove as M
# Instantiate Mangrove class
M = M()
```
Its that simple. Make sure to always use the PyPI instead of the repo in case the released updates have not be tested.

## Usage

You can now import Mangroves from the [PyPI](https://pypi.org/project/mangroves/) library in your Python code and use them directly for instantiation. A set of use cases is provided in ```use/main.py```.

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

```bibtex
@misc{Mangrove2023,
  author = {Subhransu S. Bhattacharjee},
  title = {Mangrove: A Dynamic Data Management Engine for Advanced AI Applications},
  year = {2023},
  note = {GitHub repository},
  howpublished = {\url{https://github.com/1ssb/mangroves}}
}
```
