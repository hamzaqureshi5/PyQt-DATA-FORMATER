import sys
import re
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QTextEdit, QPushButton, QVBoxLayout, QWidget, QFileDialog
from PyQt6.QtGui import QIcon,QIntValidator
import datetime
import time

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SPACE FORMATER")
        self.setGeometry(100, 100, 300, 200)
        self.setFixedHeight(400)
        self.setFixedWidth(500)
        self.setWindowIcon(QIcon("ico.ico"))

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.label1 = QLabel("FILE PATH:", self)
        self.layout.addWidget(self.label1)

        self.edit1 = QLineEdit(self)
        self.edit1.setReadOnly(True)
        self.layout.addWidget(self.edit1)

        self.browse_button = QPushButton("BROWSE", self)
        self.browse_button.clicked.connect(self.browseFile)
        self.layout.addWidget(self.browse_button)

        self.label2 = QLabel("SPACE AFTER:", self)
        self.layout.addWidget(self.label2)

        self.edit2 = QLineEdit(self)
        int_validator = QIntValidator()
        self.edit2.setValidator(int_validator)
        self.edit2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.edit2)

        self.submit_button = QPushButton("SUBMIT", self)
        self.submit_button.clicked.connect(self.generateResults)
        self.layout.addWidget(self.submit_button)

        self.text_box = QTextEdit(self)
#        self.text_box.setFontPointSize(8)
        self.layout.addWidget(self.text_box)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)
        self.developer_label = QLabel("Developed by : Hamza Qureshi", self)
        self.developer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Align center
        self.layout.addWidget(self.developer_label)
        self.version_label = QLabel("Version 1.0.0", self)
        self.version_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Align center
        self.layout.addWidget(self.version_label)

    def browseFile(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File", "", "All Files (*)")
        if file_path:
            self.edit1.setText(file_path)
            self.inputfile=file_path

    def generateResults(self):
        file_path = self.edit1.text()
        input_variable = self.edit2.text()

        if file_path and input_variable:
            # Perform processing or generate results using the file path and input variable
            
            result = f"File: {file_path}, \nExpect space after every {input_variable} character/characters\nOutput file generated named as \"Output.txt\""
            self.text_box.setPlainText(result)
            self.submit(file_path,int(input_variable))
        else:
            self.text_box.setPlainText("Please enter a valid file path and input variable.")



    def process_and_generate(self,input_file_path, output_file_path, spaces_after_x):
        try:
            with open(input_file_path, "r") as input_file:
                content = input_file.read()

            content_without_spaces = re.sub(r"\s+", "", content)

            processed_content = " ".join(content_without_spaces[i:i+spaces_after_x] for i in range(0, len(content_without_spaces), spaces_after_x))

            with open(output_file_path, "w") as output_file:
                output_file.write(processed_content)

            return True  # Successfully processed and generated the output file

        except Exception as e:
            self.text_box.append(str(e))
#            print("Error:", str(e))
            return False  # Failed to process and generate the output file

    def submit(self,input_path,spaces_after):
        # Usage example:
        # input_path = self.inputfile
        
        output_path = "output.txt"
        # spaces_after = self.spacer

        if self.process_and_generate(input_path, output_path, spaces_after):
#            print("Processing and generation completed successfully.")
            self.text_box.append(str("Processing and generation completed successfully."))

        else:
#            print("Processing and generation failed.")
            self.text_box.append(str("Processing and generation failed."))
            
    def get_time(self):
        p_time = str(time.strftime("%H_%M_%S", time.localtime()))
        p_date = str(datetime.date.today().strftime("%Y_%m_%d"))
        return p_date+"_"+p_time

def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
