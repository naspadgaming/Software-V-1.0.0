from PySide6.QtWidgets import QMainWindow

from core.psd import PSDAnalyzer

from widgets.psd import PSDWidget



class PSDWindow(QMainWindow):


    def __init__(self, trace):

        super().__init__()



        self.trace = trace



        self.setWindowTitle(
            "Power Spectral Density"
        )


        self.resize(
            1000,
            700
        )



        self.widget = PSDWidget()



        self.setCentralWidget(
            self.widget
        )



        self.calculate()



    # ======================================
    # Calculate PSD
    # ======================================

    def calculate(self):


        analyzer = PSDAnalyzer(
            self.trace
        )


        frequency, power = analyzer.compute()



        peak = analyzer.peak_frequency()



        self.widget.plot_psd(

            frequency,

            power,

            f"PSD {self.trace.id} | Peak {peak:.2f} Hz"

        )