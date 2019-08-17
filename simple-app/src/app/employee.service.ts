import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Employee } from './employee';

@Injectable({
  providedIn: 'root'
})
export class EmployeeService {
  url = 'http://localhost:5002';

  constructor(private httpClient: HttpClient) { }

  getEmployees() {
    return this.httpClient.get<Employee[]>(`${this.url}/employees`);
  }

  getEmployeeById(id: number) {
    return this.httpClient.get<Employee>(`${this.url}/${id}`);
  }
}