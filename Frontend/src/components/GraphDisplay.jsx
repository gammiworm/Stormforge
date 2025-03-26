import React, { useEffect, useState } from "react";
import ChartComponent from "./ChartComponent";
import axios from "axios";

const GraphDisplay = ({ dataPoints }) => {
  const [bestFit, setBestFit] = useState(null);
  const [chartType, setChartType] = useState("scatter");

  useEffect(() => {
    if (dataPoints.length === 0) return;

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
      {dataPoints.length > 0 && bestFit ? (
        <div className="chart-container">
          <ChartComponent
            dataPoints={dataPoints}
            bestFit={bestFit}
            chartType={chartType}
          />
        </div>
      ) : (
        <p>No data points available</p>
      )}
      <div className="toggle-controls radio-group">
        <label>
          <input
            type="radio"
            value="scatter"
            checked={chartType === "scatter"}
            onChange={() => setChartType("scatter")}
          />
          <span>Scatter Plot</span>
        </label>
        <label>
          <input
            type="radio"
            value="line"
            checked={chartType === "line"}
            onChange={() => setChartType("line")}
          />
          <span>Line Plot</span>
        </label>
      </div>
    </div>
  );
};


export default GraphDisplay;