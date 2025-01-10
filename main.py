from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton, QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import re


class FunctionPlotter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Function Plotter")
        self.setGeometry(100, 100, 800, 600)
        self.initUI()

    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        # Input fields
        self.input_function1 = QLineEdit(self)
        self.input_function1.setPlaceholderText("Enter first function (e.g., 5*x^3 + 2*x)")
        self.layout.addWidget(self.input_function1)

        self.input_function2 = QLineEdit(self)
        self.input_function2.setPlaceholderText("Enter second function (e.g., x^2 - 3*x)")
        self.layout.addWidget(self.input_function2)

        # Plot button
        self.plot_button = QPushButton("Plot Functions")
        self.plot_button.clicked.connect(self.plot_functions)
        self.layout.addWidget(self.plot_button)

        # Matplotlib canvas
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

    def validate_and_parse(self, function_str):
        # Replace '^' with '**' for Python syntax
        function_str = function_str.replace("^", "**")
        # Validate allowed characters
        if not re.fullmatch(r"[0-9x+\-*/.()^log10sqrt ]+", function_str):
            return None
        return function_str

    def plot_functions(self):
        func1_str = self.validate_and_parse(self.input_function1.text())
        func2_str = self.validate_and_parse(self.input_function2.text())

        if func1_str is None or func2_str is None:
            # Explicitly create a QMessageBox
            error_dialog = QMessageBox(self)
            error_dialog.setWindowTitle("Input Error")
            error_dialog.setText("Invalid function format!")
            error_dialog.setIcon(QMessageBox.Warning)
            error_dialog.show()
            return

        x = np.linspace(-10, 10, 500)
        try:
            y1 = eval(func1_str, {"x": x, "log10": np.log10, "sqrt": np.sqrt})
            y2 = eval(func2_str, {"x": x, "log10": np.log10, "sqrt": np.sqrt})

            # Clear previous plot
            self.figure.clear()
            ax = self.figure.add_subplot(111)

            # Plot the functions
            ax.plot(x, y1, label="f1(x) = " + self.input_function1.text())
            ax.plot(x, y2, label="f2(x) = " + self.input_function2.text())

            # Find intersection points
            diff = np.abs(y1 - y2)
            idx = np.argmin(diff)
            intersection_x = x[idx]
            intersection_y = y1[idx]
            ax.scatter(intersection_x, intersection_y, color="red", label="Intersection")
            ax.annotate(f"({intersection_x:.2f}, {intersection_y:.2f})",
                        (intersection_x, intersection_y), textcoords="offset points", xytext=(-15, 10))

            ax.legend()
            ax.grid()
            self.canvas.draw()

        except Exception as e:
            error_dialog = QMessageBox(self)
            error_dialog.setWindowTitle("Error")
            error_dialog.setText(f"Error plotting functions: {str(e)}")
            error_dialog.setIcon(QMessageBox.Critical)
            error_dialog.show()


if __name__ == "__main__":
    app = QApplication([])
    window = FunctionPlotter()
    window.show()
    app.exec_()
