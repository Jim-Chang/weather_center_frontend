import { DateRange } from 'Types/date-range';
import { Component, OnInit, ViewChild } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';
import { MatDateRangeInput } from '@angular/material/datepicker';
import { Subject } from 'rxjs';

@Component({
  selector: 'filter',
  templateUrl: './filter.component.html',
  styleUrls: ['./filter.component.sass']
})
export class FilterComponent implements OnInit {

  @ViewChild(MatDateRangeInput, { static: true }) dateRangeInput!: MatDateRangeInput<Date>;

  private filterHoursSubj = new Subject<number>();
  filterHours$ = this.filterHoursSubj.asObservable();

  private filterDateRangeSubj = new Subject<DateRange>();
  filterDateRange$ = this.filterDateRangeSubj.asObservable();

  constructor() { }

  ngOnInit(): void {
  }

  onClickFilterBtn(hours: number): void {
    this.filterHoursSubj.next(hours);
  }

  onCloseDateRangePicker(): void {
    if (this.dateRangeInput.value) {
      const startDate = this.dateRangeInput.value.start;
      const endDate = this.dateRangeInput.value.end;

      if (startDate && endDate) {
        this.filterDateRangeSubj.next({
          startDate,
          endDate,
        });
      }
    }
  }
}
