from PyQt6 import uic 
from PyQt6.QtWidgets import QMainWindow,QMessageBox,QHBoxLayout,QListWIdget
from PyQt6.QtCore import Qt
from widgets.dialog import CreateDialog, UpdateDialog
from setup_db import *
from widgets.anime import AnimeItemWidget

class AnimeCRUD():
    def create(self):
        create_dialog=CreateDialog()
        if create_dialog.exec()== CreateDialog.DialogCode.Accepted:
            data=create_dialog.get_data()
            create_anime(data["tite"],data["release_date"], data["image"], data["rating"], data["link"])
            
    def read(self):
        results=get_all_anime()
        return results
    
    def update(self,id):
        item = get_anime_by_id(id)
        update_dialog= UpdateDialog(item)
        if update_dialog.exec()==UpdateDialog.DialogCode.Accepted:
            data= update_dialog.get_data()
            anime= Anime (data["tite"],data["release_date"], data["image"], data["rating"], data["link"])
            update_anime(id,anime)
            
            
    def delete(self,id):
        question=QMessageBox.question(self,"Delete Anime",
                                      "Are you sure you want to delte this anime?",
                                      QMessageBox.StandarButton.Yes|QMessageBox.StandarButton.No)
        
        if question==  QMessageBox.StandarButton.Yes:
            delete_anime(id)
            QMessageBox.information(self,"Delete Anime", "Anime deleted successfully!")
            

class MainWindow(QMainWindow):
    def __init__ (self):
        super().__init__()
        
        uic.loadUi("main_windows.ui",self)
        self.animeLisWidget=self.findChild(QListWIdget,"animeLisWidget")
        
        self.horizontallayout= QHBoxLayout(self.animeLisWidget)
        self.horizontallayout. setAligment(Qt.AlignmentFlag.AlignLeft)
        
    def display_anime_layout(self, animeList):
        self.animeLisWidget.clear()
        for anime in animeList:
         self.layout=AnimeItemWidget(anime)
         self.horizontallayout.addWidget(self.layout)
        self.animeLisWidget.setLayout(self.horizontallayout)