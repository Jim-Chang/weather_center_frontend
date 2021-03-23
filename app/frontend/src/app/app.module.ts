import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { ChartsModule } from 'ng2-charts';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { WeatherChartComponent } from 'Components/weather-chart/weather-chart.component';
import { mockApihttpInterceptorProviders } from 'Mock/mock-api.intercepter';

@NgModule({
  declarations: [
    AppComponent,
    WeatherChartComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    ChartsModule,
  ],
  providers: [mockApihttpInterceptorProviders],
  bootstrap: [AppComponent]
})
export class AppModule { }
