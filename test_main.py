import pytest
from PySide2.QtWidgets import QMessageBox
from PySide2.QtCore import Qt  # Import Qt for mouse buttons
from main import FunctionPlotter  # Assuming the main code is in main.py


@pytest.fixture
def app(qtbot):
    window = FunctionPlotter()
    qtbot.addWidget(window)  # Add the window to qtbot for lifecycle management
    return window


def test_valid_input(app, qtbot):
    app.input_function1.setText("x^2")
    app.input_function2.setText("2*x + 1")
    qtbot.mouseClick(app.plot_button, Qt.LeftButton)  # Corrected to use Qt.LeftButton

    assert app.input_function1.text() == "x^2"
    assert app.input_function2.text() == "2*x + 1"


def test_invalid_input(app, qtbot):
    app.input_function1.setText("x^^2")  # Invalid input
    app.input_function2.setText("2*x + 1")
    qtbot.mouseClick(app.plot_button, Qt.LeftButton)  # Corrected to use Qt.LeftButton

    # Check for error dialog (assuming you use QMessageBox)
    error_dialog = app.findChild(QMessageBox)
    assert error_dialog is not None
    assert error_dialog.windowTitle() == "Input Error"
    assert "Invalid function format!" in error_dialog.text()
