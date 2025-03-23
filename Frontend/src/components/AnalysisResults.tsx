
import React from 'react';
import { useEffect, useState} from "react";
import axios from "axios";
import { DataPoint } from "../apiService";

// Define the shape of the API response
type StatsResult = {
  mean: { x: number; y: number };
  median: { x: number; y: number };
  mode: { x: number; y: number } | "No mode";
  bestFit: {
    slope: number;
    intercept: number;
  };
};

// Props type
type AnalysisResultsProps = {
  dataPoints: DataPoint[];
};

const AnalysisResults: React.FC<AnalysisResultsProps> = ({ dataPoints }) => {
  const [stats, setStats] = useState<StatsResult | null>(null);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

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
          <p><strong>Mean:</strong> X = {stats.mean.x}, Y = {stats.mean.y}</p>
          <p><strong>Median:</strong> X = {stats.median.x}, Y = {stats.median.y}</p>
          <p>
            <strong>Mode:</strong>{" "}
            {stats.mode === "No mode"
              ? "No mode results"
              : `X = ${stats.mode.x}, Y = ${stats.mode.y}`}
          </p>
          <p>
            <strong>Best Fit Line:</strong> y = {stats.bestFit.slope.toFixed(2)}x + {stats.bestFit.intercept.toFixed(2)}
          </p>
        </>
      ) : (
        <p>No analysis data available.</p>
      )}
    </div>
  );
};

export default AnalysisResults;
