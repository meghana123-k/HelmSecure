import cv2

from detection.helmet_detector import HelmetDetector
from utils.drawing_utils import draw_detections, draw_violation_count
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