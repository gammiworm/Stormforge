import { useEffect, useState } from "react";
import axios from "axios";

const AnalysisResults = ({ dataPoints }) => {
  const [stats, setStats] = useState(null);

  useEffect(() => {
    if (dataPoints.length === 0) return;

    axios
      .post("http://localhost:5000/get-analysis", { data: dataPoints })
      .then((response) => {
        setStats(response.data);
      })
      .catch((error) => {
        console.error("Error fetching analysis:", error);
      });
  }, [dataPoints]);

  return (
    <div className="analysis-results">
      <h3>Analysis</h3>
      {stats ? (
        <>
          <p>Mean: {stats.mean}</p>
          <p>Median: {stats.median}</p>
          <p>Standard Deviation: {stats.stdDev}</p>
          <p>Best Fit: {stats.bestFit}</p>
        </>
      ) : (
        <p></p>
      )}
    </div>
  );
};

export default AnalysisResults;
