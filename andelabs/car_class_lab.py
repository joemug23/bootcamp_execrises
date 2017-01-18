class Car(object):
    def __init__(self, car_type='saloon', model='GM', name='General', speed=0):
        self.name = name
        self.model = model
        self.car_type = car_type
        self.speed = speed
        self.num_of_wheels = 4
        self.num_of_doors = 4

    def set_door_number(self):
        if self.model == 'Porshe' or self.model == 'Koenigsegg':
            self.num_of_doors = 2
        return self.num_of_doors

    def set_wheels_number(self):
        if self.car_type == 'trailer':
            self.num_of_wheels = 8
        return self.num_of_wheels

    def is_saloon(self):
        if self.car_type == 'trailer':
            self.car_type = 'trailer'
        return self.car_type

    def drive(self, speed):
        if self.car_type == 'trailer':
            self.speed == 77
        else:
            self.speed = 10 ** speed
        return self
