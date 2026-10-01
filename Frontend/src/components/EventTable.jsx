export default function EventTable({
  events
}) {

  return (
    <div className="table-container">

      <div className="section-title">
        LIVE SECURITY EVENTS
      </div>

      <table>

        <thead>

          <tr>
            <th>Time</th>
            <th>Event</th>
            <th>Severity</th>
            <th>Source</th>
            <th>Target</th>
            <th>MITRE</th>
            <th>Risk</th>
          </tr>

        </thead>

        <tbody>

          {events.map((event, index) => (

            <tr key={
              event.id ||
              `${event.timestamp}-${index}`
            }>

              <td>
                {new Date(
                  event.timestamp
                ).toLocaleTimeString()}
              </td>

              <td>
                {event.event_type}
              </td>

              <td>

                <span
                  className={
                    `severity ${event.severity?.toLowerCase()}`
                  }
                >
                  {event.severity}
                </span>

              </td>

              <td>
                {event.source_ip}
              </td>

              <td>
                {event.target}
              </td>

              <td>
                {event.mitre_technique}
              </td>

              <td>
                {event.risk_score}
              </td>

            </tr>

          ))}

        </tbody>

      </table>

    </div>
  );
}