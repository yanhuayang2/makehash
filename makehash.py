import sys
from PyQt5.QtWidgets import QApplication
from gui import HashApp

def main():
    app = QApplication(sys.argv)
    ex = HashApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
