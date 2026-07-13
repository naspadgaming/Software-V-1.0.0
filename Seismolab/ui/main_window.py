from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QFileDialog,
    QDockWidget,
    QMainWindow,
    QMessageBox,
    QTextEdit,
    QStatusBar,
)

from core.reader import SeismicReader
from core.session import Session
from core.processor import SignalProcessor

from ui.toolbar import MainToolBar
from ui.filter_dialog import BandpassDialog

from widgets.waveform import WaveformWidget


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.session = Session()

        self.setWindowTitle("SeismoLab v0.8")
        self.resize(1400, 900)

        self.create_actions()
        self.create_menu()
        self.create_toolbar()
        self.setup_ui()
        self.connect_signals()

    # ==================================================
    # Actions
    # ==================================================

    def create_actions(self):

        self.open_action = QAction("Open", self)

        self.export_png_action = QAction("Export PNG", self)

        self.export_csv_action = QAction("Export CSV", self)

        self.exit_action = QAction("Exit", self)

        self.filter_action = QAction("Bandpass Filter", self)

        self.fft_action = QAction("FFT", self)

        self.spectrogram_action = QAction("Spectrogram", self)

        self.pick_action = QAction("Pick Arrival", self)

        self.about_action = QAction("About", self)

    # ==================================================
    # Menu
    # ==================================================

    def create_menu(self):

        menu = self.menuBar()

        file_menu = menu.addMenu("File")

        file_menu.addAction(self.open_action)
        file_menu.addSeparator()
        file_menu.addAction(self.export_png_action)
        file_menu.addAction(self.export_csv_action)
        file_menu.addSeparator()
        file_menu.addAction(self.exit_action)

        process = menu.addMenu("Processing")

        process.addAction(self.filter_action)
        process.addAction(self.fft_action)
        process.addAction(self.spectrogram_action)
        process.addAction(self.pick_action)

        help_menu = menu.addMenu("Help")

        help_menu.addAction(self.about_action)

    # ==================================================
    # Toolbar
    # ==================================================

    def create_toolbar(self):

        self.toolbar = MainToolBar(self)

        self.addToolBar(self.toolbar)

    # ==================================================
    # UI
    # ==================================================

    def setup_ui(self):

        self.waveform = WaveformWidget()

        self.setCentralWidget(self.waveform)

        dock = QDockWidget("Explorer", self)

        self.explorer = QTextEdit()

        self.explorer.setReadOnly(True)

        self.explorer.setPlainText("No file loaded.")

        dock.setWidget(self.explorer)

        self.addDockWidget(
            Qt.LeftDockWidgetArea,
            dock
        )

        status = QStatusBar()

        status.showMessage("Ready")

        self.setStatusBar(status)

    # ==================================================
    # Signals
    # ==================================================

    def connect_signals(self):

        self.exit_action.triggered.connect(self.close)

        self.open_action.triggered.connect(
            self.open_file
        )

        self.filter_action.triggered.connect(
            self.bandpass_filter
        )

    # ==================================================
    # Open File
    # ==================================================

    def open_file(self):

        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Open Seismic File",
            "",
            "MiniSEED (*.mseed *.ms);;SAC (*.sac)"
        )

        if not filename:
            return

        try:

            stream = SeismicReader.load(filename)

            self.session.load(
                filename,
                stream
            )

            self.refresh()

            self.statusBar().showMessage(
                "File Loaded"
            )

        except Exception as e:

            QMessageBox.critical(
                self,
                "Error",
                str(e)
            )

    # ==================================================
    # Bandpass
    # ==================================================

    def bandpass_filter(self):

        if self.session.current_stream is None:

            QMessageBox.warning(
                self,
                "Warning",
                "Open a seismic file first."
            )

            return

        dialog = BandpassDialog()

        if dialog.exec():

            p = dialog.values()

            filtered = SignalProcessor.bandpass(
                self.session.current_stream,
                p["freqmin"],
                p["freqmax"],
                p["corners"],
                p["zerophase"]
            )

            self.session.apply(
                filtered,
                f"Bandpass ({p['freqmin']} - {p['freqmax']} Hz)"
            )

            self.refresh()

    # ==================================================
    # Refresh GUI
    # ==================================================

    def refresh(self):

        self.waveform.plot_trace(
            self.session.current_trace()
        )

        self.explorer.setPlainText(
            self.session.info()
        )