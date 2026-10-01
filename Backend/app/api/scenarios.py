from fastapi import APIRouter

router = APIRouter(
    prefix="/api/scenarios",
    tags=["Scenarios"]
)


@router.get("")
def scenarios():

    return {
        "scenarios": [
            {
                "id": "reconnaissance",
                "name": "Enterprise Reconnaissance",
                "attacks": [
                    "port_scan"
                ]
            },
            {
                "id": "authentication",
                "name": "Authentication Attack",
                "attacks": [
                    "brute_force",
                    "authentication_abuse"
                ]
            },
            {
                "id": "network_anomaly",
                "name": "Network Anomaly",
                "attacks": [
                    "traffic_anomaly"
                ]
            }
        ]
    }