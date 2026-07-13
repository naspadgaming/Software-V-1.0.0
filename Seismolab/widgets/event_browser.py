from PySide6.QtCore import Signal

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTableWidget,
    QTableWidgetItem,
    QPushButton
)



class EventBrowser(QWidget):


    event_selected = Signal(int)



    def __init__(self):

        super().__init__()



        self.events = []



        self.table = QTableWidget()



        self.table.setColumnCount(
            5
        )



        self.table.setHorizontalHeaderLabels(

            [

                "ID",

                "Station",

                "Channel",

                "Time",

                "File"

            ]

        )



        self.table.cellClicked.connect(

            self.select_event

        )



        self.refresh_button = QPushButton(

            "Refresh"

        )


        self.refresh_button.clicked.connect(

            self.refresh

        )



        layout = QVBoxLayout()



        layout.addWidget(

            self.table

        )


        layout.addWidget(

            self.refresh_button

        )



        self.setLayout(

            layout

        )



    # ======================================
    # Load Events
    # ======================================

    def load_events(self, events):


        self.events = events



        self.table.setRowCount(

            len(events)

        )



        for row, event in enumerate(events):


            # database format:

            # id,

            # filename,

            # start_time,

            # station,

            # network,

            # channel,

            # magnitude,

            # location



            values = [

                event[0],

                event[3],

                event[5],

                event[2],

                event[1]

            ]



            for col, value in enumerate(values):


                self.table.setItem(

                    row,

                    col,

                    QTableWidgetItem(

                        str(value)

                    )

                )



        self.table.resizeColumnsToContents()



    # ======================================
    # Select Event
    # ======================================

    def select_event(self,row,column):


        if row < 0:

            return



        event_id = self.table.item(

            row,

            0

        ).text()



        self.event_selected.emit(

            int(event_id)

        )



    # ======================================
    # Refresh Placeholder
    # ======================================

    def refresh(self):


        pass