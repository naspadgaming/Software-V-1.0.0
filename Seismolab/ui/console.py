from datetime import datetime

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTextEdit
)



class ConsoleWidget(QWidget):


    def __init__(self):

        super().__init__()



        self.output = QTextEdit()


        self.output.setReadOnly(
            True
        )



        layout = QVBoxLayout()


        layout.addWidget(
            self.output
        )


        self.setLayout(
            layout
        )



        self.log(
            "[SYSTEM] Console initialized"
        )



    # ======================================
    # Write Log
    # ======================================

    def log(self, message):


        time = datetime.now().strftime(
            "%H:%M:%S"
        )



        text = (
            f"[{time}] {message}"
        )



        self.output.append(
            text
        )