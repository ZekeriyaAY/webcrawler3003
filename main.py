import sys
import colorama
from PySide6.QtWidgets import QApplication
from app.main_window import MainWindow

if __name__ == "__main__":
    try:
        colorama.init()
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec())
    except KeyboardInterrupt:
        print('bye!!')
