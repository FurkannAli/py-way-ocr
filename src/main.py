import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QSystemTrayIcon,
    QMenu, QStyle
)
from PySide6.QtCore import Qt, QThread, Signal, Slot
from PySide6.QtGui import QKeySequence, QShortcut

from capture import capture_region
from ocr_engine import extract_text
from window import Ui_Form


class OCRWorker(QThread):
    #worker thread so slurp or ((spectacle)) doesnt freeze the gui
    finished = Signal(str)
    status_update = Signal(str)

    def __init__(self, lang: str, psm: int):
        super().__init__()
        self.lang = lang
        self.psm = psm

    def run(self):
        self.status_update.emit("Selecting region...")
        image_path = capture_region()

        if not image_path:
            self.status_update.emit("Capture cancelled or failed.")
            self.finished.emit("")
            return
        
        self.status_update.emit("Running OCR...")
        text = extract_text(image_path, lang=self.lang, psm=self.psm)

        self.status_update.emit("Ready")
        self.finished.emit(text)

class OCRCompanionApp(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

        #uummmmmm i think setting icons like this isn't really optimal..
        self.program_icon = self.style().standardIcon(QStyle.StandardPixmap.SP_FileDialogContentsView)
        self.setWindowIcon(self.program_icon)

        self.setup_combo_data()

        self.ui.btn_capture.clicked.connect(self.start_ocr_process)
        self.ui.btn_copy.clicked.connect(self.copy_to_clipboard)

        self.ui.lbl_status.setText("Ready")

        self.init_shortcuts()
        self.init_tray()

    def setup_combo_data(self):
        #attaches actual data to the combo box 
        #cant this be ((dynamic))?? ( ╹ -╹)?
        self.ui.combo_lang.clear()
        self.ui.combo_lang.addItem("English (eng)", "eng")
        self.ui.combo_lang.addItem("Japanese - Horizontal (jpn)", "jpn")
        self.ui.combo_lang.addItem("Japanese - Vertical (jpn_vert)", "jpn_vert")
        self.ui.combo_lang.addItem("Chinese Sim. - Horizontal (chi_sim)", "chi_sim")
        self.ui.combo_lang.addItem("Chinese Sim. - Vertical (chi_sim_vert)", "chi_sim_vert")
        self.ui.combo_lang.addItem("Japanese + English", "jpn+eng")
        self.ui.combo_lang.addItem("Chinese Sim. + English", "chi_sim+eng")



        self.ui.combo_psm.clear()
        self.ui.combo_psm.addItem("6 (Single Block - Horizontal)", 6)
        self.ui.combo_psm.addItem("5 (Single Block - Vertical)", 5)
        self.ui.combo_psm.addItem("11 (Sparse Text)", 11)
        self.ui.combo_psm.addItem("3 (Auto)", 3)

    def init_shortcuts(self):
        #ctrl+s also triggers capture
        self.shortcut_capture = QShortcut(QKeySequence("Ctrl+S"), self)
        self.shortcut_capture.activated.connect(self.start_ocr_process)

    #tray thing
    def init_tray(self):
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(self.program_icon)

        tray_menu = QMenu()
        capture_action = tray_menu.addAction("Capture Snippet")
        capture_action.triggered.connect(self.start_ocr_process)

        toggle_action = tray_menu.addAction("Show/Hide Window")
        toggle_action.triggered.connect(self.toggle_window)

        tray_menu.addSeparator()
        quit_action = tray_menu.addAction("Quit")
        quit_action.triggered.connect(QApplication.quit)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

    def toggle_window(self):
        if self.isVisible():
            self.hide()
        else:
            self.showNormal()
            self.activateWindow()

    @Slot()
    def start_ocr_process(self):
        self.ui.btn_capture.setEnabled(False)

        lang = self.ui.combo_lang.currentData()
        psm = self.ui.combo_psm.currentData()

        self.worker = OCRWorker(lang=lang, psm=psm)
        self.worker.status_update.connect(self.update_status)
        self.worker.finished.connect(self.handle_ocr_finished)
        self.worker.start()

    @Slot(str)
    def update_status(self, message: str):
        self.ui.lbl_status.setText(message)

    @Slot(str)
    def handle_ocr_finished(self, text: str):
        if text:
            self.ui.text_result.setText(text)
        self.ui.btn_capture.setEnabled(True)

    def copy_to_clipboard(self):
        text = self.ui.text_result.toPlainText()
        if text:
            clipboard = QApplication.clipboard()
            clipboard.setText(text)
            self.ui.lbl_status.setText("Copited to clipboard.")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)

    #prevent app termination while tray icon is active
    app.setQuitOnLastWindowClosed(False)

    window = OCRCompanionApp()
    window.show()

    sys.exit(app.exec())