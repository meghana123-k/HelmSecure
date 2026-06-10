export function TableCard({ violations }) {
  return (
    <div className="table-card">
      <div className="table-header">
        <h2 className="section-title">Recent Helmet Violations</h2>
        <span className="record-count">Total Records: {violations.length}</span>
      </div>

      <table className="violations-table">
        <thead>
          <tr>
            <th>Violation ID</th>
            <th>Timestamp</th>
            <th>Violation Type</th>
            <th>Status</th>
          </tr>
        </thead>

        <tbody>
          {violations.length > 0 ? (
            violations.map((violation) => (
              <tr key={violation.id}>
                <td>{violation.id}</td>
                <td>{violation.Timestamp}</td>
                <td>{violation.Violation_Type}</td>
                <td>
                  <span className="status-badge">Recorded</span>
                </td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="4" className="no-data">
                No violations found
              </td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
}
