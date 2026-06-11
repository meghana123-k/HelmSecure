import { NavLink } from "react-router-dom";
import "./Navbar.css";

export function Navbar() {
  return (
    <nav className="navbar">
      <div className="navbar-brand">HelmSecure</div>

      <div className="navbar-links">
        <NavLink to="/">Dashboard</NavLink>
        <NavLink to="/analytics">Analytics</NavLink>
        <NavLink to="/evidence">Evidence</NavLink>
        <NavLink to="/live-monitoring">Live Monitoring</NavLink>
      </div>
    </nav>
  );
}
