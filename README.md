# Mangrove: A Dynamic Data Management System for Advanced AI Applications
#### Phase 7: Final Verification phase in progress.
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
from mangroves.mangrove import Mangrove, MangroveException
```

For further understanding of usages use the ```./use``` directory files.

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
