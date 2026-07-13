import numpy as np

from matplotlib.backends.backend_qtagg import (
    FigureCanvasQTAgg,
    NavigationToolbar2QT
)

from matplotlib.figure import Figure

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout
)


class SpectrumWidget(QWidget):

    def __init__(self):

        super().__init__()


        self.figure = Figure(
            figsize=(10, 6)
        )


        self.canvas = FigureCanvasQTAgg(
            self.figure
        )


        self.toolbar = NavigationToolbar2QT(
            self.canvas,
            self
        )


        layout = QVBoxLayout()


        layout.setContentsMargins(
            0,
            0,
            0,
            0
        )


        layout.addWidget(
            self.toolbar
        )


        layout.addWidget(
            self.canvas
        )


        self.setLayout(
            layout
        )


        self.ax = self.figure.add_subplot(
            111
        )


        self.reset_axes()



    # ==================================================
    # Reset
    # ==================================================

    def reset_axes(self):

        self.ax.clear()


        self.ax.set_title(
            "Frequency Spectrum"
        )


        self.ax.set_xlabel(
            "Frequency (Hz)"
        )


        self.ax.set_ylabel(
            "Amplitude"
        )


        self.ax.grid(
            True
        )


        self.canvas.draw()



    # ==================================================
    # Plot FFT Result
    # ==================================================

    def plot_spectrum(
        self,
        frequency,
        amplitude,
        title="FFT Spectrum"
    ):


        self.ax.clear()



        self.ax.plot(
            frequency,
            amplitude,
            linewidth=0.8
        )



        self.ax.set_title(
            title
        )


        self.ax.set_xlabel(
            "Frequency (Hz)"
        )


        self.ax.set_ylabel(
            "Amplitude"
        )


        self.ax.grid(
            True
        )


        self.figure.tight_layout()


        self.canvas.draw()