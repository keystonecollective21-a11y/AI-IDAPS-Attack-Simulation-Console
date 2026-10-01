import random


def generate():

    return {
        "event_type": "DoS",
        "severity": "CRITICAL",

        "source_ip": "192.0.2.42",
        "target": "192.0.2.10",

        "mitre_technique": "T1498",

        "risk_score": random.randint(90, 99),

        # ML features
        "source_port": random.randint(40000, 60000),

        "destination_port": random.choice([
            80,
            443
        ]),

        "protocol": "TCP",

        "duration": round(
            random.uniform(0.2, 3.0),
            2
        ),

        "packets": random.randint(
            700,
            1600
        ),

        "bytes_transferred": random.randint(
            60000,
            180000
        ),

        "syn_count": random.randint(
            500,
            1400
        ),

        "failed_connections": random.randint(
            5,
            35
        ),

        "details": {
            "description":
                "Controlled synthetic denial-of-service traffic pattern",

            "simulation": True,

            "traffic_pattern":
                "High-volume synthetic TCP traffic"
        }
    }