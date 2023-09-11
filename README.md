# Mangrove: A Dynamic Data Management System for Advanced AI Applications

Unlock streamlined data management with Mangrove, a multi-dimensional structure that simplifies variable handling across Robotics, NLP, computer vision and graphics. Focus more on model development and less on data organization.

## Description
Mangrove is a utility data structure designed to manage various types of data within multi-layered superstructures, denoted by 'depths.' It offers high-fidelity operations, including the ability to transfer values to the GPU for accelerated computing. As the program runs, Mangrove naturally organizes data in a structured manner based on its importance and requirements. It can move priority tensors to the GPU for computation and later retrieve them, adding them back as attributes within the same instance. This provides an end-to-end management utility well-suited for large-scale, episodic training processes and data acquisition systems, making it highly versatile and applicable to a range of use cases.

## Key Features
- **Dynamic Configuration**: Use `config()` for data type constraints per depth.
- **Data Ingestion**: `add_data()` adds variables dynamically with type checks.
- **Insightful Summaries**: `summary()` for quick data overviews.
- **Dynamic Access**: Use `__getattr__` and `__setattr__` for variable access.
- **Result Caching**: Local caching minimizes Dictionary lookups.
- **Deleting Restrictions**: `deleter()` allows you to safely delete the instance and free up memory.

## Special Functionalities
- **Seamless GPU Acceleration**: `tocuda()` for easy data transfer to CUDA GPUs.
- **Dynamic Depth Management**: `push()` adjusts variable depths dynamically.
- **Depth 0**: Untyped data layer for flexibility.
- **Inosculation**: `inosc()` allows direct value accessing and joining across depths. Inspired from the structure in trees.
- **Uprooting**: `uproot()` moves variables to depth 0.
- **Deleter**: `deleter()` deletes the instance and its data.

## Methods
- `config()`: Define type constraints.
- `add_data()`: Add variables with checks.
- `summary()`: Overview of data state.
- `__getattr__` and `__setattr__`: Variable access.
- `tocuda()`: Transfer data to CUDA GPUs.
- `push()`: Modify variable depth.
- `inosc()`: Manipulate values across depths.
- `uproot()`: Move variables to root.
- `shift()`: Shift variables between depths.
- `deleter()`: Delete the instance and its data.

## Requirements
- CUDA-enabled GPU
- Python 3.x
- Torch >=1.8
- Sympy
  
## Installation

```bash
pip install mangroves
```

## Usage

You can now import Mangroves from the [PyPI](https://pypi.org/project/mangroves/) library in your Python code and use them directly for instantiation. A set of use cases is provided in ```./use/main.py```.

In python environemnt utilise the class as:

```python
# Import the Mangrove library
from mangroves.mangrove import Mangrove as M
# Instantiate Mangrove class
M = M()
```
Its that simple. Make sure to always use the PyPI instead of cloning the repo, in case the unreleased commits have not been tested.

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

If you find this code useful in your research, please leave a star and cite as:

```bibtex
@misc{Mangrove2023,
  author = {Subhransu S. Bhattacharjee},
  title = {Mangrove: A Dynamic Data Management Engine for Advanced AI Applications},
  year = {2023},
  note = {GitHub repository},
  howpublished = {\url{https://github.com/1ssb/mangroves}}
}
```
