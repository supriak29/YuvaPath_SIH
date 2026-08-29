from pathlib import Path
from .data_loader import (
    load_career_pathway_data,
    load_skill_outcome_data
)

PROJECT_ROOT = Path(__file__).resolve().parents[2]
PROCESSED_DIR = PROJECT_ROOT / "ai" / "processed"


def save_processed_data():
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    career_df = load_career_pathway_data()
    outcome_df = load_skill_outcome_data()

    career_df.to_csv(
        PROCESSED_DIR / "career_pathway_processed.csv",
        index=False
    )

    outcome_df.to_csv(
        PROCESSED_DIR / "skilloutcome_processed.csv",
        index=False
    )


if __name__ == "__main__":
    save_processed_data()
    print("Processed datasets saved successfully.")