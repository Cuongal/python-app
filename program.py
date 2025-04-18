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
        self.btn_application = self.findChild(QPushButton,'btn_application')
        self.btn_schedule = self.findChild(QPushButton,'btn_schedule')
        
        self.stackedWidget = self.findChild(QStackedWidget,'stackedWidget')
        
        # Initialize schedule page elements
        self.calendar = self.findChild(QCalendarWidget, 'calendar')
        self.date_label = self.findChild(QLabel, 'date_label')
        self.schedule_table = self.findChild(QTableWidget, 'schedule_table')

        # Initialize application page elements
        self.applications_table = self.findChild(QTableWidget, 'applications_table')
        self.btn_new_application = self.findChild(QPushButton, 'btn_new_application')
        self.btn_edit_application = self.findChild(QPushButton, 'btn_edit_application')
        self.btn_delete_application = self.findChild(QPushButton, 'btn_delete_application')
        
        # Set table properties
        self.schedule_table.setColumnCount(5)
        self.schedule_table.setHorizontalHeaderLabels(['Môn học', 'Bắt đầu', 'Kết thúc', 'Giáo viên', 'Phòng học'])
        self.schedule_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.schedule_table.setAlternatingRowColors(True)
        
        # Set applications table properties
        self.applications_table.setColumnCount(6)
        self.applications_table.setHorizontalHeaderLabels(['Loại đơn', 'Người nhận', 'Tiêu đề', 'Ngày bắt đầu', 'Ngày kết thúc', 'Trạng thái'])
        self.applications_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.applications_table.setAlternatingRowColors(True)
        
        # Connect buttons
        self.btn_caidat.clicked.connect(lambda: self.navigation(3))
        self.btn_chucnang.clicked.connect(lambda: self.navigation(4))
        self.btn_lienhe.clicked.connect(lambda: self.navigation(2))
        self.btn_tintuc.clicked.connect(lambda: self.navigation(0))
        self.btn_application.clicked.connect(lambda: self.navigation(1))
        self.btn_schedule.clicked.connect(lambda: self.navigation(5))
        self.btn_avatar.clicked.connect(self.update_avatar)
        
        # Connect application buttons
        if self.btn_new_application:
            self.btn_new_application.clicked.connect(self.create_new_application)
        if self.btn_edit_application:
            self.btn_edit_application.clicked.connect(self.edit_application)
        if self.btn_delete_application:
            self.btn_delete_application.clicked.connect(self.delete_application)
        
        # Connect calendar selection changed signal
        if self.calendar:
            self.calendar.selectionChanged.connect(self.update_schedule)
            self.calendar.setSelectedDate(QDate.currentDate())
            self.update_schedule()
        
        # Load user info and applications
        self.load_applications()
        self.load_user_info()
        
    def load_user_info(self):
        self.user = database.find_user_by_id(self.user_id)
        self.btn_avatar = self.findChild(QPushButton,'btn_avatar')
        self.txt_name = self.findChild(QLineEdit,'txt_name')
        self.txt_email = self.findChild(QLineEdit,'txt_email')
        self.d_dob = self.findChild(QDateEdit,'d_dob')
        self.cb_gender = self.findChild(QComboBox,'cb_gender')
        self.btn_update_info = self.findChild(QPushButton,'btn_update_info')
        self.name_header = self.findChild(QLabel,'name_header')
        self.btn_update_info.clicked.connect(self.update_info)


        self.txt_name.setText(self.user["name"])
        self.txt_email.setText(self.user["email"])
        self.txt_email.setReadOnly(True)
        self.d_dob.setDate(QDate.fromString(self.user["birthday"], "dd/MM/yyyy"))
        self.cb_gender.setCurrentText(self.user["gender"])
        self.btn_avatar.setIcon(QIcon(self.user["avatar"]))
        self.name_header.setText(self.user["name"])

    def update_info(self):
        name = self.txt_name.text()
        dob = self.d_dob.date().toString("dd/MM/yyyy")
        gender = self.cb_gender.currentText()
        database.update_user(self.user_id, name, dob, gender)
        msg = Alert()
        msg.success_message("Update info success")
        self.load_user_info() 
    
    def update_avatar(self):
        file,_ = QFileDialog.getOpenFileName(self,"Select Image","","Image Files(*.png *.jpg *jpeg *.bmp)")
        if file:
            self.user["avatar"] = file
            self.btn_avatar.setIcon(QIcon(file))
            database.update_user_avatar(self.user_id, file)

    def load_applications(self):
        """Load applications for the current user"""
        if not self.applications_table:
            return
            
        # Get applications from database
        applications = database.get_applications_by_user_id(self.user_id)
        
        # Clear existing data
        self.applications_table.setRowCount(0)
        
        # Add applications to table
        for app in applications:
            row = self.applications_table.rowCount()
            self.applications_table.insertRow(row)
            
            # Create items for each column
            items = [
                QTableWidgetItem(app['type']),
                QTableWidgetItem(app['recipient']),
                QTableWidgetItem(app['title']),
                QTableWidgetItem(app['start_date']),
                QTableWidgetItem(app['end_date']),
                QTableWidgetItem(app['status'])
            ]
            
            # Set items in table
            for col, item in enumerate(items):
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.applications_table.setItem(row, col, item)
                
            # Store application ID in first item
            self.applications_table.item(row, 0).setData(Qt.ItemDataRole.UserRole, app['id'])

    def create_new_application(self):
        dialog = ApplicationDialog(self)
        if dialog.exec() == QDialog.accept:
            data = dialog.get_data()
            data['user_id'] = self.user_id
            data['status'] = 'pending'
            database.create_application(data)
            self.load_applications()
    
    def edit_application(self):
        current_row = self.applications_table.currentRow()
        if current_row >= 0:
            application_id = int(self.applications_table.item(current_row, 0).text())
            application = database.get_application_by_id(application_id)
            if application:
                dialog = ApplicationDialog(self, application)
                if dialog.exec() == QDialog.accept:
                    data = dialog.get_data()
                    data['id'] = application_id
                    database.update_application(data)
                    self.load_applications()
    
    def delete_application(self):
        current_row = self.applications_table.currentRow()
        if current_row >= 0:
            application_id = int(self.applications_table.item(current_row, 0).text())
            reply = QMessageBox.question(
                self,
                'Xác nhận xóa',
                'Bạn có chắc chắn muốn xóa đơn này?',
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )
            if reply == QMessageBox.Yes:
                database.delete_application(application_id)
                self.load_applications()

    def navigation(self, index):
        print(f"Navigating to index: {index}")  # Debug print
        self.stackedWidget.setCurrentIndex(index)
            
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

