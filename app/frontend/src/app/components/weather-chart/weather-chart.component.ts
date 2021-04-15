import { Component, Input, OnInit, ViewChild, OnChanges, SimpleChanges } from '@angular/core';
import { ChartDataSets, ChartOptions, ChartType } from 'chart.js';
import { Color, BaseChartDirective, Label } from 'ng2-charts';
import { WeatherData } from 'Types/weather-data';
import * as moment from 'moment';

@Component({
  selector: 'weather-chart',
  templateUrl: './weather-chart.component.html',
  styleUrls: ['./weather-chart.component.sass']
})
export class WeatherChartComponent implements OnInit, OnChanges {

  @Input() weatherDatas: WeatherData[] = [];

  chartData: ChartDataSets[] = [
    {
      label: 'Temperature',
      yAxisID: 'y-axis-0',
      data: [],
    },
    {
      label: 'Humidity',
      yAxisID: 'y-axis-1',
      data: [],
    }
  ];

  chartLabels: Label[] = [];

  chartOptions: ChartOptions = {
    responsive: true,
    elements: {
      point: {
        radius: 0,
      }
    },
    scales: {
      // We use this empty structure as a placeholder for dynamic theming.
      xAxes: [{}],
      yAxes: [
        {
          id: 'y-axis-0',
          position: 'left',
          ticks: {
            fontColor: 'rgba(148,159,255,1)',
            max: 40,
            min: 5,
          }
        },
        {
          id: 'y-axis-1',
          position: 'right',
          ticks: {
            fontColor: 'rgba(77,183,96,1)',
            max: 100,
            min: 30,
          }
        }
      ]
    }
  };
  chartColors: Color[] = [
    { // grey
      backgroundColor: 'rgba(148,159,255,0.2)',
      borderColor: 'rgba(148,159,255,1)',
      pointBackgroundColor: 'rgba(148,159,255,1)',
      pointBorderColor: '#fff',
      pointHoverBackgroundColor: '#fff',
      pointHoverBorderColor: 'rgba(148,159,255,0.8)'
    },
    { // dark grey
      backgroundColor: 'rgba(77,183,96,0.2)',
      borderColor: 'rgba(77,183,96,1)',
      pointBackgroundColor: 'rgba(77,183,96,1)',
      pointBorderColor: '#fff',
      pointHoverBackgroundColor: '#fff',
      pointHoverBorderColor: 'rgba(77,183,96,1)'
    },
  ];
  chartLegend = true;
  chartType: ChartType = 'line';

  @ViewChild(BaseChartDirective, { static: true }) chart!: BaseChartDirective;

  constructor() { }

  ngOnInit(): void {
  }

  ngOnChanges(changes: SimpleChanges): void {
    if (changes.weatherDatas) {
      this.chartData[0].data = this.weatherDatas.map((data) => data.temperature);
      this.chartData[1].data = this.weatherDatas.map((data) => data.humidity);
      this.chartLabels = this.weatherDatas.map((data) => moment(data.datetime).format('hh:mm'));

      this.chart.update();
    }
  }

}
