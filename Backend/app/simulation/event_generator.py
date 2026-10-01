import random

from app.simulation.attacks.port_scan import generate as port_scan
from app.simulation.attacks.brute_force import generate as brute_force
from app.simulation.attacks.traffic_anomaly import generate as traffic_anomaly
from app.simulation.attacks.ioc_simulation import generate as ioc
from app.simulation.attacks.authentication_abuse import generate as auth_abuse
from app.simulation.attacks.dos_simulation import generate as dos


GENERATORS = {
    "port_scan": port_scan,
    "brute_force": brute_force,
    "traffic_anomaly": traffic_anomaly,
    "ioc": ioc,
    "authentication_abuse": auth_abuse,
    "dos": dos,
}


def generate_event(attack_type: str):

    generator = GENERATORS.get(attack_type)

    if generator is None:
        raise ValueError(
            f"Unknown attack type: {attack_type}"
        )

    event = generator()

    # Make absolutely sure the selected
    # simulation type is preserved.
    attack_names = {
        "port_scan": "Port Scan",
        "brute_force": "Brute Force",
        "traffic_anomaly": "Traffic Anomaly",
        "ioc": "IOC Detection",
        "authentication_abuse": "Authentication Abuse",
        "dos": "DoS",
    }

    event["event_type"] = attack_names.get(
        attack_type,
        event.get("event_type", "Unknown")
    )

    event["simulation_attack_type"] = attack_type

    return event