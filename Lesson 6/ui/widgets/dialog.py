from PyQt6 import uic 
from PyQt6.QtWidgets import QDialog, QFileDialog, QLabel, QLineEdit, QPushButton, QDateEdit
from PyQt6.QtCore import Qt, QDate, QDir
from models.anime import Anime

class Dialog(QDialog):
    def __init__(self):
        super().__int__()
        uic.loadUi("dialog.ui",self)
        
        self.titleInput = self.findChild(QLineEdit, "titleInput")
        self.releasedateInput=self.findChild(QDateEdit,"releasedateInput")
        self.image_label=self.findChild(QLabel, "image_label")
        self.ratingInput=self.findChild(QLineEdit,"ratingInput")
        self.urlInput=self.findChild(QLineEdit,"urlInput")
        
        self.uploadImgButton=self.findChild(QPushButton,"uploadImgButton")
        
        self.releasedateInput.setDisplayFormat("dd/MM/yyyy")
        self.uploadImgButton.clicked.connect(self.browse_files)
     
        
    def browse_files(self):
        file_dialog=QFileDialog()
        file_dialog.setFileMode(QFileDialog.FileMode.ExisitngFile)
        file_dialog.setNameFilter("Images(*.png*.jpg*.jpeg)")
        if file_dialog.exec()==QDialog.DialogCode.Accepted:
            file_path=file_dialog.selectedFiles()[0]
            self.image_path.setText(file_path)
            self.image_path.setReadOnly(True)
            
    
    def get_data(self):
        return{
            "title": self.titleInput.text(),
            "realse_date":self.releasedateInput.date().toString(Qt.DateFormat.ISODate),
            "image":self.image_label. text(),
            "rating": self.ratingInput.text(),
            "link": self.urlInput.text()
        }
        
        
class CreateDialog(Dialog):
    def __int__(self):
        super().__int__()
        self.setWindowTitle("Create Anime")
        
class UpdateDialog(Dialog):
    def __init__(self, item:Anime):
        super().__init__()
        self.setWindowTile("Update Anime")
        
        self.titleInput.setText(item.tile)
        date=QDate.froString(item.release_date, Qt.DateFormat.ISODate)
        self.releasedateInput.setDate(date)
        self.image_label.setText(item.image)
        self.ratingInput.setText(item.rating)
        self.urlInput.setText(item.link)
            