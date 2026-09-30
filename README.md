# Python Tkinter Calculator

A simple, modern, and beginner-friendly desktop calculator application built using Python and Tkinter.

---

## Features

- **Clean Interface:** Modern color-coded buttons and clear display entry.
- **Numbers & Decimals:** Full keypad for digits `0` through `9` and decimal point (`.`).
- **Basic Operators:** Addition (`+`), Subtraction (`−`), Multiplication (`×`), and Division (`÷`).
- **Clear & Backspace:** Clear (`C`) button to reset and Backspace (`⌫`) button to correct entry mistakes.
- **Error Handling:** Gracefully handles division by zero and invalid input without crashing.

---

## Visual Preview & How it Works

### Calculator Layout
```text
+---------------------------------+
|  Simple Calculator          _ X |
+---------------------------------+
|  [                     25.5 × 4 ] | <-- Calculation Display
+---------------------------------+
|  [  C  ]  [  ⌫  ]        [  ÷  ] | <-- Clear, Backspace, Divide
|  [  7  ]  [  8  ]  [  9  ] [  ×  ] | <-- Numbers & Multiply
|  [  4  ]  [  5  ]  [  6  ] [  −  ] | <-- Numbers & Subtract
|  [  1  ]  [  2  ]  [  3  ] [  +  ] | <-- Numbers & Add
|  [  0  ]  [  .  ]  [     =     ] | <-- Number, Decimal, Equals
+---------------------------------+
```

### Example Usage Scenarios

1. **Basic Math:**
   - Click `1` `2` `+` `3` `4` `=` $\rightarrow$ Output: `46`
2. **Decimal Math:**
   - Click `2` `.` `5` `×` `4` `=` $\rightarrow$ Output: `10`
3. **Division by Zero Handling:**
   - Click `5` `÷` `0` `=` $\rightarrow$ Output: `Error: Division by Zero`
4. **Correction:**
   - Click `1` `2` `5` `⌫` $\rightarrow$ Display changes from `125` to `12`.
   - Click `C` $\rightarrow$ Display resets to empty.

---

## How to Run in VS Code (Step-by-Step)

### Prerequisites
- Python 3.x installed on your computer. (Tkinter comes pre-installed with standard Python on Windows and macOS).

### Step 1: Open VS Code
1. Launch **Visual Studio Code**.
2. Open the project folder (`File` > `Open Folder...` and select the repository folder containing `calculator.py`).

### Step 2: Select Python Interpreter
1. Press `Ctrl + Shift + P` (or `Cmd + Shift + P` on macOS) to open the Command Palette.
2. Type `Python: Select Interpreter` and select your installed Python version.

### Step 3: Run the Calculator Application
You can run the application using any of the following methods:

- **Method A (Run Button):**
  Open `calculator.py` in the editor and click the **Play ▶ button** in the top-right corner of VS Code.

- **Method B (VS Code Terminal):**
  Open the built-in terminal (`Terminal` > `New Terminal` or `Ctrl + \``) and run:
  ```bash
  python calculator.py
  ```
  *(On Linux/macOS, you may need `python3 calculator.py`)*

---

## Running Unit Tests

To run the unit tests:
```bash
python3 -m unittest test_calculator.py
```
*(In headless Linux environments, run with `xvfb-run python3 -m unittest test_calculator.py`)*
