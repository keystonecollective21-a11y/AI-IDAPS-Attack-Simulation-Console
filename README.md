# AI-IDAPS Cyber Attack Simulation Console

A separate Windows desktop test application for the AI-IDAPS academic project.

## What it does

This application creates **synthetic network-flow telemetry** representing:
- DoS / SYN Flood (simulated)
- Port Scan (simulated)
- Brute Force (simulated)
- Normal Traffic

It sends the synthetic records to:

`http://localhost:8000/api/predict`

The AI-IDAPS backend classifies the telemetry and writes the event to its SQLite audit database. The AI-IDAPS dashboard can then display the event and its notification.

## Safety

This application does NOT generate packets, scan systems, attempt logins, contact external hosts, or perform an actual cyber attack. It is designed for an authorized academic/lab demonstration.

## Run on Windows

1. Start AI-IDAPS backend first:

```powershell
cd F:\AI-IDAPS-Professional\backend
.\.venv\Scripts\Activate.ps1
uvicorn app.main:app --reload --port 8000
```

2. In a second terminal, run this simulator:

```powershell
cd F:\AI-IDAPS-Attack-Simulation-Console\simulator
python attack_simulator.py
```

No additional Python package is required; it uses Python's built-in Tkinter and urllib.

3. Select a scenario and click **SEND SIMULATED EVENT**.

4. Open the AI-IDAPS dashboard:

`http://localhost:5173`

5. Click the bell icon to see the new security notification.

## Burst test

`BURST x10` sends ten synthetic events to the local AI-IDAPS API so you can demonstrate the dashboard updating with multiple events.
