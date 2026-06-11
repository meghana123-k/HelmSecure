from datetime import datetime

from database.mongo import violations_collection


def save_violation(violation_type, image_path, confidence=None):

    violations_collection.insert_one(
        {
            "timestamp": datetime.now(),
            "violation_type": violation_type,
            "image_path": image_path,
            "confidence": confidence,
            "status": "Recorded",
        }
    )
