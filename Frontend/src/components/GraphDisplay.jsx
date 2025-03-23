import React, { useEffect, useState } from "react";
import ChartComponent from "./ChartComponent";
import axios from "axios";

const GraphDisplay = ({ dataPoints }) => {
  const [bestFit, setBestFit] = useState(null);

  useEffect(() => {
    if (dataPoints.length === 0) return;

    // Fetch best fit line data from the backend
    axios
      .post("http://localhost:8000/api/get-analysis", { data: dataPoints })
      .then((response) => {
        setBestFit(response.data.bestFit);
      })
      .catch((error) => {
        console.error("Error fetching best fit line:", error);
      });
  }, [dataPoints]);

  return (
    <div className="graph-display">
      <h3>Generated Graph</h3>
      {dataPoints.length > 0 && bestFit ? (
        <ChartComponent dataPoints={dataPoints} bestFit={bestFit} />
      ) : (
        <p>No data points available</p>
      )}
    </div>
  );
};

export default GraphDisplay;
