from datetime import datetime
import random


def generate():

    return {
        "timestamp": datetime.utcnow().isoformat(),
        "event_type": "TRAFFIC_ANOMALY",
        "severity": random.choice(
            ["MEDIUM", "HIGH", "CRITICAL"]
        ),
        "source_ip": random.choice([
            "192.0.2.50",
            "192.0.2.60",
            "192.0.2.70",
            "192.0.2.80"
        ]),
        "target": "SIMULATED-NETWORK",
        "mitre_technique": "T1498",
        "risk_score": random.randint(55, 95),
        "details": {
            "traffic_rate": random.randint(500, 5000),
            "baseline_rate": 300,
            "description": "Synthetic abnormal traffic pattern"
        }
    }