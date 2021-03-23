import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { WeatherData } from 'Types/weather-data';
import { QueryWeatherDataResponse } from 'Types/weather-api-response';
import { Observable, of } from 'rxjs';
import { catchError, map } from 'rxjs/operators';
@Injectable({
  providedIn: 'root'
})
export class WeatherDataService {

  queryWeatherDataUrl = '/api/v1/weather/query';

  constructor(private http: HttpClient) { }

  getLatestWeatherData(): Observable<WeatherData[]> {
    const params = new HttpParams().set('start_datetime', '2021-01-01').set('end_datetime', '2021-01-02')
    return this.http.get<QueryWeatherDataResponse>(this.queryWeatherDataUrl, { params }).pipe(
      map((resp) => resp.data)
    );
  }

}
