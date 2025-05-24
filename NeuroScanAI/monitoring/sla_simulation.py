import time, random
while True:
    latency = random.uniform(0.1, 1.5)
    print(f"Simulated latency: {latency}")
    if latency > 1.2:
        print("ALERT: SLA breach! Latency exceeds threshold.")
    time.sleep(5)
