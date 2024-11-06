from kivy.animation import Animation
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput

from operations import add_employee, add_car, add_sale, delete_employee, delete_car, delete_sale, list_employees, \
    list_cars, list_sales


# Главно меню
class MainMenu(Screen):
    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        # Бутон за добавяне на служител
        add_employee_button = Button(text='Add Employee',
                                     font_size=30,
                                     background_color=(3, 3, 3, 3),
                                     color=(0, 0, 0, 1))
        add_employee_button.bind(
            on_press=lambda instance: [animate_button_press(instance), self.go_to_add_employee(instance)])
        layout.add_widget(add_employee_button)

        # Бутон за добавяне на кола
        add_car_button = Button(text='Add Car',
                                font_size=30,
                                background_color=(3, 3, 3, 3),
                                color=(0, 0, 0, 1))
        add_car_button.bind(on_press=lambda instance: [animate_button_press(instance), self.go_to_add_car(instance)])
        layout.add_widget(add_car_button)

        # Бутон за добавяне на продажба
        add_sale_button = Button(text='Add Sale',
                                 font_size=30,
                                 background_color=(0, 1, 0, 1),
                                 color=(0, 0, 0, 1))
        add_sale_button.bind(on_press=lambda instance: [animate_button_press(instance), self.go_to_add_sale(instance)])
        layout.add_widget(add_sale_button)

        # Бутон за изброяване на служители
        list_employees_button = Button(text='List Employees',
                                       font_size=30,
                                       background_color=(0, 1, 0, 1),
                                       color=(0, 0, 0, 1))
        list_employees_button.bind(
            on_press=lambda instance: [animate_button_press(instance), self.go_to_list_employees(instance)])
        layout.add_widget(list_employees_button)

        # Бутон за изброяване на коли
        list_cars_button = Button(text='List Cars',
                                  font_size=30,
                                  background_color=(0, 1, 0, 1),
                                  color=(0, 0, 0, 1))
        list_cars_button.bind(
            on_press=lambda instance: [animate_button_press(instance), self.go_to_list_cars(instance)])
        layout.add_widget(list_cars_button)

        # Бутон за изброяване на продажби
        list_sales_button = Button(text='List Sales',
                                   font_size=30,
                                   background_color=(3, 0, 0, 8),
                                   color=(0, 0, 0, 1))
        list_sales_button.bind(
            on_press=lambda instance: [animate_button_press(instance), self.go_to_list_sales(instance)])
        layout.add_widget(list_sales_button)

        # Бутон за изтриване на записи
        delete_entry_button = Button(text='Delete Entry',
                                     font_size=30,
                                     background_color=(3, 0, 0, 8),
                                     color=(0, 0, 0, 1))
        delete_entry_button.bind(
            on_press=lambda instance: [animate_button_press(instance), self.go_to_delete_entry(instance)])
        layout.add_widget(delete_entry_button)

        self.add_widget(layout)

        def animate_button_press(button_instance):
            animation = Animation(size=(button_instance.width * 0.9, button_instance.height * 0.9), duration=5.1)
            animation += Animation(size=(button_instance.width, button_instance.height), duration=5.1)
            animation.start(button_instance)

    def go_to_add_employee(self, instance):
        self.manager.current = 'add_employee'

    def go_to_add_car(self, instance):
        self.manager.current = 'add_car'

    def go_to_add_sale(self, instance):
        self.manager.current = 'add_sale'

    def go_to_list_employees(self, instance):
        self.manager.current = 'list_employees'

    def go_to_list_cars(self, instance):
        self.manager.current = 'list_cars'

    def go_to_list_sales(self, instance):
        self.manager.current = 'list_sales'

    def go_to_delete_entry(self, instance):
        self.manager.current = 'delete_entry'


