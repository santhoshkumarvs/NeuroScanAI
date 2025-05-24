import random
def detect_anomalies(data):
    score = random.random()
    return {"anomaly": score > 0.7, "score": score}
