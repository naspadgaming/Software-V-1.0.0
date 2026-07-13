from PySide6.QtWidgets import QMainWindow

from widgets.waveform import WaveformWidget

from core.trigger import TriggerAnalyzer



class TriggerWindow(QMainWindow):


    def __init__(self, trace):

        super().__init__()



        self.trace = trace



        self.setWindowTitle(
            "STA/LTA Detector"
        )


        self.resize(
            1100,
            700
        )



        self.waveform = WaveformWidget()



        self.setCentralWidget(
            self.waveform
        )



        self.run_detection()



    # ======================================
    # Detection
    # ======================================

    def run_detection(self):


        self.waveform.plot_trace(
            self.trace
        )


        analyzer = TriggerAnalyzer(
            self.trace
        )


        events = analyzer.detect()



        for event in events:


            start = (

                event[0]

                /

                self.trace.stats.sampling_rate

            )


            end = (

                event[1]

                /

                self.trace.stats.sampling_rate

            )


            self.waveform.ax.axvspan(

                start,

                end,

            )



        self.waveform.canvas.draw()