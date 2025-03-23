import React from "react";
import { useState, useEffect } from "react";
import DataInput from "../components/DataInput";
import GraphDisplay from "../components/GraphDisplay";
import AnalysisResults from "../components/AnalysisResults";
import { fetchDataPoints, DataPoint } from "../apiService";

const Home = () => {
  const [dataPoints, setDataPoints] = useState<DataPoint[]>([]);

  const refreshDataPoints = async () => {
    try {
      const data = await fetchDataPoints();
      setDataPoints(data);
    } catch (error) {
      console.error("Error fetching data points:", error);
    }
  };

  useEffect(() => {
    console.log("Data points:", dataPoints); // Log data points
    refreshDataPoints();
  }, []);

  return (
    <div className="home">
      <DataInput onDataPointCreated={refreshDataPoints} />
      <GraphDisplay dataPoints={dataPoints} />
      <AnalysisResults dataPoints={dataPoints} />
    </div>
  );
};

export default Home;
