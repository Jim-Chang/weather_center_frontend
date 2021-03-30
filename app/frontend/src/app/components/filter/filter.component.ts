import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'filter',
  templateUrl: './filter.component.html',
  styleUrls: ['./filter.component.sass']
})
export class FilterComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

  onClickFilterBtn(hours: number): void {
    console.log('onClickFilterBtn', hours);
  }

}
