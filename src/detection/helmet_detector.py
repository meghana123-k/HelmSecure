from ultralytics import YOLO


class HelmetDetector:

    def __init__(self):
        self.model = YOLO("models/helmet_detector.pt")

    def detect(self, frame):

        results = self.model(frame, conf=0.5)

        detections = []

        for result in results:

            for box in result.boxes:

                x1, y1, x2, y2 = map(
                    int,
                    box.xyxy[0]
                )

                confidence = float(box.conf[0])

                class_id = int(box.cls[0])

                class_name = self.model.names[class_id]

                detections.append({
                    "bbox": (x1, y1, x2, y2),
                    "confidence": confidence,
                    "class_name": class_name
                })

        return detections