#!/usr/bin/env python
# coding: utf-8

"""A test to try out how Rust and Python work together."""

import unittest
import sys
import pathlib

# Set sys.path
sys.path.append(str(pathlib.Path()))
 
# import 
myrustlib = __import__("myrustlib")

def py_hello_world(name: str) -> str:
    return f"Hello {name}! This message comes from python."


class TestFunctions(unittest.TestCase):
    """TestFunctions runs the unittests and compares the python and rust implementation"""

    def test_py_hello_world_ok(self):
        """test_py_hello_world_ok checks the greeting string"""
        greeting = py_hello_world("Daniel")
        self.assertEqual(greeting, "Hello Daniel! This message comes from python.")

        greeting = py_hello_world("Ferris Rust")
        self.assertEqual(greeting, "Hello Ferris Rust! This message comes from python.")

    def test_rs_hello_world_ok(self):
        """test_rs_hello_world_ok checks the greeting string from the rust library"""
        greeting = myrustlib.rs_hello_world("Daniel")
        self.assertEqual(greeting, "Hello Daniel! This message comes from Rust.")
    
        greeting = myrustlib.rs_hello_world("Ferris Rust")
        self.assertEqual(greeting, "Hello Ferris Rust! This message comes from Rust.")

if __name__ == '__main__':
    unittest.main(exit=False)