# Задание для сам. выполнения:
# Создать класс Airline: Пункт назначения, Номер рейса, Тип самолета, Время вылета, Дни недели.
# Создать список объектов. Вывести:
# a)    список рейсов для заданного пункта назначения;
# b)    список рейсов для заданного дня недели;.

class Airline:
    def __init__(self, destination, flight_number, airplane_type, departure_time, days_of_the_week):
        self.destination = destination
        self.flight_number = flight_number
        self.__airplane_type = airplane_type
        self.departure_time = departure_time
        self.__days_of_the_week = days_of_the_week

    def get_destination(self):
        return self.destination

    def get_flight_number(self):
        return self.flight_number

    def get_airplane_type(self):
        return self.__airplane_type

    def get_departure_time(self):
        return self.departure_time

    def get_days_of_the_week(self):
        return self.__days_of_the_week


def info(item):
    print('Пункт назначения:', All_airline[item].get_destination())
    print('Номер рейса:', All_airline[item].get_flight_number())
    print('Тип самолета', All_airline[item].get_airplane_type())
    print('Время вылета', All_airline[item].get_departure_time())
    print('Дни недели', All_airline[item].get_days_of_the_week())
    print('---------------')


All_airline = [Airline('Берлин', 245, 'A', '12:55', 'понедельник'),
               Airline('Варшава', 113, 'B', '00:15', 'вторник'),
               Airline('Москва', 657, 'C', '08:05', 'среда'),
               Airline('Новосибирск', 478, 'A', '11:00', 'четверг'),
               Airline('Санкт-Питербург', 325, 'A', '09:30', 'пятница'),
               Airline('Берлин', 982, 'C', '19:15', 'суббота'),
               Airline('Москва', 147, 'B', '22:10', 'воскресенье'),
               Airline('Берлин', 354, 'A', '17:15', 'понедельник'),
               Airline('Калининград', 783, 'C', '14:35', 'вторник'),
               Airline('Варшава', 328, 'C', '18:40', 'среда'),
               Airline('Санкт-Питербург', 456, 'A', '21:10', 'четверг'),
               Airline('Берлин', 224, 'B', '14:10', 'пятница')
               ]


def search_destination(d):
    for i in range(len(All_airline)):
        if All_airline[i].get_destination() == d:
            info(i)


def search_day(day):
    for i in range(len(All_airline)):
        if All_airline[i].get_days_of_the_week() == day:
            info(i)


des_search = input('Введите пункт назначения:\n')
search_destination(des_search)

day_search = input('Введите день недели:\n')
search_day(day_search)
