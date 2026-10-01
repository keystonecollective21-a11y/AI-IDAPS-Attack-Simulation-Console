export default function Header({
  connectionStatus
}) {

  return (
    <header className="header">

      <div>

        <h1>
          AI-IDAPS
        </h1>

        <span>
          Attack Simulation Console
        </span>

      </div>

      <div className="connection">

        <span
          className={
            connectionStatus === "CONNECTED"
              ? "status-dot online"
              : "status-dot"
          }
        />

        {connectionStatus}

      </div>

    </header>
  );
}