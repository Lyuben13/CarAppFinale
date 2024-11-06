import csv
import os
import re
from loguru import logger

# Пътища до CSV файловете
EMPLOYEES_FILE = 'employees.csv'
CARS_FILE = 'cars.csv'
SALES_FILE = 'sales.csv'

# Конфигуриране на логването
logger.add("file.log", rotation="1 MB", level="INFO", backtrace=True, diagnose=True)


# Инициализация на CSV файловете, ако не съществуват
def initialize_files():
    files = {
        EMPLOYEES_FILE: ['Name', 'Position', 'Contact Number', 'Email'],
        CARS_FILE: ['Make', 'Model', 'Year', 'Cost Price', 'Sale Price'],
        SALES_FILE: ['Employee', 'Car', 'Date of Sale', 'Actual Selling Price']
    }

    for file_name, headers in files.items():
        if not os.path.isfile(file_name):
            with open(file_name, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(headers)
                logger.info(f"Initialized file: {file_name} with headers: {headers}")


# Валидация на формата на email адреса
def is_valid_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email) is not None


# Валидация на годината
def is_valid_year(year):
    return year.isdigit() and 1886 <= int(year) <= 2024


# Валидация на датата на продажба
def is_valid_date(date):
    regex = r'^\d{4}-\d{2}-\d{2}$'
    return re.match(regex, date) is not None


# Добавяне на служител
def add_employee(name, position, contact_number, email):
    if not is_valid_email(email):
        logger.error(f"Invalid email format: {email}")
        raise ValueError(f"Invalid email format: {email}")

    with open(EMPLOYEES_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, position, contact_number, email])
        logger.info(f"Added employee: {name}")


# Добавяне на автомобил
def add_car(make, model, year, cost_price, sale_price):
    if not is_valid_year(year):
        logger.error(f"Invalid year: {year}")
        raise ValueError(f"Invalid year: {year}")

    with open(CARS_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([make, model, year, cost_price, sale_price])
        logger.info(f"Added car: {make} {model} ({year})")


# Добавяне на продажба
def add_sale(employee_name, car_model, sale_date, actual_selling_price):
    if not is_valid_date(sale_date):
        logger.error(f"Invalid sale date: {sale_date}")
        raise ValueError(f"Invalid sale date: {sale_date}")

    with open(SALES_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([employee_name, car_model, sale_date, actual_selling_price])  # Обновен ред
        logger.info(f"Added sale: {employee_name} sold {car_model} on {sale_date} for {actual_selling_price}")


# Изтриване на служител
def delete_employee(employee_name):
    employees = list_employees()
    logger.debug(f"Employees before deletion: {employees}")

    if not employees:
        logger.error("No employees to delete.")
        raise ValueError("No employees to delete.")

    deleted = False
    with open(EMPLOYEES_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Position', 'Contact Number', 'Email'])

        for emp in employees:
            if emp[0].strip() != employee_name.strip():
                writer.writerow(emp)
            else:
                deleted = True
                logger.info(f"Deleted employee: {emp}")

    if not deleted:
        logger.error(f"Employee '{employee_name}' not found.")
        raise ValueError(f"Employee '{employee_name}' not found.")
    else:
        logger.info(f"Employee '{employee_name}' has been deleted successfully.")
        logger.debug(f"Current list of employees: {list_employees()}")


# Изтриване на автомобил
def delete_car(model):
    cars = list_cars()
    deleted = False
    with open(CARS_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Make', 'Model', 'Year', 'Cost Price', 'Sale Price'])
        for car in cars:
            if car[1].strip() != model.strip():
                writer.writerow(car)
            else:
                deleted = True
                logger.info(f"Deleted car model: {car}")

    if not deleted:
        logger.error(f"Car model '{model}' not found.")
        raise ValueError(f"Car model '{model}' not found.")
    else:
        logger.info(f"Car model '{model}' has been deleted successfully.")
        logger.debug(f"Current list of cars: {list_cars()}")


# Изтриване на продажба
def delete_sale(sale_date):
    sales = list_sales()
    deleted = False
    with open(SALES_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Employee', 'Car', 'Date of Sale', 'Actual Selling Price'])
        for sale in sales:
            if sale[2].strip() != sale_date.strip():
                writer.writerow(sale)
            else:
                deleted = True
                logger.info(f"Deleted sale on date: {sale}")

    if not deleted:
        logger.error(f"Sale date '{sale_date}' not found.")
        raise ValueError(f"Sale date '{sale_date}' not found.")
    else:
        logger.info(f"Sale on date '{sale_date}' has been deleted successfully.")
        logger.debug(f"Current list of sales: {list_sales()}")


# Списък със служители
def list_employees():
    try:
        with open(EMPLOYEES_FILE, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            return [row for row in reader]
    except FileNotFoundError:
        logger.warning("Employees file not found.")
        return []


# Списък с автомобили
def list_cars():
    try:
        with open(CARS_FILE, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            return [row for row in reader]
    except FileNotFoundError:
        logger.warning("Cars file not found.")
        return []


# Списък с продажби
def list_sales():
    try:
        with open(SALES_FILE, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            return [row for row in reader]
    except FileNotFoundError:
        logger.warning("Sales file not found.")
        return []


# Инициализиране на CSV файловете при стартиране
initialize_files()