class ApplicationDialog(QDialog):
    def __init__(self, parent=None, application_data=None):
        super().__init__(parent)
        uic.loadUi('ui/application_dialog.ui', self)
        
        # Set window title based on whether we're creating or editing
        self.setWindowTitle("Tạo đơn mới" if not application_data else "Sửa đơn")
        
        # Connect signals
        self.save_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)
        
        # Set current date for date inputs
        self.start_date.setDate(QDate.currentDate())
        self.end_date.setDate(QDate.currentDate())
        
        # If editing existing application, populate fields
        if application_data:
            self.type_combo.setCurrentText(application_data['type'])
            self.recipient_input.setText(application_data['recipient'])
            self.title_input.setText(application_data['title'])
            self.content_input.setText(application_data['content'])
            self.start_date.setDate(QDate.fromString(application_data['start_date'], 'yyyy-MM-dd'))
            self.end_date.setDate(QDate.fromString(application_data['end_date'], 'yyyy-MM-dd'))
    
    def get_data(self):
        """Get form data as dictionary"""
        return {
            'type': self.type_combo.currentText(),
            'recipient': self.recipient_input.text(),
            'title': self.title_input.text(),
            'content': self.content_input.toPlainText(),
            'start_date': self.start_date.date().toString('yyyy-MM-dd'),
            'end_date': self.end_date.date().toString('yyyy-MM-dd')
        }

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # login = Login()
    main = Main(2)
    main.show()
    sys.exit(app.exec())