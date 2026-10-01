from datetime import datetime
import random


def generate():

    return {
        "timestamp": datetime.utcnow().isoformat(),
        "event_type": "AUTHENTICATION_ABUSE",
        "severity": random.choice([
            "HIGH",
            "CRITICAL"
        ]),
        "source_ip": random.choice([
            "192.0.2.50",
            "192.0.2.70"
        ]),
        "target": "SIMULATED-IDENTITY-SERVICE",
        "mitre_technique": "T1078",
        "risk_score": random.randint(70, 97),
        "details": {
            "activity": "abnormal authentication pattern",
            "description": "Synthetic identity abuse event"
        }
    }