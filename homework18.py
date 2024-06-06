class Car:

    price = 1000000

    def __str__(self):
        return 'Авто: {} \nЦена: {}'.format(self.__class__.__name__, self.price)

    def horse_powers(self):
        print("Мощность: 350 л.с.")


class Nissan(Car):

    price = 1500000

    def horse_powers(self):
        print("Мощность: 400 л.с.\n")


class Kia(Car):
    price = 2000000

    def horse_powers(self):
        print("Мощность: 500 л.с.")


nissan = Nissan()
print(nissan)
nissan.horse_powers()
kia = Kia()
print(kia)
kia.horse_powers()