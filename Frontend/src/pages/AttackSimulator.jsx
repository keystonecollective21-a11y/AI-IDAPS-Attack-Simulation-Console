import AttackCard from "../components/AttackCard";


export default function AttackSimulator({
  onStart,
  onStop,
  running
}) {

  const attacks = [
    {
      title: "Port Scan",
      type: "port_scan",
      description:
        "Simulates synthetic network reconnaissance activity."
    },
    {
      title: "Brute Force",
      type: "brute_force",
      description:
        "Generates controlled authentication failure events."
    },
    {
      title: "Traffic Anomaly",
      type: "traffic_anomaly",
      description:
        "Produces synthetic abnormal traffic patterns."
    },
    {
      title: "IOC Detection",
      type: "ioc",
      description:
        "Generates controlled synthetic indicators of compromise."
    },
    {
      title: "Authentication Abuse",
      type: "authentication_abuse",
      description:
        "Simulates abnormal identity activity."
    },
    {
        title: "DoS Simulation",
        type: "dos",
        description:
        "Generates controlled synthetic denial-of-service traffic patterns."
    },
  ];


  return (
    <div className="page">

      <div className="page-heading">

        <div>

          <h2>
            Attack Simulation Center
          </h2>

          <p>
            Controlled synthetic security
            event generation
          </p>

        </div>

        {running && (

          <button
            className="stop-button"
            onClick={onStop}
          >
            STOP SIMULATION
          </button>

        )}

      </div>


      <div className="attack-grid">

        {attacks.map((attack) => (

          <AttackCard
            key={attack.type}
            {...attack}
            onStart={onStart}
            running={running}
          />

        ))}

      </div>

    </div>
  );
}