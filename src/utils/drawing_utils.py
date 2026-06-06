import cv2


def draw_detections(frame, detections):

    for detection in detections:

        x1, y1, x2, y2 = detection["bbox"]
        confidence = detection["confidence"]
        label = detection["class_name"]

        status = "SAFE"

        if "without" in label.lower():
            status = "VIOLATION"
            color = (0, 0, 255)  # Red
        else:
            color = (0, 255, 0)  # Green

        # Bounding box
        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            color,
            2
        )

        # Status text
        cv2.putText(
            frame,
            status,
            (x1, y1 - 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            color,
            2
        )

        # Class + confidence
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