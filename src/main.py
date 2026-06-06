import cv2
import time

from detection.helmet_detector import HelmetDetector
from utils.drawing_utils import draw_detections, draw_violation_count, draw_alert_banner, draw_timestamp
from detection.violation_manager import ViolationManager

def main():

    detector = HelmetDetector()
    violation_manager = ViolationManager()
    cap = cv2.VideoCapture(0)

    while True:

        success, frame = cap.read()

        if not success:
            break

        detections = detector.detect(frame)

        frame = draw_detections(
            frame,
            detections
        )
        count = violation_manager.process(
            frame,
            detections
        )
        frame = draw_violation_count(
            frame,
            count
        )
        has_violation = violation_manager.has_violation(
            detections
        )
        if has_violation:
            frame = draw_alert_banner(frame)
        frame = draw_timestamp(frame)
        prev_time = 0
        current_time = time.time()
        
        fps = 1 / (current_time - prev_time)
        prev_time = current_time
        cv2.putText(
            frame,
            f"FPS: {int(fps)}",
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 255),
            2
        )
        cv2.imshow(
            "Helmet Safety Monitoring",
            frame
        )

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()