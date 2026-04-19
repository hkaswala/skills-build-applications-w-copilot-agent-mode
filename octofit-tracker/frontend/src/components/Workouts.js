import React, { useEffect, useState } from 'react';

const Workouts = () => {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchWorkouts = async () => {
      const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;
      console.log('Fetching workouts from:', apiUrl);
      try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const data = await response.json();
        console.log('Fetched workouts data:', data);
        // Handle both paginated and plain array responses
        const workoutsData = data.results || data;
        setWorkouts(workoutsData);
      } catch (err) {
        console.error('Error fetching workouts:', err);
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchWorkouts();
  }, []);

  if (loading) return <div className="text-center mt-5"><div className="spinner-border" role="status"><span className="visually-hidden">Loading...</span></div></div>;
  if (error) return <div className="alert alert-danger" role="alert">Error: {error}</div>;

  const columns = workouts.length > 0 ? Object.keys(workouts[0]) : [];

  return (
    <div>
      <h2 className="mb-4">Workouts</h2>
      {workouts.length === 0 ? (
        <p className="text-muted">No workouts found.</p>
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
              {workouts.map((workout, index) => (
                <tr key={index}>
                  {columns.map((col, colIndex) => (
                    <td key={colIndex}>{typeof workout[col] === 'object' ? JSON.stringify(workout[col]) : workout[col]}</td>
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

export default Workouts;