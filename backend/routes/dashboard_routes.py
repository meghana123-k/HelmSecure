# dashboard_routes.py

import os
import shutil

from flask import Blueprint, app, jsonify, request
import pandas as pd
from datetime import datetime

VIOLATIONS_DIR = "outputs/violations"
STATIC_SCREENSHOTS_DIR = "static/screenshots"


dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/api/stats")
def get_stats():
    total_violations = 0
    today_violations = 0
    latest_violation = "No Violations"
    recent_violations = []
    daily_violations = {"labels": [], "counts": []}

    try:

        df = pd.read_csv("outputs/logs/violations.csv")
        total_violations = len(df)

        if not df.empty:

            df["Date"] = pd.to_datetime(df["Timestamp"]).dt.date

            daily_counts = df.groupby("Date").size().reset_index(name="count")
            daily_violations = {
                "labels": [str(date) for date in daily_counts["Date"]],
                "counts": daily_counts["count"].tolist(),
            }

            today = datetime.now().date()

            today_violations = len(
                df[df["Date"] == today]
            )

            if not df.empty:
                df["Timestamp"] = pd.to_datetime(df["Timestamp"])

                latest_violation = df["Timestamp"].max().strftime("%Y-%m-%d %H:%M:%S")

                recent_violations = df.tail(10).iloc[::-1].to_dict("records")

    except Exception as e:
        print(f"Error reading violation logs: {e}")

    return jsonify(
        {
            "total_violations": total_violations,
            "today_violations": today_violations,
            "latest_violation": latest_violation,
            "recent_violations": recent_violations,
            "daily_violations": daily_violations,
        }
    )

@dashboard_bp.route("/api/evidence")
def get_evidence():

    evidence = []

    os.makedirs(STATIC_SCREENSHOTS_DIR, exist_ok=True)

    if os.path.exists(VIOLATIONS_DIR):

        for image in os.listdir(VIOLATIONS_DIR):

            source = os.path.join(VIOLATIONS_DIR, image)

            destination = os.path.join(STATIC_SCREENSHOTS_DIR, image)

            if not os.path.exists(destination):
                shutil.copy(source, destination)

            evidence.append(
                {
                    "filename": image,
                    "image_url": f"http://127.0.0.1:5000/static/screenshots/{image}",
                }
            )

    evidence.sort(
        key=lambda x: os.path.getctime(
            os.path.join(STATIC_SCREENSHOTS_DIR, x["filename"])
        ),
        reverse=True,
    )

    return jsonify(evidence)
