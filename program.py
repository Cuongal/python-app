from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import QDate, Qt
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
        self.user = database.find_user_by_id(user_id)

        # Initialize UI elements
        self.btn_caidat = self.findChild(QPushButton,'btn_caidat')
        self.btn_chucnang = self.findChild(QPushButton,'btn_chucnang')
        self.btn_lienhe = self.findChild(QPushButton,'btn_lienhe')
        self.btn_tintuc = self.findChild(QPushButton,'btn_tintuc')
        self.btn_avatar = self.findChild(QPushButton,'btn_avatar')
        
        # Find schedule button
        self.btn_schedule = self.findChild(QLabel, 'label_47')  # Thời khoá biểu label
        
        self.stackedWidget = self.findChild(QStackedWidget,'stackedWidget')
        
        # Initialize schedule page elements
        self.calendar = self.findChild(QCalendarWidget, 'calendar')
        self.date_label = self.findChild(QLabel, 'date_label')
        self.schedule_table = self.findChild(QTableWidget, 'schedule_table')

        if not self.calendar or not self.date_label or not self.schedule_table:
            print("Failed to find schedule widgets!")
            return
        
        # Set table properties
        self.schedule_table.setColumnCount(5)
        self.schedule_table.setHorizontalHeaderLabels(['Môn học', 'Bắt đầu', 'Kết thúc', 'Giáo viên', 'Phòng học'])
        self.schedule_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.schedule_table.setAlternatingRowColors(True)
        
        # Connect buttons
        self.btn_caidat.clicked.connect(lambda: self.navigation(2))
        self.btn_chucnang.clicked.connect(lambda: self.navigation(3))
        self.btn_lienhe.clicked.connect(lambda: self.navigation(1))
        self.btn_tintuc.clicked.connect(lambda: self.navigation(0))
        self.btn_avatar.clicked.connect(self.update_avatar)
        
        # Make schedule label clickable and connect it
        if self.btn_schedule:
            self.btn_schedule.setStyleSheet("QLabel { cursor: pointer; }")
            self.btn_schedule.mousePressEvent = lambda e: self.navigation(4)  # 4 is the index of schedule page
        
        # Connect calendar selection changed signal
        self.calendar.selectionChanged.connect(self.update_schedule)
        
        # Initialize schedule with current date
        self.calendar.setSelectedDate(QDate.currentDate())
        self.update_schedule()
        
        # Load user info
        self.load_user_info()

    def navigation(self, index):
        print(f"Navigating to index: {index}")  # Debug print
        self.stackedWidget.setCurrentIndex(index)

    def load_user_info(self):
        self.lb_name = self.findChild(QLabel, 'lb_name')
        self.lb_email = self.findChild(QLabel, 'lb_email')
        if self.user:
            self.lb_name.setText(self.user["name"])
            self.lb_email.setText(self.user["email"])
            if "avatar" in self.user:
                self.btn_avatar.setIcon(QIcon(self.user["avatar"]))

    def update_avatar(self):
        file,_= QFileDialog.getOpenFileName(self,"Select Image","","Image Files(*.png *.jpg *jpeg *.bmp)")
        if file:
            self.user["avatar"]=file
            self.btn_avatar.setIcon(QIcon(file))
            database.update_user_avatar(self.user_id,file)
            
    def update_schedule(self):
        if not self.calendar or not self.schedule_table:
            print("Schedule widgets not found!")
            return
            
        # Get selected date
        selected_date = self.calendar.selectedDate()
        date_str = selected_date.toString('yyyy-MM-dd')
        
        # Update date label
        self.date_label.setText(f"Thời khoá biểu ngày: {selected_date.toString('dd/MM/yyyy')}")
        
        # Get schedule for selected date
        schedule = database.get_schedule_by_date(date_str)
        
        # Clear table
        self.schedule_table.clearContents()
        
        if not schedule:
            # No data found - show message
            self.schedule_table.setRowCount(1)
            no_data_item = QTableWidgetItem("Không có lịch học cho ngày này")
            no_data_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            # Span across all columns
            self.schedule_table.setSpan(0, 0, 1, 5)
            self.schedule_table.setItem(0, 0, no_data_item)
            return
        
        # Reset any previous spans
        self.schedule_table.clearSpans()
        
        # Update table with data
        self.schedule_table.setRowCount(len(schedule))
        
        for row, schedule_item in enumerate(schedule):
            # Create items
            items = [
                QTableWidgetItem(schedule_item['subject']),
                QTableWidgetItem(schedule_item['start_time']),
                QTableWidgetItem(schedule_item['end_time']),
                QTableWidgetItem(schedule_item['teacher']),
                QTableWidgetItem(schedule_item['room'])
            ]
            
            # Set items in table
            for col, item in enumerate(items):
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.schedule_table.setItem(row, col, item)
            
            # Set color for break time
            if schedule_item['type'] == 'break':
                for col in range(5):
                    item = self.schedule_table.item(row, col)
                    if item:
                        item.setBackground(QColor('#FFD700'))  # Gold color for break time

        # Adjust column widths
        self.schedule_table.resizeColumnsToContents()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # login = Login()
    main = Main(1)
    main.show()
    sys.exit(app.exec())