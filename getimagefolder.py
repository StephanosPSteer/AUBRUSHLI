#import csv
import sqlite3
import configparser
import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QWidget, QVBoxLayout, QGroupBox, QRadioButton, QLabel, QCheckBox, QPushButton, QMessageBox, QButtonGroup


class foldWindow(QMainWindow):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.rows = []
        self.initUI()
        # self.setWindowTitle("CSV Viewer")
        # self.setFixedSize(800, 600)

    def initUI(self):
        central_widget = QWidget()
        vbox = QVBoxLayout()

        # Add a label at the top of the window
        label = QLabel('Please select the shot that you want to create a storyboard for:')
        #label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size: 18pt; font-family: Courier; font-weight: bold;")
        vbox.addWidget(label)


        conn = sqlite3.connect('aubrushli.db')
        # Query the table
        cursor = conn.execute("SELECT distinct s.* from shots s join ShotImages SI on s.Shot_Number = SI.ShotID")
        for i, row in enumerate(cursor):
              row_text = ', '.join(row[:10])

              radio_button = QRadioButton(f"SHOT {i + 1}: {row_text}")

              #radio_button.setStyleSheet("font-size: 18pt; font-family: Courier; font-weight: bold;")

              vbox.addWidget(radio_button)
              #button_group.addButton(radio_button)
              self.rows.append((i + 1, row, radio_button))
        conn.close()
   

       # Create a horizontal layout for the confirm button
        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        confirm_button = QPushButton('Confirm')
        hbox1.addWidget(confirm_button)

        #vbox.addLayout(hbox)
        vbox.addLayout(hbox1)
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

        # Connect the confirm button to the handler function
        confirm_button.clicked.connect(self.confirmSelection)

        # Load the style sheet
        with open("dark_orange3.qss", "r") as f:
            self.setStyleSheet(f.read())


    def handle_radio_button_click(self, radio_button):
        for row in self.rows:
            if row[2] == radio_button:
                #print(f"Selected row: {row}")
                break

    def confirmSelection(self, radio_button):
        selected_rows = []
        for row in self.rows:
            #print(row)
            if row[2].isChecked():
                #print(row)
                selected_rows.append(row[1][0])
        if not selected_rows:
            # Show an error message if no row is selected
            QMessageBox.critical(self, 'Error', 'No row selected. Please select at least one row before confirming.')
        else:
            # Call a second Python script and pass the selected rows as arguments
            subprocess.run(['python', 'imageselector.py'] + selected_rows)
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    config = configparser.ConfigParser()
    config.read('settings.ini')
    shot_list_file = config.get('FileLocations', 'ShotListFile')
    csv_window = foldWindow(shot_list_file)
    csv_window.show()
    sys.exit(app.exec_())
