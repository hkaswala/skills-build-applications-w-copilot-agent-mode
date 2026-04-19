import React, { useEffect, useState } from 'react';

const Activities = () => {
  const [activities, setActivities] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchActivities = async () => {
      const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/`;
      console.log('Fetching activities from:', apiUrl);
      try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const data = await response.json();
        console.log('Fetched activities data:', data);
        // Handle both paginated and plain array responses
        const activitiesData = data.results || data;
        setActivities(activitiesData);
      } catch (err) {
        console.error('Error fetching activities:', err);
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchActivities();
  }, []);

  if (loading) return <div className="text-center mt-5"><div className="spinner-border" role="status"><span className="visually-hidden">Loading...</span></div></div>;
  if (error) return <div className="alert alert-danger" role="alert">Error: {error}</div>;

  const columns = activities.length > 0 ? Object.keys(activities[0]) : [];

  return (
    <div>
      <h2 className="mb-4">Activities</h2>
      {activities.length === 0 ? (
        <p className="text-muted">No activities found.</p>
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
              {activities.map((activity, index) => (
                <tr key={index}>
                  {columns.map((col, colIndex) => (
                    <td key={colIndex}>{typeof activity[col] === 'object' ? JSON.stringify(activity[col]) : activity[col]}</td>
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

export default Activities;