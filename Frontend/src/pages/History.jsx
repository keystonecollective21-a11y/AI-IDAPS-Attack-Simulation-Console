export default function History({
  events
}) {

  return (
    <div className="page">

      <div className="page-heading">

        <div>

          <h2>
            Simulation History
          </h2>

          <p>
            Events recorded in the local
            simulation database
          </p>

        </div>

      </div>


      <div className="history-list">

        {events.map((event) => (

          <div
            className="history-item"
            key={event.id}
          >

            <div>

              <strong>
                {event.event_type}
              </strong>

              <span>
                {event.source_ip}
              </span>

            </div>

            <div>

              <span>
                Risk: {event.risk_score}
              </span>

              <span>
                {event.severity}
              </span>

            </div>

          </div>

        ))}

      </div>

    </div>
  );
}