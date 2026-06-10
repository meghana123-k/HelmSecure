# src/detection/person_detector.py
from ultralytics import YOLO


class PersonDetector:
    def __init__(self):
        self.model = YOLO("yolov8n.pt")

    def detect(self, frame):
        results = self.model(frame)

        detections = []

        for result in results:
            for box in result.boxes:

                class_id = int(box.cls[0])
                confidence = float(box.conf[0])

                # COCO class 0 = person
                if class_id == 0 and confidence > 0.5:

                    x1, y1, x2, y2 = map(
                        int,
                        box.xyxy[0]
                    )

                    detections.append({
                        "bbox": (x1, y1, x2, y2),
                        "confidence": confidence
                    })

        return detections