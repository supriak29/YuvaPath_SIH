import numpy as np
import pandas as pd
from pathlib import Path

from .data_loader import load_skill_outcome_data


PROJECT_ROOT = Path(__file__).resolve().parents[2]
PROCESSED_DIR = PROJECT_ROOT / "ai" / "processed"


def create_ml_dataset():
    df = load_skill_outcome_data().copy()

    rng = np.random.default_rng(42)

    # ---------------------------------------------------------
    # Pre-placement features
    # ---------------------------------------------------------

    df["attendance_percentage"] = np.where(
        df["completed_training"],
        rng.normal(82, 9, len(df)),
        rng.normal(62, 12, len(df))
    ).clip(30, 100).round(1)

    df["assessment_score"] = np.where(
        df["completed_training"],
        rng.normal(72, 12, len(df)),
        rng.normal(48, 15, len(df))
    ).clip(0, 100).round(1)

    df["certification_status"] = np.where(
        df["completed_training"],
        "certified",
        "not_certified"
    )

    df["previous_employment_status"] = rng.choice(
        ["never_employed", "previously_employed"],
        size=len(df),
        p=[0.65, 0.35]
    )

    # Skill-related development feature
    df["skill_match"] = (
        0.35 * (df["attendance_percentage"] / 100)
        + 0.40 * (df["assessment_score"] / 100)
        + 0.15 * df["completed_training"].astype(int)
        + 0.10 * (
            df["previous_employment_status"] == "previously_employed"
        ).astype(int)
    )

    # Add small noise so the relationship isn't deterministic
    df["skill_match"] += rng.normal(0, 0.05, len(df))
    df["skill_match"] = df["skill_match"].clip(0, 1).round(3)

    # Desired job role from observed job role where available,
    # otherwise use the course/trade as a development proxy.
    df["desired_job_roles"] = df["job_role"].fillna(df["course_trade"])

    # Placement target
    df["placed"] = (
        df["outcome_path"] == "formal_employment"
    ).astype(int)

    # Keep only model-development fields
    ml_columns = [
        "outcome_id",
        "district",
        "course_trade",
        "training_provider",
        "gender",
        "age",
        "attendance_percentage",
        "assessment_score",
        "certification_status",
        "existing_skills",
        "desired_job_roles",
        "skill_match",
        "previous_employment_status",
        "placed"
    ]

    # Existing skills are not available in the outcome dataset.
    # Keep the field for the contract, but mark it as unknown
    # rather than inventing trainee skill lists.
    df["existing_skills"] = "unknown"

    ml_df = df[ml_columns].copy()

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    output_path = PROCESSED_DIR / "placement_ml_dataset.csv"
    ml_df.to_csv(output_path, index=False)

    print("ML dataset created successfully.")
    print("Shape:", ml_df.shape)
    print("Saved to:", output_path)


if __name__ == "__main__":
    create_ml_dataset()