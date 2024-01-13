import sys
from PyQt6.QtWidgets import QApplication, QWidget, QStackedWidget, QVBoxLayout, QTableWidgetItem,QMessageBox
from PyQt6 import QtWidgets
from arabaekle import arabaekle
from arabaislemleri import arabaislemleri
from arabasil import arabasil
from ciraksil import ciraksil
from kayitol import kayitol
from musteri import musteri
from sifremiunuttum import sifremiunuttum
from yonetici1 import yonetici1
from yoneticigorecek import yoneticigorecek
from yoneticiMenu import yoneticiMenu
from pymongo import MongoClient
import hashlib
import secrets
import resources 


class anaSayfa(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["ayCarTaks"]
        self.users_collection = self.db["kullaniciBilgileri"]
        self.car_collection = self.db["aracbilgi"]


        self.vlayout = QVBoxLayout(self)
        self.vlayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self)
        self.stackedWidget.setContentsMargins(0, 0, 0, 0)

        self.arabaekleWidget = QWidget()
        self.arabaislemleriWidget = QWidget()
        self.arabasilWidget = QWidget()
        self.ciraksilWidget = QWidget()
        self.kayitolWidget = QWidget()
        self.musteriWidget = QWidget()
        self.musterigormesiWidget = QWidget()
        self.sifremiunuttumWidget = QWidget()
        self.yonetici11Widget = QWidget()
        self.yoneticigorecekWidget = QWidget()


        self.stackedWidget.addWidget(self.arabaekleWidget) #{0}
        self.stackedWidget.addWidget(self.arabaislemleriWidget) #1
        self.stackedWidget.addWidget(self.arabasilWidget) #2
        self.stackedWidget.addWidget(self.ciraksilWidget) #3
        self.stackedWidget.addWidget(self.kayitolWidget) #4
        self.stackedWidget.addWidget(self.musteriWidget) #5
        self.stackedWidget.addWidget(self.musterigormesiWidget) #6
        self.stackedWidget.addWidget(self.sifremiunuttumWidget) #7
        self.stackedWidget.addWidget(self.yonetici11Widget) #8
        self.stackedWidget.addWidget(self.yoneticigorecekWidget) #9

        self.vlayout.addWidget(self.stackedWidget)
        self.stackedWidget.setCurrentIndex(5)

        self.loggedUser = None
        self.loggedUsername = None

        self.yonetici1Sayfasi()
        self.kayitSayfasi()
        self.musteriSayfasi()
        self.sifremiUnuttumSayfa()
        self.yoneticiGorecekSayfa()

        self.registerSpawned = False
        self.toDoPageUserSpawned = False
        self.toDoPageAdminSpawned = False

    def yonetici1Sayfasi(self):
        self.yonetici1 = yonetici1()
        self.yonetici1.setupUi(self.yonetici11Widget)
        self.girisbutonu= self.yonetici1.girisyap
        self.girisbutonu.clicked.connect(self.giris)
        self.sifremiunuttumButon=self.yonetici1.sifremiunuttum
        self.sifremiunuttumButon.clicked.connect(self.showsifremiunuttum)
        
    def yoneticiGorecekSayfa(self):
        self.yoneticigorecek = yoneticigorecek()
        self.yoneticigorecek.setupUi(self.yoneticigorecekWidget)
        self.kaydetButonu= self.yoneticigorecek.kaydet
        self.plakagirin = self.yoneticigorecek.plakagirin
        self.siragir = self.yoneticigorecek.siragir
        self.tutar = self.yoneticigorecek.tutar
        self.yapilanislemler = self.yoneticigorecek.yapilanislemler
        self.kaydetButonu.clicked.connect(self.arackaydet)

    def kayitSayfasi(self):
        self.kayitol = kayitol()
        self.kayitol.setupUi(self.kayitolWidget)
        self.kayitButonu= self.kayitol.kaydol_2
    
    def sifremiUnuttumSayfa(self):
        self.sifremiunuttum = sifremiunuttum()
        self.sifremiunuttum.setupUi(self.sifremiunuttumWidget)
        self.girisKodu=self.sifremiunuttum.giriskodu
        
    def musteriSayfasi(self):
        self.musteri = musteri()
        self.musteri.setupUi(self.musteriWidget)
        self.yoneticiGirisButon= self.musteri.yoneticiGirisButon
        self.plaka2 = self.musteri.plaka2
        self.plakagörme = self.musteri.plakagörme
        self.sirasi = self.musteri.sirasi
        self.yapilanislemler2 = self.musteri.yapilanislemler
        self.tutar2 = self.musteri.tutar
        self.yoneticiGirisButon.clicked.connect(self.yoneticiGiris)
        self.sorgulaButon= self.musteri.sorgula
        self.sorgulaButon.clicked.connect(self.musterigormesi)
        
        
    def showsifremiunuttum(self):
        self.stackedWidget.setCurrentIndex(7)       

        
    def arackaydet(self):
        plaka= self.plakagirin.text().strip()
        sira= self.siragir.text().strip()
        yapilanislemler= self.yapilanislemler2.text().strip()
        tutar= self.tutar2.text().strip()

        arac_data ={
            "plaka":plaka,
            "sira":sira,
            "yapilanislemler":yapilanislemler,
            "tutar": tutar
        }
           
        self.car_collection.insert_one(arac_data)
        QMessageBox.information(self,"Basarili","Arac Basariyla Kaydedildi")
            
    def musterigormesi(self):
        search_value = self.plaka2.text()
        result = self.car_collection.find_one({"plaka": search_value})

        if result:
            self.musteri.widget.setHidden(True)
            self.musteri.gormewidget.setHidden(False)
            self.plakagörme.setText(f"Plaka: {result.get('plaka', '')}")
            self.sirasi.setText(f"Sıranız: {result.get('sira', '')}")
            self.yapilanislemler2.setText(f"Yapılan İşlemler: {result.get('yapilanislemler', '')}")
            self.tutar2.setText(f"Tutar: {result.get('tutar', '')}")
        else:
            QMessageBox.warning(self,"hata","hata")

    def yoneticiGiris(self):
        self.stackedWidget.setCurrentIndex(8)       
    def giris(self):
        self.username=self.yonetici1.eposta.text().strip()
        self.sifre=self.yonetici1.sifre.text().strip()

        if self.users_collection.find_one({"kullaniciAdi":self.username,"sifre":self.sifre}):
            self.stackedWidget.setCurrentIndex(9)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = anaSayfa()
    window.show()
    sys.exit(app.exec())