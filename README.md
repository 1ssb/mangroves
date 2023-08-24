# Mangrove Project

### Pending---Phase 2: DeepCopy to GPU memory and GPU operations return updated mangrove to the CPU. (In progress tensor.py) Abhaas kindly read the description, and the mangrove and main codes and replicate all functionalities for PyTorch Tensor and check if we can pass the index dictionary directly to the GPU for unpacking and operations.

### Pending---Phase 3: Perform all unit tests and push to production in PyPI library. As installable package pip install mangrove.

## Mangrove - A fully customizable High Dimensional High-Density Liquid Data Structure for next-gen AI

Mangrove is a custom data structure that provides dynamic configuration and management of variables across multiple depths and data types. It offers flexible configuration, ordered bundling, memory address tracking, and more. Use cases available in main.py.

## Functionality

### Attributes

- `depths`: A dictionary that holds depth values as keys and corresponding allowed types as values.
- `data`: A dictionary to store variable names as keys and their associated values.
- `types`: A dictionary that maps variable names to their data types.
- `levels`: An internal dictionary that associates variable names with their depths.
- `index`: A dictionary which stores all the variables stored in a certain depth for a particular data type.

### Constructor

The constructor `__init__` initializes the Mangrove object by creating empty dictionaries for depths, data, types, levels, and bindings.

### Configuring Depths and Types

The `config` method allows the configuration of depths and associated types. It takes depth and a list of types as arguments. If the given depth requires a preceding depth to be configured, it checks for its presence in the depths dictionary. If not, it raises a ValueError.

### Adding Data

The `add_data` method adds data to the Mangrove object. It requires a depth, type, variable name(s) `var`, and an optional value. It verifies that the provided depth and type are configured and then adds the variable names and associated values to the data dictionary, along with their types and depths.

### Summary

The `summary` method generates a summary of the data stored in the Mangrove object. It creates a dictionary where variable names are keys, and each entry includes the variable's type and depth.

### Dynamic Attribute Access

The methods `__getattr__` and `__setattr__` are used to dynamically access and set attributes of the Mangrove object. If the attribute is a variable name stored in data, `__getattr__` returns the associated value. If it's a variable name in bindings, the corresponding value is returned. If the attribute doesn't match any stored variables, an AttributeError is raised.

### String Representation

The `__repr__` method provides a string representation of the Mangrove object, showing its data dictionary.

### Variable Listing

The `var` method allows listing variable names based on specified depth and data type filters. If depth and/or data_type are provided, the method returns a list of variable names that match the given criteria.

### Indexing

The `index` method binds variables together based on specified depths and data types as a dictionary. It can be parsed for downstream applications and creates a natural indexing order to represent dimensionality.


## Possible Applications

### Computer Vision Applications:

- **Image Classification:** Mangrove's dynamic configuration simplifies image classification setups, streamlining variable management for image data and labels.

- **Object Detection:** Efficiently organize object detection datasets by leveraging Mangrove's variable depth and type configuration for bounding box coordinates and class labels.

- **Facial Recognition:** Mangrove's ordered bundling aids in managing facial recognition datasets, making it easy to arrange face images and associated identities.

- **Image Segmentation:** Flexibly handle image segmentation tasks with Mangrove's variable configurations for input images and masks, accommodating pixel-level annotations.

- **Medical Imaging:** Mangrove's versatile data management suits medical imaging tasks, supporting multi-modal data, annotations, and classifications across medical image formats.

- **Autonomous Vehicles:** Simplify the organization of sensor data from autonomous vehicles with Mangrove's depth-based configuration, accommodating various data types like LiDAR, cameras, and radar.

### Natural Language Processing (NLP) Applications:

- **Sentiment Analysis:** Utilize Mangrove's ordered bundling to efficiently manage sentiment analysis datasets, pairing text samples with sentiment labels for model training.

- **Text Summarization:** Mangrove's dynamic configuration caters to text summarization tasks, efficiently managing source texts and their corresponding summaries.

- **Question Answering:** Effortlessly set up question answering tasks with Mangrove by configuring variables for passages, questions, and answers, ensuring dataset coherence.

- **Language Translation:** Leverage Mangrove's flexibility to configure multilingual translation datasets, maintaining alignment between source and target texts for translation models.

- **Named Entity Recognition:** Harness Mangrove's data organization capabilities for labeled entity management, supporting named entity recognition tasks.

### Other AI Applications:

- **Healthcare Predictive Modeling:** Mangrove's dynamic configuration and data management capabilities are valuable for healthcare predictive modeling, facilitating diverse patient data organization.

- **Financial Analysis:** Utilize Mangrove for financial data handling, benefiting from ordered bundling and variable management in predictive analytics, fraud detection, and portfolio optimization.

- **Recommendation Systems:** Efficiently set up recommendation system experiments with Mangrove, organizing user-item interaction data and recommendation targets using its flexible configuration.

- **Gaming AI:** Mangrove efficiently organizes game data for training AI agents, managing game states, actions, and rewards, facilitating reinforcement learning experiments.

- **Energy Management:** Effectively organize sensor data for energy consumption analysis using Mangrove's data management capabilities, optimizing energy usage in buildings and industrial setups.

### Econometrics and Time Series Data Management:

- **Data Organization:** Leverage Mangrove's dynamic configuration to efficiently manage and organize econometrics and time series datasets.

- **Variable Relationships:** Easily analyze relationships between variables with Mangrove's structured data setup, supporting regression analysis and correlation assessments.

- **Time Series Handling:** Configure variables to represent different time periods for streamlined management and analysis of time series data.

- **Forecasting and Modeling:** Utilize Mangrove's ordered bundling to set up forecasting experiments, bundling historical data, exogenous factors, and outcomes.

- **Financial Data Management:** Efficiently manage financial time series data (e.g., stock prices, economic indicators) with Mangrove, aiding in portfolio optimization and risk assessment.

- **Impact Analysis:** Structure scenarios and analyze the impact of economic events or policy changes using Mangrove's dynamic data management capabilities.

