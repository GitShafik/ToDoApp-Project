from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QComboBox, QListWidget, QListWidgetItem, QCheckBox, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import sys

from application.services import TaskService
from domain.task import Task


class TaskQtDesktop:
    def __init__(self, service: TaskService):
        self.service = service
        self.app = QApplication(sys.argv)
        self.window = MainWindow(self.service)

    def run(self):
        self.window.show()
        sys.exit(self.app.exec())


class MainWindow(QMainWindow):
    def __init__(self, service: TaskService):
        super().__init__()
        self.service = service
        self.setWindowTitle("Todo List App")
        self.setMinimumSize(600, 400)

        # Main widget and layout
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        # Add task section
        add_section = QWidget()
        add_layout = QHBoxLayout()
        add_section.setLayout(add_layout)

        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Ange uppgiftens titel")
        add_layout.addWidget(self.task_input)

        self.priority_combo = QComboBox()
        self.priority_combo.addItems(["Låg", "Medium", "Hög"])
        self.priority_combo.setCurrentIndex(1)  # Default to Medium
        add_layout.addWidget(self.priority_combo)

        add_button = QPushButton("Lägg till")
        add_button.clicked.connect(self.add_task)
        add_layout.addWidget(add_button)

        main_layout.addWidget(add_section)

        # Task list
        self.task_list = QListWidget()
        main_layout.addWidget(self.task_list)

        # Buttons section
        buttons_section = QWidget()
        buttons_layout = QHBoxLayout()
        buttons_section.setLayout(buttons_layout)

        refresh_button = QPushButton("Uppdatera lista")
        refresh_button.clicked.connect(self.refresh_tasks)
        buttons_layout.addWidget(refresh_button)

        main_layout.addWidget(buttons_section)

        # Load initial tasks
        self.refresh_tasks()

    def add_task(self):
        title = self.task_input.text().strip()
        if not title:
            QMessageBox.warning(self, "Varning", "Uppgiftens titel kan inte vara tom.")
            return

        priority_map = {0: "low", 1: "medium", 2: "high"}
        priority = priority_map[self.priority_combo.currentIndex()]

        try:
            self.service.create_task(title=title, priority=priority)
            self.task_input.clear()
            self.refresh_tasks()
        except Exception as e:
            QMessageBox.critical(self, "Fel", f"Ett fel uppstod: {str(e)}")

    def refresh_tasks(self):
        self.task_list.clear()
        tasks = self.service.get_all_tasks()
        for task in tasks:
            item = QListWidgetItem()
            widget = TaskItemWidget(task, self.service, parent=self)
            item.setSizeHint(widget.sizeHint())
            self.task_list.addItem(item)
            self.task_list.setItemWidget(item, widget)


class TaskItemWidget(QWidget):
    def __init__(self, task, service, parent= None):
        super().__init__(parent)
        self.task = task
        self.service = service
        self.parent = parent
       
        layout = QHBoxLayout()
        self.setLayout(layout)

        # Checkbox for completed status
        self.checkbox = QCheckBox()
        self.checkbox.setChecked(task.completed)
        self.checkbox.stateChanged.connect(self.on_checkbox_changed)
        layout.addWidget(self.checkbox)

        # Task ID and title
        self.title_label = QLabel(f"{task.id}. {task.title}")
        layout.addWidget(self.title_label)

        # Priority
        self.priority_label = QLabel(f"[{task.priority}]")
        layout.addWidget(self.priority_label)

        # Push everything to the left
        layout.addStretch()

        # Update the title style based on completion status
        self.update_title_style()
        
        
        # Delete button
        self.delete_button = QPushButton("🗑️")
        self.delete_button.setStyleSheet("background-color: transparent;")
        self.delete_button.clicked.connect(self.handle_delete)

        layout.addStretch()
        layout.addWidget(self.delete_button)

    def handle_delete(self):
        task_id = self.task.id
        self.service.delete_task(task_id)
        self.parent.refresh_tasks()
        # self.deleteLater()

       
    def update_title_style(self):
        # Create a font object
        font = QFont()
        # Set strikeout if task is completed
        font.setStrikeOut(self.task.completed)
        # Apply the font to the title label
        self.title_label.setFont(font)
        # Set color when task completed
        
        label = QLabel(self.task.title)
        font = label.font()

        if self.task.completed:
            font.setStrikeOut(True)             
            label.setStyleSheet("color: gray")  
        else:
            font.setStrikeOut(False)
            label.setStyleSheet("color: black")

            label.setFont(font)
           
    def on_checkbox_changed(self, state):
        # Prevent infinite recursion by disconnecting the signal temporarily
        self.checkbox.stateChanged.disconnect(self.on_checkbox_changed)

        try:
            print(f"Task {self.task.id} marked as completed.")
            print(f"State: {Qt.CheckState.Checked}")
            print(f"Completed: {self.task.completed}")
            # Only update if the state has actually changed
            #if self.task.completed != (state == Qt.CheckState.Checked):
            self.parent.service.mark_completed(self.task.id)

            # Update the task's completed status locally
            self.task.completed = (state == Qt.CheckState.Checked)
            # Update the title style
            self.update_title_style()
            # Refresh the task list to show updated status
            self.parent.refresh_tasks()
        except Exception as e:
            QMessageBox.critical(self.parent, "Fel", f"Ett fel uppstod: {str(e)}")
            # Revert checkbox to original state
            self.checkbox.setChecked(self.task.completed)
        finally:
            # Reconnect the signal
            self.checkbox.stateChanged.connect(self.on_checkbox_changed)
    