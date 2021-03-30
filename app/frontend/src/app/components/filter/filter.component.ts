import { Component, OnInit } from '@angular/core';
import { Subject } from 'rxjs';

@Component({
  selector: 'filter',
  templateUrl: './filter.component.html',
  styleUrls: ['./filter.component.sass']
})
export class FilterComponent implements OnInit {

  private filterHoursSubj = new Subject<number>();
  filterHours$ = this.filterHoursSubj.asObservable();

  constructor() { }

  ngOnInit(): void {
  }

  onClickFilterBtn(hours: number): void {
    this.filterHoursSubj.next(hours);
  }

}
