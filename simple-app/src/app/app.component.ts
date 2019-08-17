import { Component } from '@angular/core';
import { Employee } from './employee';
import { EmployeeService } from './employee.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'simple-app';
  employees: Employee[];

  constructor(private employeeService: EmployeeService) { }

  getAllEmployees() {
    this.employeeService.getEmployees().subscribe(e => {
      console.log(e);
      this.employees = e;
    });
  }
}
