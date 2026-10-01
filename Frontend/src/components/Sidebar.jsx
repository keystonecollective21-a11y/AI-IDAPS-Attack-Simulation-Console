import {
  LayoutDashboard,
  ShieldAlert,
  BarChart3,
  History,
  Circle
} from "lucide-react";


export default function Sidebar({
  page,
  setPage
}) {

  const menuItems = [
    {
      id: "dashboard",
      label: "Dashboard",
      icon: LayoutDashboard
    },
    {
      id: "simulator",
      label: "Attack Simulator",
      icon: ShieldAlert
    },
    {
      id: "analytics",
      label: "Analytics",
      icon: BarChart3
    },
    {
      id: "history",
      label: "History",
      icon: History
    }
  ];


  return (
    <aside className="sidebar">

      <div className="sidebar-brand">

        <div className="brand-icon">
          <ShieldAlert size={24} />
        </div>

        <div>
          <h2>AI-IDAPS</h2>
          <span>Security Console</span>
        </div>

      </div>


      <nav className="sidebar-nav">

        {menuItems.map((item) => {

          const Icon = item.icon;

          return (
            <button
              key={item.id}
              type="button"
              className={
                page === item.id
                  ? "nav-item active"
                  : "nav-item"
              }
              onClick={() => {
                setPage(item.id);
              }}
            >

              <Icon size={19} />

              <span>
                {item.label}
              </span>

            </button>
          );

        })}

      </nav>


      <div className="sidebar-footer">

        <div className="system-status">

          <Circle
            size={9}
            fill="currentColor"
          />

          <span>
            Simulation Console
          </span>

        </div>

        <small>
          v2.0.0
        </small>

      </div>

    </aside>
  );
}