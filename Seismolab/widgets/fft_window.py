from PySide6.QtWidgets import (
    QMainWindow
)

from core.fft import FFTAnalyzer

from widgets.spectrum import SpectrumWidget



class FFTWindow(QMainWindow):

    def __init__(self, trace):

        super().__init__()


        self.trace = trace


        self.setWindowTitle(
            "FFT Spectrum"
        )


        self.resize(
            900,
            600
        )


        self.spectrum = SpectrumWidget()


        self.setCentralWidget(
            self.spectrum
        )


        self.calculate()



    # ======================================
    # Calculate FFT
    # ======================================

    def calculate(self):

        analyzer = FFTAnalyzer(
            self.trace
        )


        frequency, amplitude = analyzer.compute()


        dominant = analyzer.dominant_frequency()



        self.spectrum.plot_spectrum(

            frequency,

            amplitude,

            f"FFT {self.trace.id} | Dominant {dominant:.2f} Hz"

        )