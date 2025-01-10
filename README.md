# MathematicalFunctionSolverAndVisualizer

Function Plotter

A simple PySide2-based GUI application to plot two mathematical functions and display their intersection point.


Features
Input two mathematical functions.
Automatically plots the functions and their intersection point.
Validates input to ensure the function format is correct.
Displays error messages using QMessageBox when the input format is invalid.


Requirements
Python 3.x
PySide2
Matplotlib
NumPy
pytest (for testing)

You can install the required dependencies using pip:
pip install PySide2 matplotlib numpy pytest

How to Run
Clone the repository or download the files (main.py and test_main.py).

Run the main.py file:
python main.py

This will open the Function Plotter application window, where you can enter mathematical functions like x^2, 5*x^3 + 2*x, etc. Then, click "Plot Functions" to generate the graph and find the intersection.


File Descriptions
main.py: Contains the GUI application code that allows users to input functions, plot them, and identify the intersection.
test_main.py: Contains test cases using pytest and qtbot for ensuring the application works correctly.


Testing
To run the tests: pytest test_main.py

The tests validate the following:
Correct input is properly parsed and plotted.
Invalid input triggers an error message via a QMessageBox.


Error Handling
The application includes error handling to catch:
Invalid function format (e.g., missing characters or unrecognized symbols).
Plotting errors.
If an invalid input is entered, an error dialog will be shown with the message: "Invalid function format!".

Usage Example
Enter the first function: x^2
Enter the second function: 2*x + 1
Click "Plot Functions".
The plot will display the functions, and the intersection point will be marked in red. The coordinates of the intersection will be displayed next to it.
