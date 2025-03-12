import { useState } from "react";
import DataInput from "../components/DataInput";
import GraphDisplay from "../components/GraphDisplay";
import AnalysisResults from "../components/AnalysisResults";

const Home = () => {
  const [dataPoints, setDataPoints] = useState([]);

  return (
    <div className="home">
      <DataInput setDataPoints={setDataPoints} />
      <GraphDisplay dataPoints={dataPoints} />
      <AnalysisResults dataPoints={dataPoints} />
    </div>
  );
};

export default Home;
