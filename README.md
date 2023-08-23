# Mangrove

## A data structure for multiple key types and keys that index underlying data variables or structures. 

### Phase 1: Create a data structure that can input multiple keys of several types which must have the same cardinality. (Complete)

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

### Possible Applications

- Experiment and data management in scientific research.
- Configuration and tracking of complex system parameters.
- Customizable data structures for various applications.
