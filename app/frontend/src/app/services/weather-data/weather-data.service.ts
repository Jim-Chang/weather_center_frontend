import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { WeatherData } from 'Types/weather-data';
import { QueryWeatherDataResponse } from 'Types/weather-api-response';
import { Observable, of } from 'rxjs';
import { catchError, map } from 'rxjs/operators';
import * as moment from 'moment';
@Injectable({
  providedIn: 'root'
})
export class WeatherDataService {

  private queryWeatherDataUrl = '/api/v1/weather/query';

  constructor(private http: HttpClient) { }

  getLatestWeatherData(): Observable<WeatherData[]> {
    return this.queryWeatherData(3);
  }

  queryWeatherData(hours: number): Observable<WeatherData[]> {
    const startDatetime = moment().subtract(hours, 'hours').format();
    const endDatetime = moment().format();

    const params = new HttpParams().set('start_datetime', startDatetime).set('end_datetime', endDatetime);
    return this.http.get<QueryWeatherDataResponse>(this.queryWeatherDataUrl, { params }).pipe(
      map((resp) => resp.data)
    );
  }

}
