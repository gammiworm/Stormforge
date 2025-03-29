import React, { useEffect, useState } from "react";
import ChartComponent from "./ChartComponent";
import axios from "axios";

const GraphDisplay = ({ dataPoints }) => {
  const [bestFit, setBestFit] = useState(null);
  const [interpolation, setInterpolation] = useState(null);
  const [interpolation2, setInterpolation2] = useState(null);

  const [chartType, setChartType] = useState("scatter");

  useEffect(() => {
    if (dataPoints.length === 0) return;

    // Fetch best fit line data from the backend
    axios
      .get("http://localhost:8000/api/get-analysis", { data: dataPoints })
      .then((response) => {
        setBestFit(response.data.bestFit);
        setInterpolation(response.data.interpolation);
        setInterpolation2(response.data.interpolation2);

      })
      .catch((error) => {
        console.error("Error fetching best fit line:", error);
      });
  }, [dataPoints]);

  return (
    <div className="graph-display">
      <h3>Generated Graph</h3>
      {dataPoints.length > 0 && bestFit ? (
        <div className="chart-container">
          <ChartComponent
            dataPoints={dataPoints}
            bestFit={bestFit}
            interpolation={interpolation}
            interpolation2={interpolation2}
            chartType={chartType}
          />
        </div>
      ) : (
        <p>No data points available</p>
      )}
    </div>
  );
};

export default GraphDisplay;
