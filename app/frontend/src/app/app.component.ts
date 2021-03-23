import { Component, OnInit } from '@angular/core';
import { WeatherDataService } from 'Services/weather-data/weather-data.service';
import { WeatherData } from 'Types/weather-data';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.sass']
})
export class AppComponent implements OnInit {

  weatherDatas: WeatherData[] = [];

  constructor(private weatherDataService: WeatherDataService) {
    weatherDataService.getLatestWeatherData().subscribe((data) => {
      console.log(data);
      this.weatherDatas = data;
    });
  }

  ngOnInit(): void {
  }
}
