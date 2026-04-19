import React, { useEffect, useState } from 'react';

const Leaderboard = () => {
  const [leaderboard, setLeaderboard] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchLeaderboard = async () => {
      const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;
      console.log('Fetching leaderboard from:', apiUrl);
      try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const data = await response.json();
        console.log('Fetched leaderboard data:', data);
        // Handle both paginated and plain array responses
        const leaderboardData = data.results || data;
        setLeaderboard(leaderboardData);
      } catch (err) {
        console.error('Error fetching leaderboard:', err);
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchLeaderboard();
  }, []);

  if (loading) return <div className="text-center mt-5"><div className="spinner-border" role="status"><span className="visually-hidden">Loading...</span></div></div>;
  if (error) return <div className="alert alert-danger" role="alert">Error: {error}</div>;

  const columns = leaderboard.length > 0 ? Object.keys(leaderboard[0]) : [];

  return (
    <div>
      <h2 className="mb-4">Leaderboard</h2>
      {leaderboard.length === 0 ? (
        <p className="text-muted">No leaderboard data found.</p>
      ) : (
        <div className="table-responsive">
          <table className="table table-striped table-hover">
            <thead className="table-dark">
              <tr>
                {columns.map((col, index) => (
                  <th key={index} scope="col">{col}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {leaderboard.map((entry, index) => (
                <tr key={index}>
                  {columns.map((col, colIndex) => (
                    <td key={colIndex}>{typeof entry[col] === 'object' ? JSON.stringify(entry[col]) : entry[col]}</td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
};

export default Leaderboard;