import { useEffect, useState } from "react";
import axios from "axios";

const AnalysisResults = ({ dataPoints }) => {
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (dataPoints.length === 0) return;

    setLoading(true);
    setError(null);

    axios
      .post("http://localhost:8000/api/get-analysis", { data: dataPoints })
      .then((response) => {
        console.log("Analysis data:", response.data);
        setStats(response.data);
      })
      .catch((error) => {
        console.error("Error fetching analysis:", error);
        setError("Failed to fetch analysis data.");
      })
      .finally(() => {
        setLoading(false);
      });
  }, [dataPoints]);

  return (
    <div className="analysis-results">
      <h3>Analysis</h3>
      {loading ? (
        <p>Loading...</p>
      ) : error ? (
        <p>{error}</p>
      ) : stats ? (
        <>
          <p>Mean: X = {stats.mean.x}, Y = {stats.mean.y}</p>
          <p>Median: X = {stats.median.x}, Y = {stats.median.y}</p>
          <p>
            Mode:{" "}
            {stats.mode === "No mode"
              ? "No mode results"
              : `X = ${stats.mode.x}, Y = ${stats.mode.y}`}
          </p>
        </>
      ) : (
        <p>No analysis data available.</p>
      )}
    </div>
  );
};

export default AnalysisResults;
