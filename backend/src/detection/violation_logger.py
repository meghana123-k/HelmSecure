# src/detection/violation_logger.py

import csv
import os
from datetime import datetime


class ViolationLogger:

    def __init__(self):

        self.log_file = "outputs/logs/violations.csv"

        os.makedirs(
            "outputs/logs",
            exist_ok=True
        )

        if not os.path.exists(self.log_file):

            with open(
                self.log_file,
                "w",
                newline=""
            ) as file:

                writer = csv.writer(file)

                writer.writerow([
                    "Timestamp",
                    "Violation_Type"
                ])

    def log_violation(self, violation_type):

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        with open(
            self.log_file,
            "a",
            newline=""
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                timestamp,
                violation_type
            ])