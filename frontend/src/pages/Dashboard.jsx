import { useEffect, useState } from "react";
import api from "../services/api";
import { StatCard } from "../components/StatCard";
import "./Dashboard.css";
import { TableCard } from "../components/TableCard";

function Dashboard() {
  const [stats, setStats] = useState(null);

  useEffect(() => {
    fetchStats();
  }, []);

  const fetchStats = async () => {
    try {
      const response = await api.get("/stats");

      setStats(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  if (!stats) {
    return <h2>Loading...</h2>;
  }

  return (
    <div className="dashboard-container">
      <div className="dashboard-header">
        <h1>Helmet Detection Monitoring System</h1>
        <p>Real-Time Traffic Safety & Violation Analytics</p>
      </div>

      <div className="stats-grid">
        <StatCard title="Total Violations" value={stats.total_violations} />

        <StatCard title="Today's Violations" value={stats.today_violations} />

        <StatCard title="Latest Violation" value={stats.latest_violation} />
      </div>
      <TableCard violations={stats.recent_violations} />
    </div>
  );
}

export default Dashboard;
