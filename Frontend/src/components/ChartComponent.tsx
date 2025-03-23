import React from 'react';
import { Scatter } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  LinearScale,
  PointElement,
  Tooltip,
  Legend,
} from 'chart.js';
import { DataPoint } from '../apiService';

// Register chart.js components
ChartJS.register(LinearScale, PointElement, Tooltip, Legend);

type ChartComponentProps = {
  dataPoints: DataPoint[];
};

const ChartComponent: React.FC<ChartComponentProps> = ({ dataPoints }) => {
  const data = {
    datasets: [
      {
        label: 'Scatter Dataset',
        data: dataPoints.map((point) => ({
          x: point.x,
          y: point.y,
        })),
        backgroundColor: 'rgba(75, 192, 192, 1)',
      },
    ],
  };

  return <Scatter data={data} />;
};

export default ChartComponent;
