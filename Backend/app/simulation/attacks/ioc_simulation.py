from datetime import datetime
import random


def generate():

    return {
        "timestamp": datetime.utcnow().isoformat(),
        "event_type": "IOC_DETECTED",
        "severity": "HIGH",
        "source_ip": random.choice([
            "192.0.2.50",
            "192.0.2.60",
            "192.0.2.70"
        ]),
        "target": "SIMULATED-ENDPOINT",
        "mitre_technique": "T1071",
        "risk_score": random.randint(70, 95),
        "details": {
            "ioc_type": "synthetic_indicator",
            "indicator": "SIM-IOC-001",
            "description": "Synthetic indicator of compromise"
        }
    }