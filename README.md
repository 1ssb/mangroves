# Mangrove Project

### Phase 4: Preparing for release.

# Mangrove: Dynamic Data Management system for Advanced AI Applications

Unlock a new paradigm of data management with Mangrove—a high-density, multi-dimensional data structure engineered to streamline variable handling across various depths and types.

Mangrove simplifies data management in Robotics, NLP, computer vision and other AI applications by providing a versatile and efficient way to handle variables of varying types and depths. By using Mangrove, you can focus more on your AI model development and less on data organization.

## Key Features

### Data Structures
- **`depths`**: Map depth levels to their permitted data types.
- **`data`**: Key-value store for variable names and their values.
- **`types`**: Type mapping for variables.
- **`levels`**: Depth mapping for variables.
- **`index`**: An optimized way to access variables based on depth and data type.

### Dynamic Configuration

#### `config()`
- Configure depth-specific allowed data types.
- Throws an error if dependencies between depths are violated.

#### `add_data()`
- Dynamically add variables with optional initial values.
- Enforces pre-configured depth and data type constraints.
- Throws an error if the length of variable names and values do not match.

### Insightful Summaries

#### `summary()`
- Obtain a quick snapshot of variable types, depths, and more.

### Dynamic Access

#### `__getattr__` & `__setattr__`
- Retrieve or set variable values dynamically.
- Thorough error handling for invalid accesses.

### Other Methods

#### `__repr__()`
- Generate a string representation of the data store.

#### `var()`
- Filter variable names based on depth and type.

#### `index()`
- Easily organize and retrieve variables with built-in indexing based on depth and data type.

## Special Functionalities in Mangrove

### `tocuda`: Seamless Data Transfer to GPU (CUDA)

The `tocuda` method is a powerful tool designed to streamline the transition of your variables to the GPU, specifically if a CUDA-enabled GPU is available. This function enables you to efficiently utilize the power of GPUs for enhanced computation. When calling `tocuda`, you can specify optional parameters such as the desired depth or data type. Mangrove will automatically identify variables that match the specified criteria and move their tensor data to the CUDA memory space. This ensures seamless integration of GPU acceleration without the need for complex manual transfers.

### Depth 0: Pre-Configured Untyped Data

Mangrove introduces the concept of Depth 0, designed to manage untyped data efficiently. Depth 0 acts as a pre-configured container for various data types, including integers, floats, strings, and PyTorch tensors. This allows you to initialize variables without specifying their types, making it a versatile foundation for managing different data types in an organized manner. Any variable added at Depth 0 will be untyped and flexible, simplifying the early stages of variable management.

### `push`: Dynamic Variable Depth Modification

The `push` functionality within Mangrove facilitates dynamic and flexible management of variable depths. By utilizing `push`, you can adjust the depth of a variable, allowing it to seamlessly transition to a different level within the depth hierarchy. However, it's important to note that the `push` operation can only be performed on variables located at Depth 0. This feature is particularly valuable when you need to reorganize your variables based on evolving requirements or to optimize the efficiency of your data processing pipeline.

Incorporating these specialized functionalities enhances the versatility and adaptability of the Mangrove library, offering you dynamic control over variable depths, efficient GPU utilization, and a foundation for untyped data management.

## Practical Applications

### Computer Vision:
- From object detection to facial recognition, Mangrove enables flexible and efficient data management.

### NLP:
- Ideal for complex tasks like sentiment analysis, text summarization, and question answering.

### Healthcare & Finance:
- Enable predictive modeling in healthcare or optimize financial portfolios, all with Mangrove's dynamic capabilities.

### Recommendation Systems & Gaming:
- Simplify setup for recommendation algorithms or game state management for AI training.

### Energy & Econometrics:
- Optimize energy consumption or efficiently manage time-series data for econometric models.

# Citation

If you find this code useful in your research, please cite as:

@misc{Mangrove2023,
  author = {Subhransu S. Bhattacharjee},
  title = {Mangrove: Dynamic Data Management Engine for Advanced AI Applications},
  year = {2023},
  note = {GitHub repository},
  howpublished = {\url{https://github.com/1ssb/mangroves}}
}
