import { useState } from "react"

/*
DataInput component expects to receive a function setDataPoints as a prop from its parent component.
state variable Inputs store array of strings of user inputs, setInputs is a function that updates Inputs. empty string means intial emptry input field
*/
const DataInput = ({ setDataPoints }) => { 
    const [Inputs, setInputs] = useState([""]); 

    const handleChange = (index, value) => {
        const newInputs = [...inputs];  // Create a copy of the current inputs array
        newInputs[index] = value;       // Update the value at the specific index
        setInputs(newInputs);           // Update the state with the new array
    };

    const addInputField = () => {
        setInputs([...inputs, ""]);
    };

    const handleSubmit = () => {
        setDataPoints(inputs.map(Number).filter(n => !isNaN(n))); //Converts the array of strings into numbers, removes any values that are NaN (invalid numbers).
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
