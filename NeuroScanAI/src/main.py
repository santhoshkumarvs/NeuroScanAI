from fastapi import FastAPI, Request
from src.anomaly_detection.detector import detect_anomalies
from src.utils.phi_masker import mask_phi
import logging

logging.basicConfig(filename="inference.log", level=logging.INFO, format="%(asctime)s - %(message)s")

app = FastAPI()

@app.post("/detect")
async def detect(request: Request):
    data = await request.json()
    masked = mask_phi(data.get("text", ""))
    result = detect_anomalies(data)
    logging.info(f"Inference: {masked} -> {result}")
    return {"masked_input": masked, "detection": result}
