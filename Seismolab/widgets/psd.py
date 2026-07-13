from matplotlib.backends.backend_qtagg import (
    FigureCanvasQTAgg,
    NavigationToolbar2QT
)

from matplotlib.figure import Figure

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout
)



class PSDWidget(QWidget):


    def __init__(self):

        super().__init__()



        self.figure = Figure(
            figsize=(10,6)
        )


        self.canvas = FigureCanvasQTAgg(
            self.figure
        )


        self.toolbar = NavigationToolbar2QT(

            self.canvas,

            self

        )


        layout = QVBoxLayout()



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



    # ======================================
    # Plot PSD
    # ======================================

    def plot_psd(

        self,

        frequency,

        power,

        title="PSD"

    ):


        self.ax.clear()



        self.ax.semilogy(

            frequency,

            power

        )



        self.ax.set_title(
            title
        )


        self.ax.set_xlabel(
            "Frequency (Hz)"
        )


        self.ax.set_ylabel(
            "Power"
        )


        self.ax.grid(
            True
        )



        self.figure.tight_layout()


        self.canvas.draw()