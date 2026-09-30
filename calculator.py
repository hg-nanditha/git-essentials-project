"""
Simple Beginner-Friendly Python Calculator using Tkinter
======================================================
This program creates a simple desktop calculator application.
It provides basic arithmetic operations (+, −, ×, ÷), clear, backspace,
decimal point input, and safely handles division by zero.
"""

import tkinter as tk


def evaluate_expression(expression: str) -> str:
    """
    Evaluates a math expression string safely and returns the result as a string.

    Replaces user-friendly display symbols ('×', '÷', '−') with Python operators
    ('*', '/', '-'). If division by zero occurs, returns an error message.
    """
    if not expression:
        return ""

    # Replace display symbols with Python's arithmetic operators
    cleaned_expression = (
        expression.replace("×", "*")
                  .replace("÷", "/")
                  .replace("−", "-")
    )

    try:
        # Evaluate the mathematical expression
        # Restricted builtins dictionary for safety
        result = eval(cleaned_expression, {"__builtins__": None}, {})

        # If the result is a float that is a whole number (e.g., 5.0), format as int (5)
        if isinstance(result, float) and result.is_integer():
            result = int(result)

        return str(result)

    except ZeroDivisionError:
        return "Error: Division by Zero"
    except Exception:
        return "Error"


class CalculatorApp:
    """
    Main Calculator GUI application class using Tkinter.
    """

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("350x450")
        self.root.resizable(False, False)
        self.root.configure(bg="#F3F4F6")  # Light gray background

        # Variable to keep track of the display text
        self.display_var = tk.StringVar()
        self.display_var.set("")

        # Flag to clear display when a new digit is pressed after showing a result or error
        self.should_reset_display = False

        # Create GUI elements
        self._create_display()
        self._create_buttons()

    def _create_display(self):
        """Creates the display screen at the top of the calculator."""
        display_frame = tk.Frame(self.root, bg="#F3F4F6")
        display_frame.pack(fill="x", padx=15, pady=(15, 10))

        # Entry field for showing the current calculation and results
        self.display_entry = tk.Entry(
            display_frame,
            textvariable=self.display_var,
            font=("Arial", 22, "bold"),
            bg="#FFFFFF",
            fg="#111827",
            bd=2,
            relief="groove",
            justify="right"
        )
        self.display_entry.pack(fill="x", ipady=10)

    def _create_buttons(self):
        """Creates the grid layout of buttons."""
        buttons_frame = tk.Frame(self.root, bg="#F3F4F6")
        buttons_frame.pack(fill="both", expand=True, padx=15, pady=(0, 15))

        # Button layout definition: (Text, Row, Column, Color Scheme, Action Handler)
        # Grid layout consists of 5 rows and 4 columns
        button_layout = [
            ("C", 0, 0, "clear"), ("⌫", 0, 1, "action"), ("÷", 0, 3, "operator"),
            ("7", 1, 0, "number"), ("8", 1, 1, "number"), ("9", 1, 2, "number"), ("×", 1, 3, "operator"),
            ("4", 2, 0, "number"), ("5", 2, 1, "number"), ("6", 2, 2, "number"), ("−", 2, 3, "operator"),
            ("1", 3, 0, "number"), ("2", 3, 1, "number"), ("3", 3, 2, "number"), ("+", 3, 3, "operator"),
            ("0", 4, 0, "number"), (".", 4, 1, "number"), ("=", 4, 2, "equal")
        ]

        # Configure grid row and column weights so buttons size evenly
        for i in range(5):
            buttons_frame.rowconfigure(i, weight=1)
        for j in range(4):
            buttons_frame.columnconfigure(j, weight=1)

        # Create each button based on the layout definition
        for item in button_layout:
            text = item[0]
            row = item[1]
            col = item[2]
            style_type = item[3]

            # Assign styling colors based on button type
            bg_color, fg_color, active_bg = self._get_button_style(style_type)

            # Determine button span (Equal '=' spans 2 columns at the bottom)
            colspan = 2 if text == "=" else 1

            btn = tk.Button(
                buttons_frame,
                text=text,
                font=("Arial", 16, "bold"),
                bg=bg_color,
                fg=fg_color,
                activebackground=active_bg,
                activeforeground=fg_color,
                bd=1,
                relief="raised",
                command=lambda t=text: self.on_button_click(t)
            )
            btn.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=3, pady=3)

    def _get_button_style(self, style_type: str):
        """Returns background, foreground, and active background colors for a button style."""
        if style_type == "number":
            return "#FFFFFF", "#1F2937", "#E5E7EB"       # White background, dark text
        elif style_type == "operator":
            return "#F59E0B", "#FFFFFF", "#D97706"       # Amber background, white text
        elif style_type == "clear":
            return "#EF4444", "#FFFFFF", "#DC2626"       # Red background, white text
        elif style_type == "action":
            return "#9CA3AF", "#FFFFFF", "#6B7280"       # Gray background, white text
        elif style_type == "equal":
            return "#10B981", "#FFFFFF", "#059669"       # Emerald green background, white text
        return "#E5E7EB", "#000000", "#D1D5DB"

    def on_button_click(self, char: str):
        """
        Handles button clicks based on the button text.
        """
        current_text = self.display_var.get()

        # If previous result was an error or calculation finished, reset for new digit entry
        if self.should_reset_display:
            if char in "0123456789.":
                current_text = ""
            self.should_reset_display = False

        # Clear button logic
        if char == "C":
            self.display_var.set("")

        # Backspace button logic
        elif char == "⌫":
            if current_text.startswith("Error"):
                self.display_var.set("")
            else:
                self.display_var.set(current_text[:-1])

        # Equals button logic
        elif char == "=":
            if current_text and not current_text.startswith("Error"):
                result = evaluate_expression(current_text)
                self.display_var.set(result)
                self.should_reset_display = True

        # Number or decimal point input
        elif char in "0123456789.":
            # If display shows an error, clear it before entering new digit
            if current_text.startswith("Error"):
                current_text = ""
            self.display_var.set(current_text + char)

        # Operator input (+, −, ×, ÷)
        elif char in ["+", "−", "×", "÷"]:
            if current_text.startswith("Error"):
                current_text = ""

            # Avoid duplicate trailing operators
            if current_text and current_text[-1] in ["+", "−", "×", "÷"]:
                current_text = current_text[:-1]

            if current_text or char == "−":  # Allow negative sign at start
                self.display_var.set(current_text + char)


def main():
    """Main entry point for starting the Tkinter application."""
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
