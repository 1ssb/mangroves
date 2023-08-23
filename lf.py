class TensorTree:
    def __init__(self):
        self.tree = {}

    def add_tensor(self, key, value):
        if isinstance(key, str) and isinstance(value, (int, float, list, tuple)):
            self.tree[key] = value
        else:
            raise TypeError("Key must be a string and value must be an int, float, list or tuple")

    def get_tensor(self, key):
        if key in self.tree:
            return self.tree[key]
        else:
            raise KeyError(f"{key} not found in tree")

    def __str__(self):
        return str(self.tree)

# Example usage
my_tree = TensorTree()
my_tree.add_tensor("tensor1", [1, 2, 3])
my_tree.add_tensor("tensor2", (4, 5, 6))
my_tree.add_tensor("tensor3", 7)
print(my_tree)
print(my_tree.get_tensor("tensor1"))
