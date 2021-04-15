import { HttpEvent, HttpRequest, HttpResponse } from '@angular/common/http';

import { Observable, of } from 'rxjs';
import { WeatherData } from 'Types/weather-data';

import * as moment from 'moment';

function getRandTemp(): number {
  return Math.round((Math.random() * 20 + 15) * 10) / 10;
}

function getRandHum(): number {
  return Math.round(Math.random() * 65 + 35);
}

function queryWeatherData(request: HttpRequest<any>): Observable<HttpEvent<any>> {
  const fakeData: WeatherData[] = [];
  const dataLen = 100

  for (let i = 0; i < dataLen; i++) {
    fakeData.push({
      datetime: moment().subtract(dataLen - i, 'minutes').format(),
      temperature: getRandTemp(),
      humidity: getRandHum(),
    });
  }

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
