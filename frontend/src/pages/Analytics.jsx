// src/pages/Analytics.jsx

import { useEffect, useState } from "react";
import { getDashboardStats } from "../services/dashboardService";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

import "./Analytics.css";

function Analytics() {
  const [chartData, setChartData] = useState([]);

  useEffect(() => {
    const fetchAnalytics = async () => {
      try {
        const stats = await getDashboardStats();
        console.log("Analytics API Response:", stats);
        const labels = stats.daily_violations.labels;
        const counts = stats.daily_violations.counts;

        const formattedData = labels.map((date, index) => ({
          date,
          violations: counts[index],
        }));

        setChartData(formattedData);
      } catch (error) {
        console.error(error);
      }
    };

    fetchAnalytics();
  }, []);

  return (
    <div className="analytics-container">
      <div className="chart-card">
        <div className="chart-header">
          <h2>Daily Helmet Violations</h2>
          <p>Recorded violations by date</p>
        </div>

        <ResponsiveContainer width="100%" height={400}>
          <BarChart data={chartData}>
            <CartesianGrid strokeDasharray="3 3" />

            <XAxis
              dataKey="date"
              label={{
                value: "Date",
                position: "insideBottom",
                offset: -5,
              }}
            />

            <YAxis
              label={{
                value: "Violations",
                angle: -90,
                position: "insideLeft",
              }}
            />

            <Tooltip />

            <Bar dataKey="violations" fill="#2f4f6f" radius={[4, 4, 0, 0]} />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}

export default Analytics;
