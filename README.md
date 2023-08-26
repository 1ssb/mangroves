# Mangrove Project

### Pending---Phase 2: Passing index dictionary to CUDA.

### Pending---Phase 3: Push to Release

## Mangrove: Dynamic Data Management Engine for Advanced AI Applications

Unlock a new paradigm of data management with Mangrove—a high-density, multi-dimensional data structure engineered to streamline variable handling across various depths and types. Explore example use-cases in `main.py`.

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
  howpublished = {\url{https://github.com/1ssb/mangrove}}
}












