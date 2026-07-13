from PySide6.QtWidgets import QMainWindow

from core.spectrogram import SpectrogramAnalyzer

from widgets.spectrogram import SpectrogramWidget



class SpectrogramWindow(QMainWindow):


    def __init__(self, trace):

        super().__init__()


        self.trace = trace


        self.setWindowTitle(
            "Spectrogram"
        )


        self.resize(
            1000,
            700
        )


        self.widget = SpectrogramWidget()


        self.setCentralWidget(
            self.widget
        )


        self.calculate()



    # ======================================
    # Calculate
    # ======================================

    def calculate(self):


        analyzer = SpectrogramAnalyzer(
            self.trace
        )


        frequency, time, power = analyzer.compute()



        self.widget.plot_spectrogram(

            frequency,

            time,

            power,

            f"Spectrogram {self.trace.id}"

        )