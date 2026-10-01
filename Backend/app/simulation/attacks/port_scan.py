from datetime import datetime
import random


def generate():

    ports = random.sample(
        [21, 22, 23, 25, 53, 80, 110, 443, 445, 3389],
        random.randint(3, 7)
    )

    return {
        "timestamp": datetime.utcnow().isoformat(),
        "event_type": "PORT_SCAN",
        "severity": random.choice(
            ["MEDIUM", "HIGH"]
        ),
        "source_ip": random.choice([
            "192.0.2.50",
            "192.0.2.60",
            "192.0.2.70"
        ]),
        "target": "SIMULATED-SERVER-01",
        "mitre_technique": "T1046",
        "risk_score": random.randint(60, 90),
        "details": {
            "ports_scanned": ports,
            "description": "Synthetic network reconnaissance event"
        }
    }