import { useEffect, useState } from "react";
import { fetchDataPoints } from "../apiService";
import ChartComponent from "./ChartComponent.jsx";

const GraphDisplay = () => {
  const [dataPoints, setDataPoints] = useState([]);

  useEffect(() => {
    const getDataPoints = async () => {
      try {
        const data = await fetchDataPoints();
        setDataPoints(data);
      } catch (error) {
        console.error("Error fetching data points:", error);
      }
    };

    getDataPoints();
  }, []);

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
