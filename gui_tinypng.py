import sys
import os
import tinify
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PySide6.QtCore import Qt
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()
TINIFY_API_KEY = os.getenv("TINIFY_API_KEY")

if not TINIFY_API_KEY:
    raise ValueError("A chave da API não foi encontrada. Verifique o arquivo .env.")

# Define a chave da API no Tinify
tinify.key = TINIFY_API_KEY


class DropLabel(QLabel):
    def __init__(self):
        super().__init__("Arraste imagens aqui para comprimir")
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet(
            "QLabel { border: 2px dashed #aaa; padding: 40px; font-size: 18px; }"
        )
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            filepath = url.toLocalFile()
            if filepath.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
                self.compress_image(filepath)

    def compress_image(self, path):
        try:
            output_path = path.replace(".", "_web.")
            source = tinify.from_file(path)
            source.to_file(output_path)
            self.setText(f"✔ Imagem comprimida:\n{output_path}")
        except Exception as e:
            self.setText(f"Erro ao comprimir: {e}")


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Compressor TinyPNG")
        layout = QVBoxLayout()
        layout.addWidget(DropLabel())
        self.setLayout(layout)
        self.resize(400, 300)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
