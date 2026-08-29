# ============================================================
# PRODUCTION SKILL-DEMAND PREDICTOR
# ============================================================

from pathlib import Path
import joblib
import pandas as pd


# ------------------------------------------------------------
# Model path
# ------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[1]

MODEL_PATH = (
    BASE_DIR
    / "models"
    / "skill_demand_model.joblib"
)


# ------------------------------------------------------------
# Load model ONCE
# ------------------------------------------------------------

model = joblib.load(MODEL_PATH)


# ------------------------------------------------------------
# Required API features
# ------------------------------------------------------------

REQUIRED_FEATURES = [
    "district",
    "desired_career",
    "recommended_course",
    "job_required_skills",
    "readiness_pct",
    "skill_gap_count",
    "plfs_employment_rate_pct",
]


# ------------------------------------------------------------
# Prediction function
# ------------------------------------------------------------

def predict_skill_demand(data: dict) -> float:

    missing = [
        feature
        for feature in REQUIRED_FEATURES
        if feature not in data
    ]

    if missing:
        raise ValueError(
            f"Missing required fields: {missing}"
        )

    input_df = pd.DataFrame(
        [data],
        columns=REQUIRED_FEATURES
    )

    prediction = model.predict(
        input_df
    )[0]

    return round(
        float(prediction),
        2
    )


# ------------------------------------------------------------
# Example local test
# ------------------------------------------------------------

if __name__ == "__main__":

    sample = {
        "district": "Nanded",
        "desired_career": "Electrician",
        "recommended_course": "Electrician - Domestic & Industrial",
        "job_required_skills": (
            "Basic wiring; Circuit testing; "
            "Tool handling; Safety protocols"
        ),
        "readiness_pct": 25.0,
        "skill_gap_count": 3,
        "plfs_employment_rate_pct": 48.44,
    }

    result = predict_skill_demand(sample)

    print("Predicted nearby openings:", result)
    