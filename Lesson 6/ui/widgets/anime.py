from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QLable
from PyQt6.QtGui import QPixmap
from model.anime import Anime

class AnimeItemWidget(QWidget):
    def __init__(self, anime:Anime):
        super().__init__()
        uic.loadUi("./ui/anime_column.ui",self)
        
        self. animeInfo=self.findChild(QLable,"animeInfo")
        self.animeTitle=self.finChild(QLable,"animeTitle")
        self.animeView=self.finChild(QLable,"animeView")
        
        self.animeTitle.setText(anime.title)
        self. animeInfo. setText("Release Date:"+ anime.release_date+"Rating:"+anime.rating)
        self.animeView.setPixmap(QPixmap(anime.image))