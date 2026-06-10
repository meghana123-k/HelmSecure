import cv2
import time
import numpy as np

from src.detection.violation_manager import ViolationManager
from src.detection.helmet_detector import HelmetDetector
from src.utils.drawing_utils import (
    draw_alert_banner,
    draw_detections,
    draw_timestamp,
    draw_violation_count,
)

detector = HelmetDetector()
violation_manager = ViolationManager()
camera = None

def get_camera():
    global camera

    if camera is None or not camera.isOpened():

        camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    return camera


camera = get_camera()

monitoring_active = True


def stop_camera_monitoring():
    global monitoring_active

    monitoring_active = False

    if camera.isOpened():
        camera.release()


def generate_frames():
    global monitoring_active

    prev_time = time.time()

    while True:

        if not monitoring_active:

            blank = np.zeros((480, 640, 3), dtype=np.uint8)

            cv2.putText(
                blank,
                "MONITORING STOPPED",
                (120, 240),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                2,
            )

            ret, buffer = cv2.imencode(".jpg", blank)

            frame_bytes = buffer.tobytes()

            yield (
                b"--frame\r\n"
                b"Content-Type: image/jpeg\r\n\r\n" + frame_bytes + b"\r\n"
            )

            continue

        if not camera.isOpened():
            continue

        success, frame = camera.read()

        if not success:
            break

        detections = detector.detect(frame)

        frame = draw_detections(frame, detections)

        count = violation_manager.process(frame, detections)

        frame = draw_violation_count(frame, count)

        if violation_manager.has_violation(detections):
            frame = draw_alert_banner(frame)

        frame = draw_timestamp(frame)

        current_time = time.time()

        fps = 1 / max(current_time - prev_time, 0.0001)

        prev_time = current_time

        cv2.putText(
            frame,
            f"FPS: {int(fps)}",
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 255),
            2,
        )

        ret, buffer = cv2.imencode(".jpg", frame)

        frame_bytes = buffer.tobytes()

        yield (
            b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame_bytes + b"\r\n"
        )
