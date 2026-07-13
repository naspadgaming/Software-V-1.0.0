from PySide6.QtWidgets import QMainWindow

from widgets.picker import PickerWidget



class PickerWindow(QMainWindow):


    def __init__(self, trace):

        super().__init__()



        self.trace = trace



        self.setWindowTitle(
            "Arrival Picker"
        )


        self.resize(
            1000,
            700
        )



        self.picker = PickerWidget()



        self.setCentralWidget(
            self.picker
        )



        self.picker.plot_trace(
            trace
        )



        self.picker.picked.connect(
            self.pick_received
        )



        self.arrival_time = None



    # ======================================
    # Receive Pick
    # ======================================

    def pick_received(self, time):


        self.arrival_time = time



        print(
            f"P Arrival : {time:.3f} s"
        )