from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QFileDialog, QComboBox, QTextEdit, \
    QPlainTextEdit,QApplication
from PyQt5.QtCore import Qt, QMimeData
from utils import calculate_hash


class HashApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Hash Calculator')
        self.setFixedSize(630, 400)

        layout = QVBoxLayout()

        self.label = QLabel('Select file to calculate its hash', self)
        layout.addWidget(self.label)

        self.textEdit = QPlainTextEdit(self)
        self.textEdit.setReadOnly(True)  # 禁用输入
        layout.addWidget(self.textEdit)

        self.comboBox = QComboBox(self)
        self.comboBox.addItems(["MD5", "SHA-1", "SHA-256"])
        layout.addWidget(self.comboBox)

        self.button = QPushButton('Open File', self)
        self.button.clicked.connect(self.openFile)
        layout.addWidget(self.button)

        self.clearButton = QPushButton('Clear', self)
        self.clearButton.clicked.connect(self.clearDisplay)
        layout.addWidget(self.clearButton)

        self.quitButton = QPushButton('Quit', self)
        self.quitButton.clicked.connect(self.quitApp)
        layout.addWidget(self.quitButton)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.setAcceptDrops(True)  # 启用拖放

    def openFile(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open File')
        if file_path:
            self.calculateAndDisplayHash(file_path)

    def calculateAndDisplayHash(self, file_path):
        hash_type = self.comboBox.currentText().replace("-", "").lower()
        hash_value = calculate_hash(file_path, hash_type)
        self.textEdit.appendPlainText(f"{hash_type.upper()} hash of {file_path}:\n{hash_value}")
        self.textEdit.appendPlainText("-" * 65 )  # 添加分割线

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def quitApp(self):
        QApplication.quit()


    def dropEvent(self, event):
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            self.calculateAndDisplayHash(file_path)

    def clearDisplay(self):
        self.textEdit.clear()
