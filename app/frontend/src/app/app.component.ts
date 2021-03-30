import { FilterComponent } from 'Components/filter/filter.component';
import { Component, ViewChild, OnInit } from '@angular/core';
import { WeatherDataService } from 'Services/weather-data/weather-data.service';
import { WeatherData } from 'Types/weather-data';
import { mergeMap } from 'rxjs/operators';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.sass']
})
export class AppComponent implements OnInit {

  weatherDatas: WeatherData[] = [];

  @ViewChild(FilterComponent, { static: true }) filter!: FilterComponent;

  constructor(private weatherDataService: WeatherDataService) {
    weatherDataService.getLatestWeatherData().subscribe((data) => {
      this.weatherDatas = data;
    });
  }

  ngOnInit(): void {
    this.filter.filterHours$.pipe(
      mergeMap((hours) => {
        return this.weatherDataService.queryWeatherData(hours);
      })
    ).subscribe((data) => {
      this.weatherDatas = data;
    }, () => {
      console.log('query weather data error');
    });
  }

}
