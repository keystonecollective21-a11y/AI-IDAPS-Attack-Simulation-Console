import random


def generate():

    return {
        "event_type": "Brute Force",
        "severity": "HIGH",

        "source_ip": "192.0.2.30",
        "target": "192.0.2.10",

        "mitre_technique": "T1110",

        "risk_score": random.randint(80, 95),

        # ML features
        "source_port": random.randint(40000, 60000),
        "destination_port": 22,
        "protocol": "TCP",

        "duration": round(
            random.uniform(10, 35),
            2
        ),

        "packets": random.randint(
            60,
            220
        ),

        "bytes_transferred": random.randint(
            5000,
            30000
        ),

        "syn_count": random.randint(
            2,
            15
        ),

        "failed_connections": random.randint(
            30,
            100
        ),

        "details": {
            "description":
                "Controlled synthetic authentication failure pattern",

            "simulation": True,

            "authentication_failures":
                random.randint(30, 100)
        }
    }