import { FilterComponent } from 'Components/filter/filter.component';
import { Component, ViewChild, OnInit } from '@angular/core';
import { WeatherDataService } from 'Services/weather-data/weather-data.service';
import { WeatherData } from 'Types/weather-data';
import { mergeMap } from 'rxjs/operators';
import * as moment from 'moment';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.sass']
})
export class AppComponent implements OnInit {

  weatherDatas: WeatherData[] = [];
  lastWeatherData: WeatherData = {
    datetime: moment().format(),
    temperature: 0,
    humidity: 0,
  };

  @ViewChild(FilterComponent, { static: true }) filter!: FilterComponent;

  constructor(private weatherDataService: WeatherDataService) {
    weatherDataService.getLatestWeatherData().subscribe((data) => {
      this.weatherDatas = data;
      this.lastWeatherData = data[data.length - 1];
    });
  }

  ngOnInit(): void {
    this.filter.filterHours$.pipe(
      mergeMap((hours) => this.weatherDataService.queryWeatherDataByHours(hours))
    ).subscribe((data) => this.handleWeatherData(data));

    this.filter.filterDateRange$.pipe(
      mergeMap((dateRange) => this.weatherDataService.queryWeatherDataByDateRange(dateRange))
    ).subscribe((data) => this.handleWeatherData(data));
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
