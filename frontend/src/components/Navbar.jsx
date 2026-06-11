import { NavLink } from "react-router-dom";
import "./Navbar.css";

export function Navbar() {
  return (
    <nav className="navbar">
      <div className="navbar-brand">HelmSecure</div>

      <div className="navbar-links">
        <NavLink to="/">Live Monitoring</NavLink>
        <NavLink to="/dashboard">Dashboard</NavLink>
        <NavLink to="/analytics">Analytics</NavLink>
        <NavLink to="/evidence">Evidence</NavLink>
      </div>
    </nav>
  );
}
