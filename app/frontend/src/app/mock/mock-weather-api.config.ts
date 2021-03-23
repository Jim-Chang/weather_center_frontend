import { HttpEvent, HttpRequest, HttpResponse } from '@angular/common/http';

import { Observable, of } from 'rxjs';
import { WeatherData } from 'Types/weather-data';


function queryWeatherData(request: HttpRequest<any>): Observable<HttpEvent<any>> {
  const fakeData: WeatherData[] = [
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
  ];

  return of(
    new HttpResponse({
      status: 200,
      body: {
        status: 'ok',
        data: fakeData
      },
    }));
}


export const weatherApiHandler = (request: HttpRequest<any>) => {
  if (request.url.includes('/weather/query')) {
    return queryWeatherData;
  } else {
    return null;
  }
};
