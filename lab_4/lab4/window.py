import sys
from PyQt5.QtWidgets import (QApplication, QInputDialog, QFileDialog, QMainWindow,
                             QMessageBox, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget)
from PyQt5.QtGui import QFont

import number_card_and_functions
import works_files as file


class CardSearchWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(550, 400)
        self.setWindowTitle('SEARCH OF BANK CARD')
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        # Set up the UI elements
        self.btn_bins = QLineEdit(placeholderText="Enter the list of bins")
        self.btn_hash_card = QLineEdit(placeholderText="Enter the hash")
        self.btn_last_number = QLineEdit(placeholderText="Enter the last 4 digits")

        self.hash_btn = QPushButton('Find the card number by hash')
        self.luhn_btn = QPushButton('Validate Card Number using Luhn')
        self.graph_btn = QPushButton('Generate Performance Graph')
        self.exit_btn = QPushButton('Exit')

        # Apply custom styles
        self.apply_styles()

        # Set up the layout
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        hbox.addWidget(self.btn_bins)
        hbox.addWidget(self.btn_hash_card)
        hbox.addWidget(self.btn_last_number)
        vbox.addLayout(hbox)

        vbox.addWidget(self.hash_btn)
        vbox.addWidget(self.luhn_btn)
        vbox.addWidget(self.graph_btn)
        vbox.addWidget(self.exit_btn)

        self.centralWidget.setLayout(vbox)

        self.hash_btn.clicked.connect(lambda: self.find_number())
        self.luhn_btn.clicked.connect(self.luna_alg)
        self.graph_btn.clicked.connect(lambda: self.plot_performance_graph())
        self.exit_btn.clicked.connect(lambda: self.close_application())

        self.show()

    def apply_styles(self):
        """
        Applies custom styles to the UI elements.
        """
        self.setStyleSheet("""
            background-color: #FFFFFF;
            color: #333333;
        """)

        font = QFont("Arial", 12)
        self.btn_bins.setFont(font)
        self.btn_hash_card.setFont(font)
        self.btn_last_number.setFont(font)

        self.hash_btn.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)

        self.luhn_btn.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #0b7dda;
            }
        """)

        self.graph_btn.setStyleSheet("""
            QPushButton {
                background-color: #FF9800;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #f57c00;
            }
        """)

        self.exit_btn.setStyleSheet("""
            QPushButton {
                background-color: #F44336;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #e53935;
            }
        """)

    def find_number(self) -> None:
        """
        Handles the logic to find the card number based on the provided hash value, BINs, and last digit.
        If a valid card number is found, it is saved to a file. If not, an error message is displayed.
        """
        bins = self.btn_bins.text().split(",")
        hash_card = self.btn_hash_card.text()
        last_number = self.btn_last_number.text()
        if not bins or not hash_card or not last_number:
            QMessageBox.information(
                None,
                "Missing Card Details",
                "Please fill in all the required card details.",
            )
            return
        try:
            last_number = int(last_number)
            bins = [int(item) for item in bins]
        except ValueError:
            QMessageBox.information(
                None,
                "Invalid input",
                "Please enter valid values for the last 4 digits and BINs",
            )
            return
        card_number = number_card_and_functions.find_card_number(hash_card, bins, last_number)
        if card_number:
            directory = QFileDialog.getSaveFileName(
                self, "Select the file to save the found number:", "", "JSON File(*.json)"
            )[0]
            if directory:
                file.write_files(directory, card_number)
                QMessageBox.information(
                    None, "Successful", f"The card number has been saved in the file: {directory}"
                )
        else:
            QMessageBox.information(
                None, "Card Number Not Found", "The card number was not found based on the provided information."
            )

    def luna_alg(self) -> None:
        """
        Handles the logic to check the validity of a card number using the Luhn algorithm.
        The user is prompted to enter a card number,
        and a message is displayed based on the result of the Luhn algorithm check.
        """
        card_number = QInputDialog.getText(
            self, "Enter the card number", "Card number:"
        )
        card_number = card_number[0]
        if card_number == "":
            QMessageBox.information(
                None, "Enter the card number", "The card number was not entered"
            )
        result = number_card_and_functions.validate_luhn(card_number)
        if result is not False:
            QMessageBox.information(
                None, "The result of the check", "The card number is valid"
            )
        else:
            QMessageBox.information(
                None, "The result of the check", "The card number is invalid"
            )

    def plot_performance_graph(self) -> None:
        """
        Handles the logic to generate a graph showing the execution time of the `find_card_number` function based
        on the number of processes used.
        The user is required to provide the necessary input parameters (hash, BINs, last digit).
        """
        bins = self.btn_bins.text().split(",")
        hash_card = self.btn_hash_card.text()
        last_digit = self.btn_last_number.text()
        if not bins or not hash_card or not last_digit:
            QMessageBox.information(
                None,
                "Missing Card Details",
                "Please fill in all the required card details.",
            )
            return
        try:
            last_digit = int(last_digit)
            bins = [int(item) for item in bins]
        except ValueError:
            QMessageBox.information(
                None,
                "Invalid input",
                "Please enter valid values for the last 4 digits and BINs",
            )
            return
        number_card_and_functions.plot_performance(hash_card, bins, last_digit)

    def close_application(self):
        """
        Handles the logic to close the application when the user clicks the "Exit" button.
        The user is prompted to confirm the exit action.
        """
        reply = QMessageBox.question(self, 'Confirm Exit', "Are you sure you want to quit?",
                                     QMessageBox.Yes | QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.accept()
        else:
            self.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CardSearchWindow()
    app.exec()
