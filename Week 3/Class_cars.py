import os
import csv

'''
Скрипт генерирует список объектов (в csv таблице), наследуемых от класса CarBase с различными атрибутами 
и методами, в зависимости от входящих данных 
'''


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)
        self.car_type = None

    def get_photo_file_ext(self):
        ext = os.path.splitext(self.photo_file_name)
        return ext[1]

    def __repr__(self):
        return self.brand


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)
        self.car_type = 'car'


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.body_whl = body_whl
        self.body_length = 0.0
        self.body_width = 0.0
        self.body_height = 0.0
        try:
            self.body_length, self.body_width, self.body_height = [float(i) for i in body_whl.split('x')]
        except ValueError:
            pass
        self.car_type = 'truck'

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra
        self.car_type = 'spec_machine'


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        for row in reader:

            if row[0] == 'car' and row[1] != '' and row[3] != '' and row[5] != '' and row[2] != '':
                car_list.append(Car(row[1], row[3], row[5], row[2]))
            elif row[0] == 'truck' and row[1] != '' and row[3] != '' and row[5] != '':
                car_list.append(Truck(row[1], row[3], row[5], row[4]))
            elif row[0] == 'spec_machine' and row[1] != '' and row[3] != '' and row[5] != '' and row[6] != '' \
                    and os.path.splitext(row[3])[1] != '':
                car_list.append(SpecMachine(row[1], row[3], row[5], row[6]))

    return car_list
