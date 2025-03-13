import { useEffect, useState } from "react";
import axios from "axios";

const GraphDisplay = ({ dataPoints }) => {
  const [graphUrl, setGraphUrl] = useState(null);

  useEffect(() => {
    if (dataPoints.length === 0) return;

    axios
      .post("http://localhost:5000/generate-graph", { data: dataPoints })
      .then((response) => {
        setGraphUrl(response.data.imageUrl); // Backend should return an image URL
      })
      .catch((error) => {
        console.error("Error fetching graph:", error);
      });
  }, [dataPoints]);

  return (
    <div className="graph-display">
      <h3>Generated Graph</h3>
      {graphUrl ? <img src={graphUrl} alt="Generated Graph" /> : <p></p>}
    </div>
  );
};

export default GraphDisplay;
