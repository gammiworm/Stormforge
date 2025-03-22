import React from "react";
import ChartComponent from "./ChartComponent.jsx";

const GraphDisplay = ({ dataPoints }) => {
  return (
    <div className="graph-display">
      <h3>Generated Graph</h3>
      {dataPoints.length > 0 ? (
        <ChartComponent dataPoints={dataPoints} />
      ) : (
        <p>No data points available</p>
      )}
    </div>
  );
};

export default GraphDisplay;
