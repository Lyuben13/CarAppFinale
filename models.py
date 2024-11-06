class Employee:
    def __init__(self, full_name, job_position, contact_number, email):
        self.full_name = full_name
        self.job_position = job_position
        self.contact_number = contact_number
        self.email = email


class Car:
    def __init__(self, manufacturer, year, model, cost_price, sale_price):
        self.manufacturer = manufacturer
        self.year = year
        self.model = model
        self.cost_price = cost_price
        self.sale_price = sale_price


class Sale:
    def __init__(self, employee, car, date_of_sale, actual_selling_price):
        self.employee = employee
        self.car = car
        self.date_of_sale = date_of_sale
        self.actual_selling_price = actual_selling_price
