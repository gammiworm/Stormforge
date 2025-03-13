import { useState } from "react";

const DataInput = ({ setDataPoints }) => {
  const [inputs, setInputs] = useState([{ x: "", y: "" }]); // Initial (x, y) pair

  const handleChange = (index, field, value) => {
    const newInputs = [...inputs];
    newInputs[index][field] = value;
    setInputs(newInputs);
  };

  const addInputField = () => {
    setInputs([...inputs, { x: "", y: "" }]); // Add a new (x, y) pair
  };

  const handleSubmit = () => {
    // Convert inputs to numbers and update state in parent
    const formattedData = inputs
      .map(({ x, y }) => ({
        x: parseFloat(x),
        y: parseFloat(y),
      }))
      .filter(({ x, y }) => !isNaN(x) && !isNaN(y));

    setDataPoints(formattedData);
  };

  return (
    <div className="data-input">
      <h3>Input Data Points</h3>
      {inputs.map((input, index) => (
        <div key={index} className="xy-input">
          <input
            type="number"
            value={input.x}
            onChange={(e) => handleChange(index, "x", e.target.value)}
            placeholder={`x = `}
          />
          <input
            type="number"
            value={input.y}
            onChange={(e) => handleChange(index, "y", e.target.value)}
            placeholder={`y = `}
          />
        </div>
      ))}
      <button className="plus-button" onClick={addInputField}>+</button>
      <button onClick={handleSubmit}>Generate</button>
    </div>
  );
};

export default DataInput;
