from PySide6.QtCore import QSize
from PySide6.QtWidgets import QToolBar

from ui.icons import icon_path



class MainToolBar(QToolBar):

    def __init__(self, parent):

        super().__init__(
            "Main Toolbar"
        )


        self.setMovable(
            False
        )


        self.setIconSize(
            QSize(
                24,
                24
            )
        )



        # ==========================================
        # Open
        # ==========================================

        parent.open_action.setToolTip(
            "Open seismic waveform file"
        )


        self.addAction(
            parent.open_action
        )



        self.addSeparator()



        # ==========================================
        # Processing
        # ==========================================

        parent.filter_action.setToolTip(
            "Apply bandpass filter"
        )


        parent.fft_action.setToolTip(
            "Frequency spectrum analysis"
        )


        parent.spectrogram_action.setToolTip(
            "Time-frequency spectrogram"
        )


        parent.pick_action.setToolTip(
            "Pick seismic arrival"
        )



        self.addAction(
            parent.filter_action
        )


        self.addAction(
            parent.fft_action
        )


        self.addAction(
            parent.spectrogram_action
        )


        self.addAction(
            parent.pick_action
        )