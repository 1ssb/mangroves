import unittest
import torch
from mangroves.mangrove import Mangrove, MangroveException

class TestMangrove(unittest.TestCase):

    def test_initial_config(self):
        m = Mangrove()
        self.assertEqual(m.depths, {0: [int, float, str, torch.Tensor]})
        self.assertEqual(m.data, {})
        self.assertEqual(m.types, {})
        self.assertEqual(m.levels, {})

    def test_depth_zero_cannot_be_modified(self):
        m = Mangrove()
        with self.assertRaises(MangroveException):
            m.config(0, [int, float])

    def test_add_data_to_unconfigured_depth(self):
        m = Mangrove()
        with self.assertRaises(MangroveException):
            m.add_data(3, int, ["z"], [5])

    def test_disallowed_type_at_configured_depth(self):
        m = Mangrove()
        m.config(1, [int, torch.Tensor])
        with self.assertRaises(MangroveException):
            m.add_data(1, str, ["s"], ["test"])

    def test_add_data(self):
        m = Mangrove()
        m.config(1, [int, torch.Tensor])
        m.add_data(1, int, ["x", "y"], [1, 2])
        self.assertEqual(m.data, {"x": 1, "y": 2})
        self.assertEqual(m.types, {"x": int, "y": int})
        self.assertEqual(m.levels, {"x": 1, "y": 1})

    def test_add_data_mismatched_length(self):
        m = Mangrove()
        m.config(1, [int, torch.Tensor])
        with self.assertRaises(MangroveException):
            m.add_data(1, int, ["x"], [1, 2])

    def test_variable_name_conflict(self):
        m = Mangrove()
        m.config(1, [int, torch.Tensor])
        m.add_data(1, int, ["x"], [1])
        with self.assertRaises(MangroveException):
            m.add_data(1, int, ["x"], [2])

    def test_attribute_access_and_modification(self):
        m = Mangrove()
        m.config(1, [int, torch.Tensor])
        m.add_data(1, int, ["x"], [1])
        self.assertEqual(m.x, 1)
        with self.assertRaises(MangroveException):
            m.x = "string"
        m.x = 10
        self.assertEqual(m.x, 10)

    def test_nonexistent_attribute_access(self):
        m = Mangrove()
        with self.assertRaises(MangroveException):
            _ = m.w

    def test_push_to_depth(self):
        m = Mangrove()
        m.config(1, [int, torch.Tensor])
        m.add_data(0, int, ["z"], [5])
        m.push(1, "z")
        self.assertEqual(m.levels, {"z": 1})

    def test_push_nonexistent_variable(self):
        m = Mangrove()
        m.config(1, [int])
        with self.assertRaises(MangroveException):
            m.push(1, "non_existent_var")

    def test_push_variable_not_at_depth_zero(self):
        m = Mangrove()
        m.config(1, [int])
        m.add_data(1, int, ["x"], [1])
        with self.assertRaises(MangroveException):
            m.push(1, "x")
    
    def test_tocuda(self):
        m = Mangrove()
        m.config(1, [torch.Tensor])
        m.add_data(1, torch.Tensor, ["t"], [torch.zeros(5)])
        m.tocuda()
        self.assertTrue(m.t.is_cuda)
    
    def test_shift(self):
        m = Mangrove()
        m.config(1, [int, torch.Tensor])
        m.add_data(1, int, ["x"], [1])

        # Test valid shift operation
        m.shift(0, "x")
        self.assertEqual(m.levels["x"], 0)

        # Test invalid depth
        with self.assertRaises(MangroveException):
            m.shift(2, "x")

        # Test invalid data type at depth
        m.config(2, [float])
        with self.assertRaises(MangroveException):
            m.shift(2, "x")

if __name__ == '__main__':
    unittest.main()

