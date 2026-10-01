export default function AttackCard({
  title,
  description,
  type,
  onStart,
  running
}) {

  return (
    <div className="attack-card">

      <div className="attack-icon">
        ⚡
      </div>

      <h3>
        {title}
      </h3>

      <p>
        {description}
      </p>

      <button
        disabled={running}
        onClick={() => onStart(type)}
      >
        {running ? "RUNNING..." : "START SIMULATION"}
      </button>

    </div>
  );
}