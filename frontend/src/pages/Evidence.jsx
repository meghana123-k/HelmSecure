// src/pages/Evidence.jsx

import { EvidenceCard } from "../components/EvidenceCard";
import "./Evidence.css";
import { fetchEvidence } from "../services/evidenceService";
import { useEffect, useState } from "react";
function Evidence() {
  const [evidences, setEvidences] = useState([]);
  const [loading, setLoading] = useState(true);

  // /api/evidence
  // [
  //   {
  //     "filename": "violation_001.jpg",
  //     "image_url": "/static/screenshots/violation_001.jpg"
  //   }
  // ]
  // display Screenshot
  // Timestamp
  // Violation Type
  //
  useEffect(() => {
    const fetchEvidences = async () => {
      try {
        const evidences = await fetchEvidence();
        setEvidences(evidences);
      } catch (error) {
        console.error(error);
      }
      setLoading(false);
    };
    fetchEvidences();
  }, []);
  if (loading) {
    return <h2>Loading...</h2>;
  }
  return (
    <div className="evidence-container">
      <div className="evidence-header">
        <h1>Violation Evidences</h1>
        <p>Visual proof of recorded helmet violations</p>
      </div>
      <EvidenceCard evidences={evidences} />
    </div>
  );
}
export default Evidence;
