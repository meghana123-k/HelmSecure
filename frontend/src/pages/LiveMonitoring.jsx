import "./LiveMonitoring.css";
import { API_BASE_URL } from "../config";
function LiveMonitoring() {
  return (
    <div className="live-container">
      <div className="live-header">
        <h1>Live Helmet Monitoring</h1>

        <div className="live-status">● SYSTEM ACTIVE</div>
      </div>

      <div className="video-card">
        <img src={`${API_BASE_URL}/api/video_feed`} alt="Live Feed" />
      </div>

      <div className="monitoring-info">
        <div className="info-card">
          <h3>Camera Status</h3>
          <p>Online</p>
        </div>

        <div className="info-card">
          <h3>Detection Engine</h3>
          <p>Running</p>
        </div>

        <div className="info-card">
          <h3>Monitoring Mode</h3>
          <p>Live</p>
        </div>
      </div>
    </div>
  );
}

export default LiveMonitoring;