# Екран за добавяне на служител
class AddEmployee(Screen):
    def __init__(self, **kwargs):
        super(AddEmployee, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        # Име
        self.name_input = TextInput(hint_text='Name')
        layout.add_widget(self.name_input)

        # Позиция
        self.position_input = TextInput(hint_text='Position')
        layout.add_widget(self.position_input)

        # Телефонен номер
        self.contact_number_input = TextInput(hint_text='Contact Number')
        layout.add_widget(self.contact_number_input)

        # Имейл
        self.email_input = TextInput(hint_text='Email')
        layout.add_widget(self.email_input)

        # Бутон за добавяне на служител
        add_employee_button = Button(text='Add Employee')
        add_employee_button.bind(on_press=self.add_employee_handler)
        layout.add_widget(add_employee_button)

        # Бутон назад
        back_button = Button(text='Back')
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        def animate_button_press(button_instance):
            animation = Animation(size=(button_instance.width * 0.9, button_instance.height * 0.9), duration=0.1)
            animation += Animation(size=(button_instance.width, button_instance.height), duration=0.1)
            animation.start(button_instance)

        self.add_widget(layout)

    def add_employee_handler(self, instance):
        name = self.name_input.text
        position = self.position_input.text
        contact_number = self.contact_number_input.text
        email = self.email_input.text

        if name and position and contact_number and email:
            try:
                add_employee(name, position, contact_number, email)
                self.show_popup(f"Added employee: {name} with position: {position}, "
                                f"contact number: {contact_number}, email: {email}")
                self.clear_inputs()
            except ValueError as e:
                self.show_popup(str(e))  # Покажи грешка за невалиден имейл
        else:
            self.show_popup("Please fill in all fields.")

    def clear_inputs(self):
        self.name_input.text = ''
        self.position_input.text = ''
        self.contact_number_input.text = ''
        self.email_input.text = ''

    def go_back(self, instance):
        self.manager.current = 'main_menu'

    def show_popup(self, message):  # noqa
        """Създайте етикет с определен размер на текста, за да обвиете текста"""  # noqa
        message_label = Label(text=message, size_hint_y=None)
        message_label.bind(size=message_label.setter('text_size'))

        popup = Popup(title='Message',
                      content=message_label,
                      size_hint=(0.9, None),
                      height=120)

        popup.open()


# Екран за добавяне на кола
class AddCar(Screen):
    def __init__(self, **kwargs):
        super(AddCar, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        # Производство въвеждане.
        self.make_input = TextInput(hint_text='Make')
        layout.add_widget(self.make_input)

        # Модел на автомобил входни данни.
        self.model_input = TextInput(hint_text='Model')
        layout.add_widget(self.model_input)

        # Година въвеждане
        self.year_input = TextInput(hint_text='Year')
        layout.add_widget(self.year_input)

        # Цена на автомобила.
        self.cost_price_input = TextInput(hint_text='Cost Price')
        layout.add_widget(self.cost_price_input)

        # Продажба въвеждане
        self.sale_price_input = TextInput(hint_text='Sale Price')
        layout.add_widget(self.sale_price_input)

        # Добави кола бутон.
        add_button = Button(text='Add Car')
        add_button.bind(on_press=self.add_car)
        layout.add_widget(add_button)

        # Бутон назад
        back_button = Button(text='Back')
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def add_car(self, instance):
        make = self.make_input.text
        model = self.model_input.text
        year = self.year_input.text
        cost_price = self.cost_price_input.text
        sale_price = self.sale_price_input.text

        # Добавяне на кола.
        add_car(make, model, year, cost_price, sale_price)

        # Clear input fields
        self.make_input.text = ''
        self.model_input.text = ''
        self.year_input.text = ''
        self.cost_price_input.text = ''
        self.sale_price_input.text = ''

    def go_back(self, instance):
        self.manager.current = 'main_menu'


# Екран за добавяне на продажба
class AddSale(Screen):
    def __init__(self, **kwargs):
        super(AddSale, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        # Служител име
        self.employee_name_input = TextInput(hint_text='Employee Name')
        layout.add_widget(self.employee_name_input)

        # Модел кола
        self.car_model_input = TextInput(hint_text='Car Model')
        layout.add_widget(self.car_model_input)

        # Дата на продажба
        self.sale_date_input = TextInput(hint_text='Sale Date')
        layout.add_widget(self.sale_date_input)

        # Актуална цена
        self.actual_selling_price_input = TextInput(hint_text='Actual Selling Price')
        layout.add_widget(self.actual_selling_price_input)

        # добави продажба бутон.
        add_button = Button(text='Add Sale')
        add_button.bind(on_press=self.add_sale)
        layout.add_widget(add_button)

        # бутон за връщане назад
        back_button = Button(text='Back')
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def add_sale(self, instance):
        employee_name = self.employee_name_input.text
        car_model = self.car_model_input.text
        sale_date = self.sale_date_input.text
        actual_selling_price = self.actual_selling_price_input.text

        add_sale(employee_name, car_model, sale_date, actual_selling_price)

        self.employee_name_input.text = ''
        self.car_model_input.text = ''
        self.sale_date_input.text = ''
        self.actual_selling_price_input.text = ''

    def go_back(self, instance):
        self.manager.current = 'main_menu'


# Екран за изброяване на служители
class ListEmployees(Screen):
    def __init__(self, **kwargs):
        super(ListEmployees, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        self.employees_label = Label(text='Employee List:')
        layout.add_widget(self.employees_label)

        self.update_employee_list()

        back_button = Button(text='Back')
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def update_employee_list(self):
        employees = list_employees()
        self.employees_label.text = 'Employee List:\n' + '\n'.join([' - '.join(emp) for emp in employees])

    def go_back(self, instance):
        self.manager.current = 'main_menu'


# Екран за изброяване на коли
class ListCars(Screen):
    def __init__(self, **kwargs):
        super(ListCars, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        self.cars_label = Label(text='Car List:')
        layout.add_widget(self.cars_label)

        self.update_car_list()

        back_button = Button(text='Back')
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def update_car_list(self):
        cars = list_cars()
        self.cars_label.text = 'Car List:\n' + '\n'.join([' - '.join(car) for car in cars])

    def go_back(self, instance):
        self.manager.current = 'main_menu'


# Екран за изброяване на продажби
class ListSales(Screen):
    def __init__(self, **kwargs):
        super(ListSales, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        self.sales_label = Label(text='Sales List:')
        layout.add_widget(self.sales_label)

        self.update_sales_list()

        back_button = Button(text='Back')
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def update_sales_list(self):
        sales = list_sales()
        self.sales_label.text = 'Sales List:\n' + '\n'.join([' - '.join(sale) for sale in sales])

    def go_back(self, instance):
        self.manager.current = 'main_menu'


# Екран за изтриване на записи
class DeleteEntry(Screen):
    def __init__(self, **kwargs):
        super(DeleteEntry, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        # Изтриване на служител
        self.employee_name_input = TextInput(hint_text='Employee Name')
        layout.add_widget(self.employee_name_input)

        delete_employee_button = Button(text='Delete Employee')
        delete_employee_button.bind(on_press=self.delete_employee)
        layout.add_widget(delete_employee_button)

        # Изтриване на кола.
        self.car_model_input = TextInput(hint_text='Car Model')
        layout.add_widget(self.car_model_input)

        delete_car_button = Button(text='Delete Car')
        delete_car_button.bind(on_press=self.delete_car)
        layout.add_widget(delete_car_button)

        # Изтриване на продажба.
        self.sale_details_input = TextInput(hint_text='Sale Details (Sale Date)')
        layout.add_widget(self.sale_details_input)

        delete_sale_button = Button(text='Delete Sale')
        delete_sale_button.bind(on_press=self.delete_sale)
        layout.add_widget(delete_sale_button)

        back_button = Button(text='Back')
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def delete_employee(self, instance):
        employee_name = self.employee_name_input.text
        if employee_name:
            try:
                delete_employee(employee_name)  # Използвайте име за изтриване.
                self.employee_name_input.text = ''
                self.show_popup(f"Deleted employee: {employee_name}")
            except Exception as e:
                self.show_popup(str(e))
        else:
            self.show_popup("Please enter an employee name.")

    def delete_car(self, instance):
        car_model = self.car_model_input.text
        if car_model:  # Validate input
            try:
                delete_car(car_model)  # Използвайте модел/кола за изтриване.
                self.car_model_input.text = ''
                self.show_popup(f"Deleted car: {car_model}")
            except Exception as e:
                self.show_popup(str(e))
        else:
            self.show_popup("Please enter a car model.")

    def delete_sale(self, instance):
        sale_details = self.sale_details_input.text
        if sale_details:
            try:
                delete_sale(sale_details)
                self.sale_details_input.text = ''
                self.show_popup(f"Deleted sale: {sale_details}")
            except Exception as e:
                self.show_popup(str(e))
        else:
            self.show_popup("Please enter sale details.")

    def go_back(self, instance):
        self.manager.current = 'main_menu'

    def show_popup(self, message):  # noqa
        popup = Popup(title='Message', content=Label(text=message), size_hint=(0.8, 0.4))
        popup.open()


# Основно Kivy приложение
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainMenu(name='main_menu'))
        sm.add_widget(AddEmployee(name='add_employee'))
        sm.add_widget(AddCar(name='add_car'))
        sm.add_widget(AddSale(name='add_sale'))
        sm.add_widget(ListEmployees(name='list_employees'))
        sm.add_widget(ListCars(name='list_cars'))
        sm.add_widget(ListSales(name='list_sales'))
        sm.add_widget(DeleteEntry(name='delete_entry'))
        return sm


if __name__ == '__main__':
    MyApp().run()
