from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6 import uic
import sys
import database

class Alert(QMessageBox):
    def error_message(self,message):
        self.setIcon(QMessageBox.Icon.Critical)
        self.setText(message)
        self.setWindowTitle('Error')
        self.exec()

    def success_message(self,message):
            self.setIcon(QMessageBox.Icon.Information)
            self.setText(message)
            self.setWindowTitle('success')
            self.exec()

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/login.ui', self)
        
        self.email_input=self.findChild(QLineEdit,'loginemail' )
        self.password_input=self.findChild(QLineEdit, 'loginpassword')
        
        self.btn_login=self.findChild(QPushButton,'Buttonlogin')
        self.btn_register=self.findChild(QPushButton,'Buttonsignup')
        self.Buttoneye_2=self.findChild(QPushButton,'Buttoneye_2')

        self.btn_login.clicked.connect(self.login)
        self.btn_register.clicked.connect(self.show_register)
        
        self.Buttoneye_2.clicked.connect(lambda: self.hiddenOrShow(self.password_input, self.Buttoneye_2))
        
    def hiddenOrShow(self, input:QLineEdit, button:QPushButton):
        if input.echoMode() == QLineEdit.EchoMode.Password:
            input.setEchoMode(QLineEdit.EchoMode.Normal)
            button.setIcon(QIcon("img/eye.png"))
        else:
            input.setEchoMode(QLineEdit.EchoMode.Password)
            button.setIcon(QIcon("img/hidden.png"))
    
    def login(self):
        email=self.email_input.text()
        password=self.password_input.text()

        if email=='':
            msg=Alert
            msg.error_message('Please enter email address')
            self.email_input.setFocus()
            return
    
        if password=='':
            msg=Alert()
            msg.error_message('Please enter password')
            self.password_input.setFocus()
            return
    
        user= database.find_user_user_by_email_and_password(email,password)
        if user:
            msg=Alert()
            msg.success_message('Login successful')
            self.show_main(user['id'])
        else:
            msg=Alert()
            msg.error_message('Invalid email or password')
    
    
    def show_register(self):
        self.register= Register()
        self.register.show()
        self.close()
        
    def show_main(self, user_id):
        self.main= Main(user_id)
        self.main.show()
        self.close() 

class Register(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/register.ui', self)

        self.email_input=self.findChild(QLineEdit,'loginemail')
        self.name_input=self.findChild(QLineEdit,'loginname')
        self.password_input=self.findChild(QLineEdit,'loginpassword')
        self.confirm_password_input=self.findChild(QLineEdit,'loginconfirm')

        self.btn_register=self.findChild(QPushButton,'Buttonsignup')
        self.btn_login=self.findChild(QPushButton,'btn_login')
        self.btn_eye=self.findChild(QPushButton,'eyebtn')
        self.btn_eye2=self.findChild(QPushButton,'eyebtn_2')
        
        self.btn_eye.clicked.connect(lambda: self.hiddenOrShow(self.password_input, self.btn_eye))
        self.btn_eye2.clicked.connect(lambda: self.hiddenOrShow(self.confirm_password_input, self.btn_eye2))
        
        self.btn_login.clicked.connect(self.show_login)
        self.btn_register.clicked.connect(self.register)
        
    def hiddenOrShow(self, input:QLineEdit, button:QPushButton):
        if input.echoMode() == QLineEdit.EchoMode.Password:
            input.setEchoMode(QLineEdit.EchoMode.Normal)
            button.setIcon(QIcon("img/eye.png"))
        else:
            input.setEchoMode(QLineEdit.EchoMode.Password)
            button.setIcon(QIcon("img/hidden.png"))

    def register(self):
        email=self.email_input.text()
        name=self.name_input.text()
        password=self.password_input.text()
        confirm_password=self.confirm_password_input.text()
    
        if email=='':
            msg=Alert
            msg.error_message('Please enter email address')
            self.email_input.setFocus()
            return
        
        if name =='':
            msg=Alert()
            msg.error_message('Please enter name')
            self. name_input.setFocus()
            return
    
        if password=='':
            msg=Alert()
            msg.error_message('Please enter password')
            self.password_input.setFocus()
            return
        
        if confirm_password=='':
            msg=Alert()
            msg.error_message('Please enter confirm password')
            self.password_input.setFocus()
            return
        
        if password !=confirm_password:
            msg=Alert()
            msg.error_message('Password and confirm password does not match ')
            self.confirm_password_input.setFocus()
            return

        user= database.find_user_by_email(email)
        if user:
            msg=Alert()
            msg.error_message('Email already exists')
        else:
            database.create_user(email,name,password)
            msg=Alert()
            msg.success_message('Registration successful')
            self.show_login()
            self.close()
            
    def show_login(self):
        self.login=Login()
        self.login.show()
        self.close()
    
class Main(QMainWindow):
    def __init__(self, user_id):
        super().__init__()
        uic.loadUi('ui/mainwindow.ui',self)
        self.user_id = user_id
        self.user=database.find_user_by_id(user_id)
        

        self.btn_caidat = self.findChild(QPushButton,'btn_caidat')
        self.btn_chucnang = self.findChild(QPushButton,'btn_chucnang')
        self.btn_lienhe = self.findChild(QPushButton,'btn_lienhe')
        self.btn_tintuc = self.findChild(QPushButton,'btn_tintuc')
        self.btn_avatar=self.findChild(QPushButton,'btn_avatar')
        
        
        self.stackedWidget = self.findChild(QStackedWidget,'stackedWidget')
        
        self.btn_caidat.clicked.connect(lambda: self.navigation(2))
        self.btn_chucnang.clicked.connect(lambda: self.navigation(3))
        self.btn_lienhe.clicked.connect(lambda: self.navigation(1))
        self.btn_tintuc.clicked.connect(lambda: self.navigation(0))
        self.btn_avatar.clicked.connect(self.update_avatar)

    def navigation(self, index):
        self.stackedWidget.setCurrentIndex(index)

    def load_user_info(self):
        self.lb_name = self.findChild(QLabel, 'lb_name' )
        self.lb_email = self.findChild(QLabel, 'lb_email')
        self.lb_name.setText(self.user["name"]) 
        self.lb_email.setText(self.user["email"])
        self.btn_avatar.setIcon(QIcon(self.user["avatar"]))

    def update_avatar(self):
        file,_= QFileDialog.getOpenFileName(self,"Select Image","","Image Files(*.png *.jpg *jpeg *.bmp)")
        if file:
            self.user["avatar"]=file
            self.btn_avatar.setIcon(QIcon(file))
            database.update_user_avatar(self.user_id,file)


if __name__ == '__main__':
    app= QApplication (sys.argv)
    login = Login()
    login.show()
    login = Main(2)
    login.show()
    sys.exit(app.exec())