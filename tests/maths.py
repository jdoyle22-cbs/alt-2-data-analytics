"""
While usually tests would be in their own folder, there are few tests for this program
and thus they are in one root-level file.
"""

import unittest
from pathlib import Path
import sys

# Add parent directory to sys.path to make it possible to import lib
parent_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(parent_dir))

from lib import mode, median, mean
import statistics as st

# Test the "mode" function
class TestMode(unittest.TestCase):

    def test_empty(self):
        # Self explanatory
        with self.assertRaises(ValueError):
            mode([])
    
    def test_invalid_data(self):
        with self.assertRaises(ValueError):
            mode([0, 0, 1, 2, 3, 4, 5, 5, 5, "6", "6", 8, "eight"], check_data_validity=True)

    def test_result(self):
        # Statistics library is reliable, so we use it as a reference if our code is working correctly
        self.assertEqual(mode([1, 4, 5, 5, 5, 2, 0, 9]), st.mode([1, 4, 5, 5, 5, 2, 0, 9]))

    def test_missing_argument(self):
        with self.assertRaises(TypeError):
            mode()

# Test the "median" function
class TestMedian(unittest.TestCase):

    def test_empty(self):
        with self.assertRaises(ValueError):
            median([])

    def test_result(self):
        self.assertEqual(median([1, 4, 5, 5, 4, 2, 0, 9]), st.median([1, 4, 5, 5, 4, 2, 0, 9]))

    def test_missing_argument(self):
        with self.assertRaises(TypeError):
            median()

# Test the "mean" function
class TestMean(unittest.TestCase):

    def test_empty(self):
        with self.assertRaises(ValueError):
            mean([])
    
    def test_invalid_data(self):
        with self.assertRaises(ValueError):
            mean([0, 0, 1, 2, 3, 4, 5, 5, 5, "6", "6", 8, "eight"], check_data_validity=True)

    def test_result(self):
        self.assertEqual(mean([1, 4, 5, 5, 5, 2, 0, 9]), st.mean([1, 4, 5, 5, 5, 2, 0, 9]))

    def test_missing_argument(self):
        with self.assertRaises(TypeError):
            mean()

unittest.main()