from flask import Blueprint, Response, request, jsonify

import os

from services.camera_service import generate_frames, stop_camera_monitoring

monitoring_bp = Blueprint("monitoring", __name__)

ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "helmsecure2026")


@monitoring_bp.route("/api/video_feed")
def video_feed():

    return Response(
        generate_frames(), mimetype="multipart/x-mixed-replace; boundary=frame"
    )


@monitoring_bp.route("/api/monitoring/stop", methods=["POST"])
def stop_monitoring():

    password = request.form.get("password")

    if password != ADMIN_PASSWORD:

        return jsonify({"success": False, "message": "Invalid Password"})

    stop_camera_monitoring()

    return jsonify({"success": True, "message": "Monitoring Stopped"})
