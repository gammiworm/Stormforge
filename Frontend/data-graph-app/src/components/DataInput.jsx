import React, { useState } from 'react';
import { createDataPoint } from '../apiService';

const DataInput = () => {
    const [xValue, setXValue] = useState('');
    const [yValue, setYValue] = useState('');

    const handleCreateDataPoint = async () => {
        try {
            await createDataPoint(Number(xValue), Number(yValue));
            setXValue('');
            setYValue('');
        } catch (error) {
            console.error("Error creating data point:", error);
        }
    };

    return (
        <div>
            <input
                type="number"
                placeholder="Enter x value"
                value={xValue}
                onChange={(e) => setXValue(e.target.value)}
            />
            <input
                type="number"
                placeholder="Enter y value"
                value={yValue}
                onChange={(e) => setYValue(e.target.value)}
            />
            <button onClick={handleCreateDataPoint}>Create Data Point</button>
        </div>
    );
};

export default DataInput;
