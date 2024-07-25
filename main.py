import sys

from PySide6.QtWidgets import QApplication

from backend_main import ResultCalculator

if __name__ == '__main__':
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()
    window = ResultCalculator()
    window.show()

    sys.exit(app.exec())
