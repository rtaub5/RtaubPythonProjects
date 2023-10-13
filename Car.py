import random


class Car:
    def __init__(self, year, make, speed):
        self.__year = year
        self.__make = make
        self.__speed = speed

    def set_year(self, year):
        self.__year = year

    def set_make(self, make):
        self.__make = make

    def set_speed(self, speed):
        self.__speed = speed

    def get_year(self):
        return self.__year

    def get_make(self):
        return self.__make

    def get_speed(self):
        return self.__speed

    def __str__(self):
        print(self.__year)
        print(self.__make)
        print(self.__speed)

    def accelerate(self):
        # this function adds 5 to cars speed
        self.__speed = int(self.__speed) + 5
        return self.__speed

    def brake(self):
        # this function subtracts 5 from cars speed
        self.__speed = int(self.__speed) - 5
        return self.__speed


def main():
    car_one = Car('2012', 'Honda', '110')
    car_two = Car('2022', 'Acura', '130')
    # these are objects of car class
    print('year = ', car_one.get_year(), 'make = ', car_one.get_make(), 'speed = ', car_one.get_speed())
    print('year = ', car_two.get_year(), 'make = ', car_two.get_make(), 'speed = ', car_two.get_speed())
    acc_car_one = random.randint(1, 10)
    # acc_car_one will generate number between 1 and 10
    print('Car One accelerates', acc_car_one, 'times.')
    for num in range(acc_car_one):
        # for statement runs accelerate function for each number of times the car accelerates
        speed_one = car_one.accelerate()
    print('Speed for Car one after accelerating', acc_car_one, 'times is', speed_one)
    speed_one = car_one.brake()
    print('Speed for Car one after breaking once is', speed_one)
    acc_car_two = random.randint(1, 10)
    # acc_car_two will generate number between 1 and 10
    print('Car Two accelerates', acc_car_two, 'times.')
    for num in range(acc_car_two):
        speed_two = car_two.accelerate()
    print('Speed for Car 2 after accelerating', acc_car_two, 'times is', speed_two)
    speed_two = car_two.brake()
    print('Speed for Car two after breaking is', speed_two)
    if speed_one > speed_two:
        # if statement compares speed of two cars and prints which one is greater
        print('Car 1 has the greatest speed')
    else:
        print('Car 2 has the greatest speed')


main()
