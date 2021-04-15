import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { WeatherData } from 'Types/weather-data';
import { DateRange } from 'Types/date-range';
import { QueryWeatherDataResponse } from 'Types/weather-api-response';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import * as moment from 'moment';
@Injectable({
  providedIn: 'root'
})
export class WeatherDataService {

  defaultQueryHours = 3;
  private queryWeatherDataUrl = `/api/v1/weather/query`;

  constructor(private http: HttpClient) { }

  getLatestWeatherData(): Observable<WeatherData[]> {
    return this.queryWeatherDataByHours(this.defaultQueryHours);
  }

  queryWeatherDataByHours(hours: number): Observable<WeatherData[]> {
    const startDatetime = moment().subtract(hours, 'hours').format('YYYY-MM-DD HH:mm:ss');
    const endDatetime = moment().format('YYYY-MM-DD HH:mm:ss');

    return this.queryWeatherData(startDatetime, endDatetime);
  }

  queryWeatherDataByDateRange(dateRange: DateRange): Observable<WeatherData[]> {
    const startDatetime = this.formatDate(dateRange.startDate) + ' 00:00:00';
    const endDatetime = this.formatDate(dateRange.endDate) + ' 23:59:59';

    return this.queryWeatherData(startDatetime, endDatetime);
  }

  private queryWeatherData(startDatetime: string, endDatetime: string): Observable<WeatherData[]> {
    const params = new HttpParams().set('start_datetime', startDatetime).set('end_datetime', endDatetime);
    return this.http.get<QueryWeatherDataResponse>(this.queryWeatherDataUrl, { params }).pipe(
      map((resp) => resp.data)
    );
  }

  private formatDate(date: Date): string {
    const mm = date.getMonth() + 1; // getMonth() is zero-based
    const dd = date.getDate();

    return [date.getFullYear(),
    (mm > 9 ? '' : '0') + mm,
    (dd > 9 ? '' : '0') + dd
    ].join('-');
  }

}
