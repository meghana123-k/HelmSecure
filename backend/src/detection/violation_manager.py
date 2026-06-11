# src/detection/violation_manager.py

import os
import cv2
from datetime import datetime
from .violation_logger import ViolationLogger
from services.violation_db_service import save_violation

class ViolationManager:

    def __init__(self):

        self.violation_count = 0
        self.last_capture_time = None
        self.logger = ViolationLogger()

        os.makedirs(
            "outputs/violations",
            exist_ok=True
        )

    def process(self, frame, detections):

        violation_label = None

        for detection in detections:

            label = detection["class_name"]
            confidence = detection['confidence']
            if "without" in label.lower():
                violation_label = label
                break

        if violation_label:

            current_time = datetime.now()

            if (
                self.last_capture_time is None
                or
                (current_time - self.last_capture_time).seconds > 5
            ):

                self.violation_count += 1
                safe_label = violation_label.replace(" ", "_")

                filename = current_time.strftime(
                    f"%Y%m%d_%H%M%S_{safe_label}.jpg"
                )

                filepath = os.path.join(
                    "outputs/violations",
                    filename
                )

                cv2.imwrite(
                    filepath,
                    frame
                )

                self.logger.log_violation(
                    violation_label
                )
                save_violation(violation_type=violation_label, image_path=filepath.replace("\\", "/"), confidence=confidence)

                self.last_capture_time = current_time

                print(
                    f"[ALERT] Violation Saved: {filepath}"
                )

        return self.violation_count

    def has_violation(self, detections):

        for detection in detections:

            label = detection["class_name"]

            if "without" in label.lower():
                return True

        return False
