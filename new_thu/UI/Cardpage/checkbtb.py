from PyQt5.QtWidgets import QCheckBox


class QtBoxStyleCheckBox2(QCheckBox):
    def __init__(self):
        super(QtBoxStyleCheckBox2, self).__init__()
        self.setText("Qt Box")
        self.setStyleSheet("""
        QCheckBox {
            font-size: 15px;
        }

        QCheckBox::indicator {
            padding-top: 1px;
            width: 40px;
            height: 30px;
            border: none;
        }

        QCheckBox::indicator:unchecked {
            image: url(PATH_TO_IMG);
        }

        QCheckBox::indicator:checked {
            image: url(PATH_TO_IMG);
        }
        """)
