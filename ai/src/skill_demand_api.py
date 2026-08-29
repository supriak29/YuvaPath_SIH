# ============================================================
# FASTAPI — SKILL DEMAND PREDICTION
# ============================================================

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from ai.src.skill_demand_predictor import predict_skill_demand


app = FastAPI(
    title="SIH Skill Demand AI",
    version="1.0.0"
)


# ------------------------------------------------------------
# Request schema
# ------------------------------------------------------------

class SkillDemandRequest(BaseModel):

    district: str
    desired_career: str
    recommended_course: str
    job_required_skills: str
    readiness_pct: float
    skill_gap_count: float
    plfs_employment_rate_pct: float


# ------------------------------------------------------------
# Prediction endpoint
# ------------------------------------------------------------

@app.post("/predict/skill-demand")
def skill_demand_prediction(
    request: SkillDemandRequest
):

    try:

        prediction = predict_skill_demand(
            request.model_dump()
        )

        return {
            "predicted_nearby_openings": prediction
        }

    except Exception as exc:

        raise HTTPException(
            status_code=400,
            detail=str(exc)
        )
