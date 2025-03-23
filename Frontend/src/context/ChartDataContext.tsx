import React, { createContext, useState, useEffect, ReactNode } from 'react';
import { fetchDataPoints, DataPoint} from '../apiService';


type ChartDataContextType = {
    dataPoints: DataPoint[];
    setDataPoints: React.Dispatch<React.SetStateAction<DataPoint[]>>;
};

export const ChartDataContext = createContext<ChartDataContextType | null>(null);

// Props for the provider
type ChartDataProviderProps = {
    children: ReactNode;
};

export const ChartDataProvider: React.FC<ChartDataProviderProps> = ({ children }) => {
    const [dataPoints, setDataPoints] = useState<DataPoint[]>([]);
  
    useEffect(() => {
      const getDataPoints = async () => {
        try {
          const data = await fetchDataPoints();
          setDataPoints(data);
        } catch (error) {
          console.error("Error fetching data points:", error);
        }
      };
  
      getDataPoints();
    }, []);
  
    return (
      <ChartDataContext.Provider value={{ dataPoints, setDataPoints }}>
        {children}
      </ChartDataContext.Provider>
    );
  };