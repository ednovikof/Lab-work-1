import doctest


class Script:
    def __init__(self, author: str, name: str, pages: int, last_read_page: int):

        self.author = author
        self.name = name
        self.pages = pages
        self.last_read_page = last_read_page

    def increment_last_read_page(self, read_pages: int):

        if not isinstance(read_pages, int):
            raise TypeError('Количество страниц должно быть типа int')
        if read_pages < 0:
            raise ValueError('Количество страниц должно быть положительным числом')
        if self.last_read_page + read_pages > self.pages:
            raise ValueError('Количество страниц превышает общее количество')

        self.last_read_page += read_pages

    def decrement_last_read_page(self, backwards_pages: int):

        if not isinstance(backwards_pages, int):
            raise TypeError('Количество страниц должно быть типа int')
        if backwards_pages < 0:
            raise ValueError('Количество страниц должно быть положительным числом')
        if self.last_read_page - backwards_pages < 0:
            raise ValueError('Окончательное количество страниц отрицательно')

        self.last_read_page -= backwards_pages


class Cat:
    def __init__(self, name: str, age: int, happy: bool, weight: int):

        self.name = name
        self.age = age
        self.happy = happy
        self.weight = weight

    def diet_routine(self, plan_weight: int):

        if not isinstance(plan_weight, int):
            raise TypeError('Плановый вес должен быть типа int')
        if plan_weight < 0:
            raise ValueError('Плановый вес должен быть неотрицательным числом')
        self.weight = plan_weight

    def feed_the_cat(self, added_weight: int):

        if not isinstance(added_weight, int):
            raise TypeError('Добавленный вес должен быть типа int')
        if added_weight < 0:
            raise ValueError('Добавленный вес должен быть неотрицательным числом')

        self.weight += added_weight


class Car:
    def __init__(self, model, year, speed=0):

        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self, amount):

        if not isinstance(amount, int):
            raise TypeError('Ускорение должно быть типа int')
        if amount < 0:
            raise ValueError('Ускорение должно быть неотрицательным числом')
        self.speed += amount

    def brake(self, amount):

        if not isinstance(amount, int):
            raise TypeError('Замедление должно быть типа int')
        if amount < 0:
            raise ValueError('Замедление должно быть неотрицательным числом')
        if self.speed - amount < 0:
            self.speed = 0
        else:
            self.speed -= amount


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
