"""
Unit tests for the Tkinter Calculator application (calculator.py).
"""

import os
import unittest
# Run Tkinter in headless environment if needed
if os.environ.get("DISPLAY") is None and os.name != "nt":
    pass  # xvfb-run should be used when running unittest on headless Linux

import tkinter as tk
from calculator import CalculatorApp, evaluate_expression


class TestCalculatorLogic(unittest.TestCase):
    """Test pure expression evaluation logic."""

    def test_addition(self):
        self.assertEqual(evaluate_expression("12+34"), "46")

    def test_subtraction(self):
        self.assertEqual(evaluate_expression("50−18"), "32")

    def test_multiplication(self):
        self.assertEqual(evaluate_expression("6×7"), "42")

    def test_division(self):
        self.assertEqual(evaluate_expression("20÷4"), "5")

    def test_decimal_operations(self):
        self.assertEqual(evaluate_expression("3.5+2.5"), "6")
        self.assertEqual(evaluate_expression("10.5÷2"), "5.25")

    def test_division_by_zero(self):
        self.assertEqual(evaluate_expression("10÷0"), "Error: Division by Zero")

    def test_invalid_expression(self):
        self.assertEqual(evaluate_expression("5+"), "Error")
        self.assertEqual(evaluate_expression("++"), "Error")

    def test_empty_expression(self):
        self.assertEqual(evaluate_expression(""), "")


class TestCalculatorGUI(unittest.TestCase):
    """Test Tkinter GUI button interactions."""

    def setUp(self):
        self.root = tk.Tk()
        self.app = CalculatorApp(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_number_input(self):
        self.app.on_button_click("1")
        self.app.on_button_click("2")
        self.app.on_button_click("3")
        self.assertEqual(self.app.display_var.get(), "123")

    def test_operator_input(self):
        self.app.on_button_click("5")
        self.app.on_button_click("+")
        self.app.on_button_click("5")
        self.assertEqual(self.app.display_var.get(), "5+5")

    def test_equals_button(self):
        self.app.on_button_click("8")
        self.app.on_button_click("×")
        self.app.on_button_click("9")
        self.app.on_button_click("=")
        self.assertEqual(self.app.display_var.get(), "72")

    def test_clear_button(self):
        self.app.on_button_click("9")
        self.app.on_button_click("9")
        self.app.on_button_click("C")
        self.assertEqual(self.app.display_var.get(), "")

    def test_backspace_button(self):
        self.app.on_button_click("1")
        self.app.on_button_click("2")
        self.app.on_button_click("3")
        self.app.on_button_click("⌫")
        self.assertEqual(self.app.display_var.get(), "12")

    def test_division_by_zero_gui(self):
        self.app.on_button_click("7")
        self.app.on_button_click("÷")
        self.app.on_button_click("0")
        self.app.on_button_click("=")
        self.assertEqual(self.app.display_var.get(), "Error: Division by Zero")

        # Pressing clear after error clears screen
        self.app.on_button_click("C")
        self.assertEqual(self.app.display_var.get(), "")


if __name__ == "__main__":
    unittest.main()
