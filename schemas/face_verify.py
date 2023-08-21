from pydantic import BaseModel


class FaceVerifyResponse(BaseModel):
    verified: bool
    distance: float
    threshold: float
    model: str
    detector_backend: str
    similarity_metric: str
    facial_areas: dict
        