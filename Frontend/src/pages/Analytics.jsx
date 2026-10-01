import {
  BarChart,
  Bar,
  CartesianGrid,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer
} from "recharts";


export default function Analytics({
  events
}) {

  const counts = {};

  events.forEach((event) => {

    counts[event.event_type] =
      (counts[event.event_type] || 0) + 1;

  });


  const data = Object.entries(
    counts
  ).map(([name, count]) => ({
    name,
    count
  }));


  return (
    <div className="page">

      <div className="page-heading">

        <div>

          <h2>
            Security Analytics
          </h2>

          <p>
            Simulation event analysis
          </p>

        </div>

      </div>


      <div className="chart-card">

        <h3>
          Attack Distribution
        </h3>

        <ResponsiveContainer
          width="100%"
          height={400}
        >

          <BarChart data={data}>

            <CartesianGrid
              strokeDasharray="3 3"
            />

            <XAxis dataKey="name" />

            <YAxis />

            <Tooltip />

            <Bar
              dataKey="count"
            />

          </BarChart>

        </ResponsiveContainer>

      </div>

    </div>
  );
}