from fastapi import APIRouter
from app.config import settings, ScoringWeights

router = APIRouter(prefix="/config", tags=["Configuration"])


@router.get("/weights")
def get_scoring_weights():
    """
    Get current default scoring weights.
    """
    return {
        "raw_weights": settings.default_weights.model_dump(),
        "normalized_weights": settings.default_weights.normalized_dict(),
    }


@router.post("/weights")
def update_scoring_weights(new_weights: ScoringWeights):
    """
    Update default scoring weights configuration.
    """
    settings.default_weights = new_weights
    return {
        "message": "Scoring weights updated successfully",
        "raw_weights": settings.default_weights.model_dump(),
        "normalized_weights": settings.default_weights.normalized_dict(),
    }
