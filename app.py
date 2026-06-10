from flask import Flask, Response, render_template, request, jsonify
import pandas as pd
import os
import shutil
from datetime import datetime
import json
# import cv2
# import numpy as np
# import time
# from ultralytics import YOLO
app = Flask(__name__)

# from src.detection.helmet_detector import HelmetDetector
# from src.detection.violation_manager import ViolationManager

# from src.utils.drawing_utils import (
#     draw_detections,
#     draw_violation_count,
#     draw_alert_banner,
#     draw_timestamp
# )

# detector = HelmetDetector()
# violation_manager = ViolationManager()

# camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
camera = None

monitoring_active = True
ADMIN_PASSWORD = os.getenv(
    "ADMIN_PASSWORD",
    "helmsecure2026"
)
SHOW_ADMIN_CONTROLS = False  # Set to True to show admin controls on the dashboard  

VIOLATIONS_DIR = "outputs/violations"
STATIC_SCREENSHOTS_DIR = "static/screenshots"


@app.route("/")
def dashboard():
    total_violations = 0
    today_violations = 0
    latest_violation = "No Violations"
    recent_violations = []
    daily_violations = {
                "labels": [],
                "counts": []
            }
    
    try:

        df = pd.read_csv(
            "outputs/logs/violations.csv"
        )
        total_violations = len(df)

        if not df.empty:

            df["Date"] = pd.to_datetime(
                df["Timestamp"]
            ).dt.date

            daily_counts = (
                df.groupby("Date")
                .size()
                .reset_index(name="count")
            )
            daily_violations = {
                "labels": [
                    str(date)
                    for date in daily_counts["Date"]
                ],
                "counts": daily_counts["count"].tolist()
            }
            

            today = datetime.now().strftime("%Y-%m-%d")

            today_violations = len(
                df[
                    df["Timestamp"].astype(str).str.startswith(today)
                ]
            )

            if not df.empty:

                latest_violation = (
                    df.iloc[-1]["Timestamp"]
                )

                recent_violations = (
                    df.tail(10)
                    .iloc[::-1]
                    .to_dict("records")
                )

    except Exception as e:
        print(e)

    os.makedirs(
        STATIC_SCREENSHOTS_DIR,
        exist_ok=True
    )

    screenshots = []

    if os.path.exists(VIOLATIONS_DIR):

        for image in os.listdir(VIOLATIONS_DIR):

            source = os.path.join(
                VIOLATIONS_DIR,
                image
            )

            destination = os.path.join(
                STATIC_SCREENSHOTS_DIR,
                image
            )

            if not os.path.exists(destination):
                shutil.copy(
                    source,
                    destination
                )

            screenshots.append(image)

    screenshots = sorted( # Sort by creation time
        screenshots,
        key=lambda x: os.path.getctime(
            os.path.join(
                STATIC_SCREENSHOTS_DIR,
                x
            )
        ),
        reverse=True
    )
    system_status = (
        "LIVE"
        if monitoring_active
        else "STOPPED"
    )

    return render_template(
        "dashboard.html",
        total_violations=total_violations,
        today_violations=today_violations,
        latest_violation=latest_violation,
        recent_violations=recent_violations,
        screenshots=screenshots,
        system_status=system_status,
        show_admin_controls=SHOW_ADMIN_CONTROLS,
        chart_labels=json.dumps(
            daily_violations.get(
                "labels",
                []
            )
        ),
        chart_counts=json.dumps(
            daily_violations.get(
                "counts",
                []
            )
        )
    )
# def generate_frames():

#     global monitoring_active
#     prev_time = time.time()
#     while True:

#         if not monitoring_active:
#             blank = np.zeros(
#                 (480, 640, 3),
#                 dtype=np.uint8
#             )

#             cv2.putText(
#                 blank,
#                 "MONITORING STOPPED",
#                 (120, 240),
#                 cv2.FONT_HERSHEY_SIMPLEX,
#                 1,
#                 (0, 0, 255),
#                 2
#             )

#             ret, buffer = cv2.imencode(
#                 ".jpg",
#                 blank
#             )

#             frame_bytes = buffer.tobytes()

#             yield (
#                 b"--frame\r\n"
#                 b"Content-Type: image/jpeg\r\n\r\n"
#                 + frame_bytes +
#                 b"\r\n"
#             )

#             continue
#         if not camera.isOpened():
#             continue
#         success, frame = camera.read()

#         if not success:
#             break

#         detections = detector.detect(frame)

#         frame = draw_detections(
#             frame,
#             detections
#         )

#         count = violation_manager.process(
#             frame,
#             detections
#         )

#         frame = draw_violation_count(
#             frame,
#             count
#         )

#         if violation_manager.has_violation(
#             detections
#         ):

#             frame = draw_alert_banner(
#                 frame
#             )

#         frame = draw_timestamp(
#             frame
#         )
#         current_time = time.time()

#         fps = 1 / (
#             current_time -
#             prev_time
#         )

#         prev_time = current_time

#         cv2.putText(
#             frame,
#             f"FPS: {int(fps)}",
#             (20, 80),
#             cv2.FONT_HERSHEY_SIMPLEX,
#             0.8,
#             (255, 255, 255),
#             2
#         )
#         ret, buffer = cv2.imencode(
#             ".jpg",
#             frame
#         )

#         frame_bytes = buffer.tobytes()

#         yield (
#             b"--frame\r\n"
#             b"Content-Type: image/jpeg\r\n\r\n"
#             + frame_bytes +
#             b"\r\n"
#         )
@app.route("/video_feed")
def video_feed():

    # return Response(
    #     generate_frames(),
    #     mimetype=
    #     "multipart/x-mixed-replace; boundary=frame"
    # )
    return "Camera feed Disabled For Cloud Deployment"
@app.route("/stop_monitoring", methods=["POST"])
def stop_monitoring():

    global monitoring_active

    password = request.form.get("password")

    if password != ADMIN_PASSWORD:

        return jsonify({
            "success": False,
            "message": "Invalid Password"
        })

    monitoring_active = False
    if camera:
        camera.release()
    return jsonify({
        "success": True,
        "message": "Monitoring Stopped"
    })
    
@app.route("/camera-test")
def camera_test():
    return render_template(
        "camera_test.html"
    )
if __name__ == "__main__":
    app.run(debug=False, threaded=True)