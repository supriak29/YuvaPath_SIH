from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "ai" / "data"


def load_career_pathway_data():
    return pd.read_csv(DATA_DIR / "career_pathway_dataset.csv")


def load_skill_outcome_data():
    return pd.read_csv(DATA_DIR / "skilloutcome_synthetic_dataset.csv")