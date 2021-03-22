import { Injectable } from '@angular/core';
import { WeatherData } from '../../types/weather-data';
import { Observable, of } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class WeatherDataService {

  constructor() { }

  getLatestWeatherData(): Observable<WeatherData[]> {
    return of([
      {
        datetime: '2021/1/1',
        temperature: 21,
        humidity: 60,
      },
      {
        datetime: '2021/1/2',
        temperature: 23,
        humidity: 63,
      },
      {
        datetime: '2021/1/3',
        temperature: 21,
        humidity: 62,
      },
      {
        datetime: '2021/1/4',
        temperature: 22,
        humidity: 66,
      },
      {
        datetime: '2021/1/5',
        temperature: 25,
        humidity: 61,
      },
    ])
  }
}
