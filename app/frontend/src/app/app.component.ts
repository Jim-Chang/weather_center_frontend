import { Component, OnInit } from '@angular/core';
import { WeatherDataService } from './services/weather-data/weather-data.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.sass']
})
export class AppComponent implements OnInit {

  constructor(private weatherDataService: WeatherDataService) {
    weatherDataService.getLatestWeatherData().subscribe((data) => {
      console.log(data);
    });
  }

  ngOnInit(): void {
  }
}
