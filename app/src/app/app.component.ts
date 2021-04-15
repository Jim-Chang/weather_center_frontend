import { FilterComponent } from 'Components/filter/filter.component';
import { Component, ViewChild, OnInit } from '@angular/core';
import { WeatherDataService } from 'Services/weather-data/weather-data.service';
import { WeatherData } from 'Types/weather-data';
import { mergeMap } from 'rxjs/operators';
import * as moment from 'moment';
import { timer, of } from 'rxjs';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.sass']
})
export class AppComponent implements OnInit {

  weatherDatas: WeatherData[] = [];
  lastWeatherData: WeatherData;

  private defaultWeatherData: WeatherData = {
    datetime: moment().format(),
    temperature: 0,
    humidity: 0,
  };

  private lastQueryHours = 0;

  @ViewChild(FilterComponent, { static: true }) filter!: FilterComponent;

  constructor(private weatherDataService: WeatherDataService) {
    this.lastWeatherData = this.defaultWeatherData;

    weatherDataService.getLatestWeatherData().subscribe((data) => {
      this.lastQueryHours = weatherDataService.defaultQueryHours;
      this.weatherDatas = data;
      this.lastWeatherData = data.length > 0 ? data[data.length - 1] : this.defaultWeatherData;
    });
  }

  ngOnInit(): void {
    this.filter.filterHours$.pipe(
      mergeMap((hours) => {
        this.lastQueryHours = hours;
        return this.weatherDataService.queryWeatherDataByHours(hours)
      })
    ).subscribe((data) => this.handleWeatherData(data));

    this.filter.filterDateRange$.pipe(
      mergeMap((dateRange) => {
        this.lastQueryHours = 0;
        return this.weatherDataService.queryWeatherDataByDateRange(dateRange)
      })
    ).subscribe((data) => this.handleWeatherData(data));

    timer(60000, 60000).pipe(
      mergeMap(() => {
        if (this.lastQueryHours > 0) {
          return this.weatherDataService.queryWeatherDataByHours(this.lastQueryHours)
        }
        return of(null);
      })
    ).subscribe((data) => {
      if (data != null) {
        this.handleWeatherData(data)
      }
    });
  }

  handleWeatherData(data: WeatherData[]): void {
    this.weatherDatas = data;
    this.lastWeatherData = data[data.length - 1];
  }

  get lastDiffMinutes(): number {
    const now = moment();
    const last = moment(this.lastWeatherData.datetime);
    return Math.round(moment.duration(now.diff(last)).asMinutes());
  }

}
