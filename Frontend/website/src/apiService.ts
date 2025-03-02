// filepath: /c:/Users/mehar/OneDrive/Documents/GitHub/Stormforge/Frontend/website/src/apiService.ts

import axios from 'axios';

const API_URL = 'http://localhost:8000/api/crud/';

export const createDataPoint = async (x: number, y: number) => {
    const response = await axios.post(API_URL, {
        operation: 'create',
        metadata: {
            changes: { x, y }
        }
    });
    return response.data;
};

export const readDataPoints = async () => {
    const response = await axios.post(API_URL, {
        operation: 'read'
    });
    return response.data;
};

export const updateDataPoint = async (id: number, x: number, y: number) => {
    const response = await axios.post(API_URL, {
        operation: 'update',
        metadata: {
            changes: { id, x, y }
        }
    });
    return response.data;
};

export const deleteDataPoint = async (id: number) => {
    const response = await axios.post(API_URL, {
        operation: 'delete',
        metadata: {
            changes: { id }
        }
    });
    return response.data;
};