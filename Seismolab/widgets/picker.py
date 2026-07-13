from PySide6.QtCore import Signal

from matplotlib.backends.backend_qtagg import (
    FigureCanvasQTAgg
)

from matplotlib.figure import Figure

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout
)


class PickerWidget(QWidget):


    picked = Signal(float)



    def __init__(self):

        super().__init__()



        self.figure = Figure(
            figsize=(10,6)
        )


        self.canvas = FigureCanvasQTAgg(
            self.figure
        )


        layout = QVBoxLayout()


        layout.addWidget(
            self.canvas
        )


        self.setLayout(
            layout
        )


        self.ax = self.figure.add_subplot(
            111
        )


        self.trace = None

        self.pick_line = None



        self.canvas.mpl_connect(

            "button_press_event",

            self.on_click

        )



    # ======================================
    # Load Trace
    # ======================================

    def plot_trace(self, trace):


        self.trace = trace


        self.ax.clear()



        data = trace.data.astype(
            float
        )


        fs = trace.stats.sampling_rate



        time = (
            range(len(data))
        )


        time = [
            x / fs
            for x in time
        ]



        self.ax.plot(

            time,

            data

        )



        self.ax.set_xlabel(
            "Time (s)"
        )


        self.ax.set_ylabel(
            "Amplitude"
        )


        self.ax.set_title(
            trace.id
        )


        self.ax.grid(
            True
        )



        self.canvas.draw()



    # ======================================
    # Mouse Click
    # ======================================

    def on_click(self,event):


        if event.xdata is None:

            return



        pick_time = event.xdata



        if self.pick_line:

            self.pick_line.remove()



        self.pick_line = self.ax.axvline(

            pick_time

        )



        self.canvas.draw()



        self.picked.emit(
            pick_time
        )