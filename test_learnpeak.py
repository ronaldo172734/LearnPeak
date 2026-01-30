# test_learnpeak.py
"""
Tests for LearnPeak module.
"""

import unittest
from learnpeak import LearnPeak

class TestLearnPeak(unittest.TestCase):
    """Test cases for LearnPeak class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = LearnPeak()
        self.assertIsInstance(instance, LearnPeak)
        
    def test_run_method(self):
        """Test the run method."""
        instance = LearnPeak()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
