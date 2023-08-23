# Mangrove

### Phase 1: Create a data structure that can input multiple keys of several types which must have the same cardinality to bundle. (Complete)

#### Unit Testing: Incomplete

### Phase 2: DeepCopy to GPU memory and GPU operations return updated mangrove to the CPU. (In progress)

## Mangrove - A Custom Data Structure

Mangrove is a custom data structure that provides dynamic configuration and management of variables across multiple depths and data types. It offers flexible configuration, ordered bundling, memory address tracking, and more.

## Functionality

Mangrove class provides the following functionalities:

### Dynamic Configuration

- `config(depth, types, name)`: Configure variables at specified depth levels with allowed data types.

### Variable Management

- `pop(variable_name)`: Display the ordered structure or access data for a specific variable.

### Bundling and Order

- `bundle(cardinal, order)`: Configure bundling rules with required cardinality and order.

### Memory Address Tracking

- `adrs()`: Get memory addresses of variables stored in the Mangrove instance.

### Bundle Dictionary

- `dict()`: Retrieve a dictionary containing bundling information.

## Possible Applications

### Computer Vision Applications:

- Image Classification: Mangrove's dynamic configuration simplifies image classification setups, streamlining variable management for image data and labels.

- Object Detection: Efficiently organize object detection datasets by leveraging Mangrove's variable depth and type configuration for bounding box coordinates and class labels.

- Facial Recognition: Mangrove's ordered bundling aids in managing facial recognition datasets, making it easy to arrange face images and associated identities.

- Image Segmentation: Flexibly handle image segmentation tasks with Mangrove's variable configurations for input images and masks, accommodating pixel-level annotations.

- Medical Imaging: Mangrove's versatile data management suits medical imaging tasks, supporting multi-modal data, annotations, and classifications across medical image formats.

- Autonomous Vehicles: Simplify the organization of sensor data from autonomous vehicles with Mangrove's depth-based configuration, accommodating various data types like LiDAR, cameras, and radar.

### Natural Language Processing (NLP) Applications:

- Sentiment Analysis: Utilize Mangrove's ordered bundling to efficiently manage sentiment analysis datasets, pairing text samples with sentiment labels for model training.

- Text Summarization: Mangrove's dynamic configuration caters to text summarization tasks, efficiently managing source texts and their corresponding summaries.

- Question Answering: Effortlessly set up question answering tasks with Mangrove by configuring variables for passages, questions, and answers, ensuring dataset coherence.

- Language Translation: Leverage Mangrove's flexibility to configure multilingual translation datasets, maintaining alignment between source and target texts for translation models.

- Named Entity Recognition: Harness Mangrove's data organization capabilities for labeled entity management, supporting named entity recognition tasks.

### Other AI Applications:

- Healthcare Predictive Modeling: Mangrove's dynamic configuration and data management capabilities are valuable for healthcare predictive modeling, facilitating diverse patient data organization.

- Financial Analysis: Utilize Mangrove for financial data handling, benefiting from ordered bundling and variable management in predictive analytics, fraud detection, and portfolio optimization.

- Recommendation Systems: Efficiently set up recommendation system experiments with Mangrove, organizing user-item interaction data and recommendation targets using its flexible configuration.

- Gaming AI: Mangrove efficiently organizes game data for training AI agents, managing game states, actions, and rewards, facilitating reinforcement learning experiments.

- Energy Management: Effectively organize sensor data for energy consumption analysis using Mangrove's data management capabilities, optimizing energy usage in buildings and industrial setups.
