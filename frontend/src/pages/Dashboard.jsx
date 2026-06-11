// src/pages/Dashboard.jsx

import { useEffect, useState } from "react";
import {getDashboardStats} from "../services/dashboardService";
import { StatCard } from "../components/StatCard";
import "./Dashboard.css";
import { TableCard } from "../components/TableCard";

function Dashboard() {
  const [stats, setStats] = useState(null);

  useEffect(() => {
    const fetchStats = async () => {
      try {
        const stats = await getDashboardStats();

        setStats(stats);
      } catch (error) {
        console.error(error);
      }
    };

    fetchStats();
  }, []);

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
