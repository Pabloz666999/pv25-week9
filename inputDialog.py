import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QInputDialog, QLabel
from PyQt5.QtCore import Qt

class InputDialogExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Input Dialog")
        self.setGeometry(100, 100, 400, 200)

        self.setStyleSheet("""
            QWidget {
                background-color: #2b2b2b;
                color: #ffffff;
            }
            QLabel {
                color: #ffffff;
            }
            QPushButton {
                color: #ffffff;
                background-color: #3c3f41;
                border: 1px solid #5c5c5c;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #4c5052;
            }
        """)

        layout = QVBoxLayout()

        nama_layout = QHBoxLayout()
        self.nama_label = QLabel("Nama:")
        self.nama_button = QPushButton("Pilih Nama")
        self.nama_button.clicked.connect(self.show_nama_dialog)
        nama_layout.addWidget(self.nama_label)
        nama_layout.addWidget(self.nama_button)
        layout.addLayout(nama_layout)

        jurusan_layout = QHBoxLayout()
        self.jurusan_label = QLabel("Jurusan:")
        self.jurusan_button = QPushButton("Pilih Jurusan")
        self.jurusan_button.clicked.connect(self.show_jurusan_dialog)
        jurusan_layout.addWidget(self.jurusan_label)
        jurusan_layout.addWidget(self.jurusan_button)
        layout.addLayout(jurusan_layout)

        tahun_lulus_layout = QHBoxLayout()
        self.tahun_lulus_label = QLabel("Tahun Lulus:")
        self.tahun_lulus_button = QPushButton("Masukkan Tahun Lulus")
        self.tahun_lulus_button.clicked.connect(self.show_tahun_lulus_dialog)
        tahun_lulus_layout.addWidget(self.tahun_lulus_label)
        tahun_lulus_layout.addWidget(self.tahun_lulus_button)
        layout.addLayout(tahun_lulus_layout)

        footer = QLabel("F1D02310144 - M. Bayu Aji")
        footer.setAlignment(Qt.AlignCenter)
        layout.addWidget(footer)

        self.setLayout(layout)

    def show_nama_dialog(self):
        text, ok = QInputDialog.getText(self, "Input Nama", "Masukkan nama kamu:")
        if ok and text:
            self.nama_button.setText(f"{text}") 

    def show_jurusan_dialog(self):
        items = ["Informatika", "Sistem Informasi", "Teknik Elektro", "Arsitektur"]
        item, ok = QInputDialog.getItem(self, "Pilih Jurusan", "Pilih jurusan kamu:", items, 0, False)
        if ok and item:
            self.jurusan_button.setText(f"{item}")  

    def show_tahun_lulus_dialog(self):
        year, ok = QInputDialog.getInt(self, "Masukkan Tahun Lulus", "Masukkan tahun lulus kamu:", 2023, 2000, 2100, 1)
        if ok:
            self.tahun_lulus_button.setText(f"{year}")  

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = InputDialogExample()
    window.show()
    sys.exit(app.exec_())
