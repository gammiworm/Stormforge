import axios from 'axios';

const API_URL = 'http://localhost:8000/api/';

export const createDataPoint = async (x, y) => {
    try {
        const response = await axios.post(`${API_URL}crud/`, {
            operation: 'create',
            metadata: {
                changes: { x, y }
            }
        });
        return response.data;
    } catch (error) {
        console.error("Error creating data point:", error);
        throw error;
    }
};

export const fetchDataPoints = async () => {
    try {
        const response = await axios.get(`${API_URL}crud/`);
        return response.data;
    } catch (error) {
        console.error("Error fetching data points:", error);
        throw error;
    }
};