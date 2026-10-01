export default function Dashboard({
  events = [],
  running = false,
  connectionStatus = "CONNECTING"
}) {
  const highRisk = events.filter(
    event => Number(event.risk_score || 0) >= 70
  ).length;

  const critical = events.filter(
    event => event.severity === "CRITICAL"
  ).length;

  return (
    <div className="page">

      <div className="page-heading">
        <div>
          <h2>Security Operations Dashboard</h2>
          <p>
            Real-time controlled cyber security simulation
          </p>
        </div>

        <div className="live-badge">
          <span />
          {running
            ? "SIMULATION ACTIVE"
            : "SYSTEM READY"}
        </div>
      </div>

      <div className="stats">

        <div className="stat-card">
          <h3>TOTAL EVENTS</h3>
          <strong>{events.length}</strong>
          <p>Current session</p>
        </div>

        <div className="stat-card">
          <h3>HIGH RISK</h3>
          <strong>{highRisk}</strong>
          <p>Risk ≥ 70</p>
        </div>

        <div className="stat-card">
          <h3>CRITICAL</h3>
          <strong>{critical}</strong>
          <p>Critical severity</p>
        </div>

        <div className="stat-card">
          <h3>AI-IDAPS</h3>
          <strong>
            {connectionStatus === "CONNECTED"
              ? "ONLINE"
              : "OFFLINE"}
          </strong>
          <p>Integration status</p>
        </div>

      </div>

      <div className="panel">
        <h3>AI Security Analysis</h3>
        <p>
          Waiting for security events from the simulation engine...
        </p>
      </div>

      <div className="panel">
        <h3>Recent Security Events</h3>

        {events.length === 0 ? (
          <p>No security events yet.</p>
        ) : (
          events.slice(0, 10).map((event, index) => (
            <div key={event.id || index}>
              {event.event_type} — {event.severity} — Risk{" "}
              {event.risk_score}
            </div>
          ))
        )}
      </div>

    </div>
  );
}