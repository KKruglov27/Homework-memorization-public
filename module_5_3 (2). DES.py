class House:
    """Название дома, номера этажей"""
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        """Переход к этажу, перечисление этажей"""
        if new_floor > self.number_of_floors:
            print('Ошибка. Объект:', '"' + self.name + '"' ':', '-', 'Такого этажа не существует.')
        else:
            for floor in range(1, new_floor + 1):
                print(floor)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    # 1. Для сравнения количества этажей предусмотреть действие, если other является числом или объектом класса House:

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other

    # 2. Предусмотреть действие, когда value(other) является числом или объектом класса House:

    def __add__(self, value):       # h1 = h1 + 10 или h1 = h1 + h2
        if isinstance(value, int):
            self.number_of_floors += value
        elif isinstance(value, House):
            self.number_of_floors += value.number_of_floors
        return self

    # 3. Методы __iadd__  и __radd__ не обязательно описывать заново, достаточно вернуть значение вызова __add__:

    def __iadd__(self, other: int):
        return self.__add__(other)
    # h1 += 10 (метод вызывается, когда используется оператор +=)

    def __radd__(self, other):
        return self.__add__(other)
    # (метод вызывается, когда объект находится справа от оператора +,
    # и левый операнд не поддерживает операцию сложения с ним)

    # 4. Метод __lt__ : этот метод определяет поведение оператора "меньше чем" <.
    # Он сравнивает текущий объект с другим объектом:
    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other

    # 5. Метод __le__: метод определяет поведение оператора "меньше или равно" <=. Он использует методы __eq__ и __lt__
    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)

    # 6. Метод __gt__: определяет поведение оператора "больше чем" >. Он использует метод __le__. Метод возвращает True,
    # если текущий объект не меньше или равен other (используя __le__), что эквивалентно тому, что он больше.
    def __gt__(self, other):
        return not self.__le__(other)

    # 7. Метод __ge__: Этот метод определяет поведение оператора "больше или равно" >=.
    # Он использует метод __lt__. Метод возвращает True, если текущий объект не меньше
    # other (используя __lt__), что эквивалентно тому, что он больше или равен.

    def __ge__(self, other):
        return not self.__lt__(other)

    # 8. Метод __ne__: Этот метод определяет поведение оператора "не равен" (!=) для объектов класса.
    # Он использует метод __eq__, который отвечает за проверку на равенство (==):

    def __ne__(self, other):
        return not self.__eq__(other)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)


print(h1)
print(h2)

print(h1 == h2)

h1 = h1 + 10
print(h1)
print(h1 == h2)

h1 += 10
print(h1)

h2 = 10 + h2
print(h2)

print(h1 > h2)
print(h1 >= h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 != h2)
