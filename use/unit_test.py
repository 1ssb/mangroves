import unittest
import torch
from mangroves.mangrove import Mangrove

class TestMangrove(unittest.TestCase):

    def test_initial_config(self):
        m = Mangrove()
        self.assertEqual(m.depths, {0: [int, float, str, torch.Tensor]})
        self.assertEqual(m.data, {})
        self.assertEqual(m.types, {})
        self.assertEqual(m.levels, {})

    def test_depth_zero_cannot_be_modified(self):
        m = Mangrove()
        with self.assertRaises(Exception) as context:
            m.config(0, [int, float])
        self.assertTrue("Depth 0 is pre-configured and cannot be modified." in str(context.exception))

    def test_add_data_to_unconfigured_depth(self):
        m = Mangrove()
        with self.assertRaises(Exception) as context:
            m.add_data(3, int, ["z"], [5])
        self.assertTrue("Depth 3 not configured. Please configure the depth first." in str(context.exception))

    def test_disallowed_type_at_configured_depth(self):
        m = Mangrove()
        m.config(1, [int, torch.Tensor])
        with self.assertRaises(Exception) as context:
            m.add_data(1, str, ["s"], ["test"])
        self.assertTrue("Type <class 'str'> is not allowed at depth 1." in str(context.exception))

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
        with self.assertRaises(Exception) as context:
            m.add_data(1, int, ["x"], [1, 2])
        self.assertTrue("Length of variable names and values must match." in str(context.exception))

    def test_variable_name_conflict(self):
        m = Mangrove()
        m.config(1, [int, torch.Tensor])
        m.add_data(1, int, ["x"], [1])
        with self.assertRaises(Exception) as context:
            m.add_data(1, int, ["x"], [2])
        self.assertTrue("Variable name x is already in use." in str(context.exception))

    def test_attribute_access_and_modification(self):
        m = Mangrove()
        m.config(1, [int, torch.Tensor])
        m.add_data(1, int, ["x"], [1])
        self.assertEqual(m.x, 1)
        with self.assertRaises(Exception) as context:
            m.x = "string"
        self.assertTrue("Value must be of type <class 'int'>." in str(context.exception))
        m.x = 10
        self.assertEqual(m.x, 10)

    def test_nonexistent_attribute_access(self):
        m = Mangrove()
        with self.assertRaises(Exception) as context:
            _ = m.w
        self.assertTrue("No such attribute: w" in str(context.exception))

    def test_push_to_depth(self):
        m = Mangrove()
        m.config(1, [int, torch.Tensor])
        m.add_data(0, int, ["z"], [5])
        m.push(1, "z")
        self.assertEqual(m.levels, {"z": 1})

    def test_push_nonexistent_variable(self):
        m = Mangrove()
        m.config(1, [int])
        with self.assertRaises(Exception) as context:
            m.push(1, "non_existent_var")
        self.assertTrue("non_existent_var is not at depth 0. Cannot push." in str(context.exception))

    def test_push_variable_not_at_depth_zero(self):
        m = Mangrove()
        m.config(1, [int])
        m.add_data(1, int, ["x"], [1])
        with self.assertRaises(Exception) as context:
            m.push(1, "x")
        self.assertTrue("x is not at depth 0. Cannot push." in str(context.exception))

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
        with self.assertRaises(Exception) as context:
            m.shift(2, "x")
        self.assertTrue("Type <class 'int'> is not allowed at depth 2." in str(context.exception))

    def test_valid_inosc(self):
        m = Mangrove()
        m.config(1, [int, float])
        m.config(2, [float, torch.Tensor])
        try:
            inosc_key = m.inosc([(1, int), (2, float)])
            self.assertTrue(inosc_key in m.inosculations)
        except Exception as e:
            self.fail(f"Valid inosculation raised an exception: {e}")

    def test_multiple_valid_inosc(self):
        m = Mangrove()
        m.config(1, [int, float])
        m.config(2, [float, torch.Tensor])
        try:
            inosc_key1 = m.inosc([(1, int), (2, float)])
            inosc_key2 = m.inosc([(1, float), (2, torch.Tensor)])
            self.assertTrue(inosc_key1 in m.inosculations)
            self.assertTrue(inosc_key2 in m.inosculations)
        except Exception as e:
            self.fail(f"Multiple valid inosculations raised an exception: {e}")

    def test_unsorted_valid_inosc(self):
        m = Mangrove()
        m.config(1, [int, float])
        m.config(2, [float, torch.Tensor])
        try:
            inosc_key = m.inosc([(2, float), (1, int)])
            self.assertTrue(inosc_key in m.inosculations)
        except Exception as e:
            self.fail(f"Unsorted valid inosculation raised an exception: {e}")

    def test_repeated_valid_inosc(self):
        m = Mangrove()
        m.config(1, [int, float])
        m.config(2, [float, torch.Tensor])
        try:
            inosc_key1 = m.inosc([(1, int), (2, float)])
            inosc_key2 = m.inosc([(1, int), (2, float)])
            self.assertTrue(inosc_key1 in m.inosculations)
            self.assertTrue(inosc_key2 in m.inosculations)
            self.assertEqual(inosc_key1, inosc_key2)
        except Exception as e:
            self.fail(f"Repeated valid inosculation raised an exception: {e}")

    def test_valid_uproot(self):
        m = Mangrove()
        m.config(1, [int])
        m.add_data(1, int, ["x"], [1])
        try:
            m.uproot(1, "x")
            self.assertEqual(m.levels["x"], 0)
        except Exception as e:
            self.fail(f"Valid uproot raised an exception: {e}")

    def test_invalid_uproot_nonexistent_variable(self):
        m = Mangrove()
        m.config(1, [int])
        with self.assertRaises(Exception) as context:
            m.uproot(1, "non_existent_var")
        self.assertTrue("Variable non_existent_var does not exist." in str(context.exception))

    def test_invalid_uproot_variable_at_depth_zero(self):
        m = Mangrove()
        m.config(1, [int])
        m.add_data(0, int, ["z"], [5])
        with self.assertRaises(Exception) as context:
            m.uproot(1, "z")
        self.assertTrue("Variable z is already at depth 0. Cannot uproot." in str(context.exception))

    def test_invalid_uproot_wrong_depth(self):
        m = Mangrove()
        m.config(1, [int])
        m.config(2, [float])
        m.add_data(2, float, ["y"], [3.14])
        with self.assertRaises(Exception) as context:
            m.uproot(1, "y")
        self.assertTrue("Variable y is not at depth 1. Cannot uproot." in str(context.exception))

if __name__ == '__main__':
    unittest.main()
