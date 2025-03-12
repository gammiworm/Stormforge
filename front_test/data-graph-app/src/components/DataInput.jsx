import { useState } from "react";

const DataInput = ({ setDataPoints }) => {
  const [inputs, setInputs] = useState([""]); // Initial empty input field

  const handleChange = (index, value) => {
    const newInputs = [...inputs];
    newInputs[index] = value;
    setInputs(newInputs);
  };

  const addInputField = () => {
    setInputs([...inputs, ""]);
  };

  const handleSubmit = () => {
    // Convert inputs to numbers and update state in parent
    setDataPoints(inputs.map(Number).filter(n => !isNaN(n)));
  };

  return (
    <div className="data-input">
      <h3>Input Data Points</h3>
      {inputs.map((input, index) => (
        <input
          key={index}
          type="number"
          value={input}
          onChange={(e) => handleChange(index, e.target.value)}
          placeholder={`Data point ${index + 1}`}
        />
      ))}
      <button onClick={addInputField}>+</button>
      <button onClick={handleSubmit}>Generate</button>
    </div>
  );
};

export default DataInput;
