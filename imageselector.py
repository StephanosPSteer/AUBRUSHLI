import os
import subprocess
import sys
import argparse
#import configparser
import sqlite3
import pandas as pd
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog
 


class ImageViewer(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.images = []#images
        self.selected_image_path = None
        self.image_labels = []
        self.text_labels = []
        

        parser = argparse.ArgumentParser(description='Process selected rows')
        parser.add_argument('rows', nargs='+', help='Selected rows')

        args = parser.parse_args()
        selected_rows = args.rows

                # Connect to the database
        conn = sqlite3.connect('aubrushli.db')

        # Define the query to retrieve data
        query = "SELECT * FROM ShotImages WHERE ShotID =" + selected_rows[0]

        # Retrieve the data into a Pandas dataframe
        df = pd.read_sql_query(query, conn)
        query1 = "SELECT * FROM shots WHERE Shot_Number=" + selected_rows[0]

        shotsdf = pd.read_sql_query(query1, conn)
        print(query1)
        
        shotsdf = shotsdf.iloc[:,:10]
        # Select a single row from the DataFrame (e.g., the second row)
        row = shotsdf.iloc[0]

# Create a PyQt5 QLabel widget
        shotlabel = QtWidgets.QLabel()

# Create a formatted string that includes the header titles and row data,
# split into two lines using the newline character '\n'
        text = " | ".join([f"{col}: {row[col]}" for col in shotsdf.columns[:4]]) + "\n"
        text += " | ".join([f"{col}: {row[col]}" for col in shotsdf.columns[4:9]]) + "\n"
        text += " | ".join([f"{col}: {row[col]}" for col in shotsdf.columns[9:]])
        


        shotlabel.setText(text)



        conn.close()
    # Find the index of the last occurrence of '/'
        last_slash_index = df.iloc[0]["imagepath"].rfind('/')

    # Truncate the string at that index (exclusive)
        truncated_path = df.iloc[0]["imagepath"][:last_slash_index]
    
        folder_path  = truncated_path#selected_rows[0]
        #print(truncated_path)


 
        for file_name in os.listdir(folder_path):
            if file_name.endswith(('.jpg', '.jpeg', '.png', '.bmp')):
                image_path = os.path.join(folder_path + '/', file_name)

                self.images.append((image_path))


  
        
        # Create a layout to hold the image labels
        layout = QtWidgets.QGridLayout()
        row = 0
        mainlab = "<b>Select an image and then click the confirm button to add it to the storyboard. If you select an image with a seed you will be able to choose just that seed for future image generations</b>"
        # Create a label to display the instruction text
        instruction_label = QtWidgets.QLabel(mainlab)
        instruction_label.setAlignment(Qt.AlignCenter)
        #instruction_label.setStyleSheet("font-size: 50px")
        layout.addWidget(instruction_label, row, 0, 1, 3, alignment=Qt.AlignLeft)
        row += 2
        # Show the QLabel widget
        layout.addWidget(shotlabel, row, 0, 2, 3, alignment=Qt.AlignLeft)
        row += 3



        


        # Create a button to confirm the selected image
        confirm_button = QtWidgets.QPushButton("CONFIRM")
        confirm_button.setCursor(Qt.PointingHandCursor)

        confirm_button.clicked.connect(self.get_selected_image_path)
        confirm_button.clicked.connect(self.confirm_handler)
        layout.addWidget(confirm_button, row, 0, 1, 2, alignment=Qt.AlignLeft)
        row += 1



        
            
        col = 0
        for image in self.images:
        # Create a vertical layout for the cell
            cell_layout = QtWidgets.QVBoxLayout()

        # Create a label for each image
            image_label = QtWidgets.QLabel()
            pixmap = QtGui.QPixmap(image).scaled(512, 512, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            image_label.setPixmap(pixmap)
            image_label.setAlignment(Qt.AlignCenter)

        # Set the label as clickable
            image_label.setCursor(Qt.PointingHandCursor)
            image_label.mousePressEvent = self.get_image_click_handler(image_label, image)

        # Add the image label to the cell layout
            cell_layout.addWidget(image_label)
        
            selected_values = df.loc[df['imagepath'] == image, str('seed')].fillna("no seed sorry")
            
            finalval =""
            if not selected_values.empty:
                finalval = str(selected_values.iloc[0])
            else:
                finalval = "no seed sorry"

            text_label = QtWidgets.QLabel(finalval)
            text_label.setAlignment(Qt.AlignCenter)

        # Add the text label to the cell layout
            cell_layout.addWidget(text_label)

        # Set the cell layout for the current grid cell
            layout.addLayout(cell_layout, row, col)
            self.image_labels.append(image_label)
            self.text_labels.append(text_label)

        # Increment row and column counters
            col += 1
            if col == 3:
                col = 0
                row += 1

            

        # Create a scroll area to hold the layout
        scroll_area = QtWidgets.QScrollArea()
        scroll_area.setWidgetResizable(True)

        # Create a widget to hold the layout
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        scroll_area.setWidget(widget)

        # Set the layout for the widget
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addWidget(scroll_area)
        self.setLayout(main_layout)

        # Load the style sheet
        with open("dark_orange2.qss", "r") as f:
            self.setStyleSheet(f.read())


  

    def confirm_handler(self):
        if self.selected_image_path is not None:
            # Create a confirmation dialog
            msg_box = QtWidgets.QMessageBox()
            msg_box.setWindowTitle("Confirmation")
            msg_box.setText(f"Are you sure you want to select the image:\n\n{self.selected_image_path}")
            msg_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            msg_box.setDefaultButton(QtWidgets.QMessageBox.No)
            msg_box.setIcon(QtWidgets.QMessageBox.Question)
            
            # Show the dialog and wait for user response
            response = msg_box.exec()
            
            # If user clicked "Yes", send the selected image path
            if response == QtWidgets.QMessageBox.Yes:
                print(f"Selected image path: {self.selected_image_path}")
                subprocess.run(['python', 'createstoryboard.py' , str(self.selected_image_path)] )
                self.close()
        else:
            # If no image is selected, show an error message
            QtWidgets.QMessageBox.critical(self, "Error", "No image selected.", QtWidgets.QMessageBox.Ok)


    def get_selected_image_path(self):
        for label in self.image_labels:
            if "rgba(0, 255, 0, 0.5)" in label.styleSheet():
                pixmap = label.pixmap()
                self.selected_image_path = self.images[self.image_labels.index(label)]
                break
        if self.selected_image_path is not None:
            print(f"Selected image: {self.selected_image_path}")
        else:
            print("No image selected.")

        # Connect the mouseover event to the highlight_image method
        for label in self.image_labels:
            label.enterEvent = self.get_image_mouseover_handler(label)
            label.leaveEvent = self.get_image_mouseout_handler(label)

    def get_image_click_handler(self, label, image):
        def handler(event):
            print(f"Image {image} clicked!")
            # Remove the border from all labels
            for l in self.image_labels:
               l.setStyleSheet("border: none")
            # Set the border color and style of the selected label to green with 50% opacity on click
            label.setStyleSheet("border: 4px solid rgba(0, 255, 0, 0.5)")
        return handler

    def get_image_mouseover_handler(self, label):
        def handler(event):
            # Set the background color of the label to yellow on mouseover
            if not "rgba(0, 255, 0, 0.5)" in label.styleSheet():
                label.setStyleSheet('border: 2px solid black;')
        return handler

    def get_image_mouseout_handler(self, label):
        def handler(event):
            # Reset the background color of the label on mouseout
            #label.setStyleSheet("")
            # Reset the border color and style of the label if not clicked
            if not "rgba(0, 255, 0, 0.5)" in label.styleSheet():
                label.setStyleSheet("border: none")
        return handler


if __name__ == '__main__':
# Create the application
    app = QtWidgets.QApplication(sys.argv)
# Create the image viewer widget
    image_viewer = ImageViewer()
    image_viewer.showMaximized()
# Run the application
    sys.exit(app.exec_())
