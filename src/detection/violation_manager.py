import os
import cv2
from datetime import datetime


class ViolationManager:

    def __init__(self):
        self.violation_count = 0
        self.last_capture_time = None

        os.makedirs(
            "outputs/violations",
            exist_ok=True
        )

    def process(self, frame, detections):

        violation_found = False

        for detection in detections:

            label = detection["class_name"]

            if "without" in label.lower():
                violation_found = True
                break

        if violation_found:

            current_time = datetime.now()

            if (
                self.last_capture_time is None
                or
                (current_time - self.last_capture_time).seconds > 5
            ):

                self.violation_count += 1

                filename = current_time.strftime(
                    "%Y%m%d_%H%M%S.jpg"
                )

                filepath = os.path.join(
                    "outputs/violations",
                    filename
                )

                cv2.imwrite(
                    filepath,
                    frame
                )

                self.last_capture_time = current_time

                print(
                    f"[ALERT] Violation Saved: {filepath}"
                )

        return self.violation_count