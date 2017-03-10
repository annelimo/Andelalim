class Car(object):
    num_wheels = 4
    gas = 30
    headlights = 4
    size = 'medium'

    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.color = 'No color yet. do painting.'
        self.wheels = Car.num_wheels
        self.gas = Car.gas

    def paint(self, color):
        self.color = color
        return self.make + ' ' + self.model + ' current ' + color

    def drive(self):
        if self.wheels < Car.num_wheels or self.gas <= 0:
            return self.make + ' ' + self.model + ' not moving!'
        self.gas -= 10
        return self.make + ' ' + self.model + ' gotten!'

    def pop_tire(self):
        if self.wheels > 0:
            self.wheels -= 1

    def fill_gas(self):
        self.gas += 30
        print('The car should not be empty.')

class Ford(Car):
    size = 'Ford'

    def rev(self):
        print('For hire for any promotion!')

    def drive(self):
        self.rev()
        return Car.drive(self)