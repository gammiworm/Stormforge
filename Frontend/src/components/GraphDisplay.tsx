import React from "react";
import ChartComponent from "./ChartComponent";
import { DataPoint } from "../apiService"; // ✅ import the type

// Define props type
type GraphDisplayProps = {
  dataPoints: DataPoint[];
};

const GraphDisplay: React.FC<GraphDisplayProps> = ({ dataPoints }) => {
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
