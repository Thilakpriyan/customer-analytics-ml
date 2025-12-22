from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np

app = FastAPI()

class ChurnRequest(BaseModel):
    features: list

@app.post("/predict/churn")
def predict_churn(req: ChurnRequest):

    features = np.array(req.features)

    # mock response returned properly
    return {
        "prediction": 1,
        "probability": 0.82
    }
