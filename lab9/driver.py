"""CS 108 Lab 9

This driver uses the Employee class to compute and save corporate statistics.

@author: Sam Hoogewind (sth6)
@date: Fall, 2020
"""

from employee import Employee

employees = []

# Load an employee object for each employee specified in 'employees.txt' into the employees list.
employee_list = open("employees.txt")
count = 0
for line in employee_list:
    values = line.split(' ')
    employees.append(Employee(values[0], values[1], values[2], int(values[3])))
    count += 1
employee_list.close()

# Accumulate the sum of all salaries and the total number of employyes at a given rank in dictionaries.
if employees == []:
    print("There are no employees.")
else:
    totals = {}
    counts = {}
    max_employee = employees[0]
    min_employee = employees[0]
    for employee in employees:
        rank = employee.rank
        salary = employee.salary
        if rank in totals:
            totals[rank] += salary
            counts[rank] += 1
        else:
            totals[rank] = salary
            counts[rank] = 1
        if salary > max_employee.salary:
            max_employee = employee
        if salary < min_employee.salary:
            min_employee = employee

# Compute statistics for employees
# Write the statistics for employees into the 'employee-stats.txt' file.
employee_stats = open("employee-stats.txt", "w")
employee_stats.write("Maximum Salary: " + str(max_employee) + "\n")
employee_stats.write("Minimum Salary: " + str(min_employee) + "\n")
employee_stats.write("Rank\tAverage Salary\n")
for rank in totals:
    ave_salary = totals[rank]/counts[rank]
    employee_stats.write(rank + "\t" + '{:.2f}'.format(ave_salary) + "\n")
employee_stats.close()

# Write the total number of employees into the 'employee-count.txt' file.
employee_count = open("employee-count.txt", "w")
employee_count.write(str(count))
employee_count.close()
