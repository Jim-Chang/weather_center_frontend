import { Component, OnInit, ViewChild } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';
import { MatDateRangeInput } from '@angular/material/datepicker';
import { start } from 'node:repl';
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

  private filterDateRangeSubj = new Subject<>();

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
        const startDateFmt = this.formatDate(startDate) + 'T00:00:00';
        const endDateFmt = this.formatDate(endDate) + 'T23:59:59';
        console.log(startDateFmt, endDateFmt);
      }
    }
  }

  private formatDate(date: Date): string {
    var mm = date.getMonth() + 1; // getMonth() is zero-based
    var dd = date.getDate();

    return [date.getFullYear(),
    (mm > 9 ? '' : '0') + mm,
    (dd > 9 ? '' : '0') + dd
    ].join('-');
  }

}
