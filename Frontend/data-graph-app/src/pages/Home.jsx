import { useState, useEffect } from "react";
import DataInput from "../components/DataInput";
import GraphDisplay from "../components/GraphDisplay";
import { fetchDataPoints } from "../apiService";

const Home = () => {
  const [dataPoints, setDataPoints] = useState([]);

  const refreshDataPoints = async () => {
    try {
      const data = await fetchDataPoints();
      setDataPoints(data);
    } catch (error) {
      console.error("Error fetching data points:", error);
    }
  };

  useEffect(() => {
    refreshDataPoints();
  }, []);

  return (
    <div className="home">
      <DataInput onDataPointCreated={refreshDataPoints} />
      <GraphDisplay dataPoints={dataPoints} />
    </div>
  );
};

export default Home;
