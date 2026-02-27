import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout,
    QListWidget, QListWidgetItem, QFrame
)
from PyQt5.QtCore import Qt

# =====================================================
# Compatibility Matrix
# =====================================================
COMPATIBILITY = {
    "P1": {"S1": False, "S2": True,  "S3": False, "S4": False, "S5": False},
    "P2": {"S1": True,  "S2": False, "S3": False, "S4": False, "S5": False},
    "P3": {"S1": False, "S2": False, "S3": False, "S4": True,  "S5": True},
    "P4": {"S1": False, "S2": False, "S3": True,  "S4": False, "S5": True},
}

# =====================================================
# Products & Fluids (Emoji + Name)
# =====================================================
PRODUCTS = {
    "P1": "💨🔥⬇️  Gas | High Temp | Low Pressure",
    "P2": "💨❄️⬆️  Gas | Low Temp | High Pressure",
    "P3": "💧🔥⬇️  Water | High Temp | Low Pressure",
    "P4": "💧❄️⬆️  Water | Low Temp | High Pressure",
}

STATES = {
    "S1": "💨❄️⬆️  Gas | Low Temp | High Pressure",
    "S2": "💨🔥⬇️  Gas | High Temp | Low Pressure",
    "S3": "💧❄️⬆️  Water | Low Temp | High Pressure",
    "S4": "💧🔥⬇️  Water | High Temp | Low Pressure",
    "S5": "💧🌡️⚖️  Water | Normal",
}

PRODUCT_FLUID = {"P1": "gas", "P2": "gas", "P3": "water", "P4": "water"}
STATE_FLUID = {"S1": "gas", "S2": "gas", "S3": "water", "S4": "water", "S5": "water"}


# =====================================================
# Drag List (Bright Theme)
# =====================================================
class DragList(QListWidget):
    def __init__(self):
        super().__init__()
        self.setDragEnabled(True)
        self.setStyleSheet("""
            QListWidget {
                background-color: #ffffff;
                color: #000000;
                font-size: 15px;
                border: 1px solid #bdbdbd;
            }
            QListWidget::item:selected {
                background-color: #e0e0e0;
            }
        """)


class DropBox(QFrame):
    def __init__(self, title):
        super().__init__()
        self.setAcceptDrops(True)
        self.data = None

        self.setStyleSheet("""
            QFrame {
                background-color: #fafafa;
                border: 2px dashed #9e9e9e;
            }
        """)

        layout = QVBoxLayout()

        self.label = QLabel(title)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("""
            font-size:14px;
            font-weight:bold;
            color:#000000;
        """)
        layout.addWidget(self.label)

        self.value = QLabel("Drop here")
        self.value.setAlignment(Qt.AlignCenter)
        self.value.setStyleSheet("""
            font-size:18px;
            color:#666666;
        """)
        layout.addWidget(self.value)

        self.setLayout(layout)

    def dragEnterEvent(self, event):
        event.acceptProposedAction()

    def dropEvent(self, event):
        item = event.source().currentItem()
        self.data = item.data(Qt.UserRole)
        self.value.setText(item.text())
        self.parent().evaluate()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🧪 Flow Safety Trainer — Bright Mode")
        self.setGeometry(200, 200, 1050, 420)
        self.setStyleSheet("background-color:#f5f5f5;")
        self.init_ui()

    def init_ui(self):
        main = QVBoxLayout()

        title = QLabel("🧪 Flow Safety Drag & Drop Trainer")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            font-size:22px;
            font-weight:bold;
            color:#000000;
        """)
        main.addWidget(title)

        content = QHBoxLayout()

        # Fluid list
        fluid_list = DragList()
        for k, v in STATES.items():
            item = QListWidgetItem(v)
            item.setData(Qt.UserRole, k)
            fluid_list.addItem(item)

        # Product list
        product_list = DragList()
        for k, v in PRODUCTS.items():
            item = QListWidgetItem(v)
            item.setData(Qt.UserRole, k)
            product_list.addItem(item)

        # Drop areas
        self.drop_fluid = DropBox("🌊 FLUID")
        self.drop_product = DropBox("🧩 PRODUCT")

        self.result_box = QLabel("RESULT")
        self.result_box.setAlignment(Qt.AlignCenter)
        self.result_box.setStyleSheet("""
            QLabel {
                background-color:#ffffff;
                border:2px solid #9e9e9e;
                font-size:26px;
                font-weight:bold;
                color:#000000;
            }
        """)

        content.addWidget(fluid_list)
        content.addWidget(self.drop_fluid)
        content.addWidget(product_list)
        content.addWidget(self.drop_product)
        content.addWidget(self.result_box)

        main.addLayout(content)
        self.setLayout(main)

    def evaluate(self):
        if not self.drop_fluid.data or not self.drop_product.data:
            return

        p = self.drop_product.data
        s = self.drop_fluid.data

        if COMPATIBILITY[p][s]:
            self.result_box.setText("🟢 SAFE")
            self.result_box.setStyleSheet("color:#2e7d32; font-size:26px;")
        elif PRODUCT_FLUID[p] == STATE_FLUID[s]:
            self.result_box.setText("🔴 DANGER")
            self.result_box.setStyleSheet("color:#c62828; font-size:26px;")
        else:
            self.result_box.setText("⚫ INVALID")
            self.result_box.setStyleSheet("color:#616161; font-size:26px;")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
