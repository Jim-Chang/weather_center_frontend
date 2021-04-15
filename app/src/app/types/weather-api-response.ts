import { WeatherData } from 'Types/weather-data';

export interface QueryWeatherDataResponse {
  status: string;
  data: WeatherData[];
};
