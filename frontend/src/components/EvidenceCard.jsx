export function EvidenceCard({ evidences }) {
  return (
    <div className="evidence-card">
      <h2 className="section-title">Recorded Violation Evidence</h2>

      <div className="evidence-grid">
        {evidences.length > 0 ? (
          evidences.map((evidence, index) => (
            <div key={evidence.filename} className="evidence-item">
              <img
                src={evidence.image_url}
                alt={`Evidence ${index + 1}`}
                className="evidence-image"
              />

              <div className="evidence-info">
                <p>
                  <span className="evidence-label">Evidence ID:</span>{" "}
                  <span className="evidence-value">{index + 1}</span>
                </p>

                <p>
                  <span className="evidence-label">File Name:</span>{" "}
                  <span className="evidence-value">{evidence.filename}</span>
                </p>

                <span className="evidence-status">VERIFIED VIOLATION</span>
              </div>
            </div>
          ))
        ) : (
          <p className="no-evidence">No violation evidence available.</p>
        )}
      </div>
    </div>
  );
}
