from PyQt6.QtWidgets import QMainWindow, QApplication, QLineEdit, QMessageBox, QPushButton
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
        
        self.email_input=self.findChild(QLineEdit,'txt_email' )
        self.password_input=self.findChild(QLineEdit, 'txt_password')
        
        self.btn_loin=self.findChild(QPushButton,'btn_loin')
        self.btn_register=self.findChild(QPushButton,'btn_register')

        self.btn_loin.clicked.connect(self.login)
        self.btn_register.clicked.connect(self.show_register)
        
    
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
        else:
            msg=Alert()
            msg.error_message('Invalid email or password')
    
    
    def show_register(self):
        register= Register()
        register.show()

class Register(QMainWindow):
    def __int__(self):
        super().__init__()
        uic.loadUi('ui/register.ui',self)

        self.email_input=self.findChild(QLineEdit,'txt_email')
        self.name_input=self.findChild(QLineEdit,'txt_name')
        self.password_input=self.findChild(QLineEdit,'txt_password')
        self.confirm_password_input=self.findChild(QLineEdit,'txt_confirm_password')

        self.btn_register=self.findChild(QPushButton,'btn_register')
        self.btn_login=self.findChild(QPushButton,'btn_login')

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

        user= database.find_user_by_email(email,password)
        if user:
            msg=Alert()
            msg.error_message('Email already exists')
        else:
            database.create_user(email, password)
            msg=Alert()
            msg.error_message('Registration successful')
            self.close()
    



 
if __name__ == '__main__':
    app= QApplication (sys.argv)
    login = Login()
    login.show()
    sys.exit(app.exec())