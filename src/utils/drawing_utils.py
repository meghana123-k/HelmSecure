import cv2
from datetime import datetime


def draw_detections(frame, detections):

    for detection in detections:

        x1, y1, x2, y2 = detection["bbox"]
        confidence = detection["confidence"]
        label = detection["class_name"]

        if "without" in label.lower():
            status = "VIOLATION"
            color = (0, 0, 255)
        else:
            status = "SAFE"
            color = (0, 255, 0)

        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            color,
            2
        )

        cv2.putText(
            frame,
            status,
            (x1, y1 - 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            color,
            2
        )

        cv2.putText(
            frame,
            f"{label} {confidence:.2f}",
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            color,
            2
        )

    return frame


def draw_violation_count(frame, count):

    cv2.putText(
        frame,
        f"Violations: {count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
    )

    return frame


def draw_alert_banner(frame):

    cv2.rectangle(
        frame,
        (0, 0),
        (frame.shape[1], 60),
        (0, 0, 255),
        -1
    )

    cv2.putText(
        frame,
        "VIOLATION DETECTED",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        2
    )

    return frame


def draw_timestamp(frame):

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    cv2.putText(
        frame,
        timestamp,
        (20, frame.shape[0] - 20),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2
    )

    return frame