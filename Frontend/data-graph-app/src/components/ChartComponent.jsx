import React, { useEffect, useRef } from 'react';
import { Scatter } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  LinearScale,
  PointElement,
  Tooltip,
  Legend,
} from 'chart.js';

ChartJS.register(LinearScale, PointElement, Tooltip, Legend);

const ChartComponent = ({ dataPoints }) => {
  const chartRef = useRef(null);

  useEffect(() => {
    return () => {
      if (chartRef.current) {
        chartRef.current.destroy();
      }
    };
  }, []);

  const data = {
    datasets: [
      {
        label: 'Scatter Dataset',
        data: dataPoints.map(point => ({ x: point.x_value, y: point.y_value })),
        backgroundColor: 'rgba(75, 192, 192, 1)',
      },
    ],
  };

  return <Scatter ref={chartRef} data={data} />;
};

export default ChartComponent;