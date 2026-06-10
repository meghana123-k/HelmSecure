# dashboard_routes.py

from flask import Blueprint, jsonify, request
import pandas as pd
from datetime import datetime

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

            today = datetime.now().strftime("%Y-%m-%d")

            today_violations = len(
                df[df["Timestamp"].astype(str).str.startswith(today)]
            )

            if not df.empty:

                latest_violation = df.iloc[-1]["Timestamp"]

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
