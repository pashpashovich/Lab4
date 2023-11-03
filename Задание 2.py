class Transport:
    def __init__(self, name, speed, cost):
        self.name = name
        self.speed = speed
        self.cost = cost

    def travel_method(self):
        return "Обычное транспортное средство"

class Plane(Transport):
    def travel_method(self):
        return "Самолет"

class Train(Transport):
    def travel_method(self):
        return "Поезд"

class Car(Transport):
    def travel_method(self):
        return "Машина"

def fastest_trip(city_distance):
    fastest_trip = None
    min_time = float('inf')

    for transport in city_distance:
        time = city_distance[transport][0]
        if time < min_time:
            min_time = time
            fastest_trip = transport
    return fastest_trip

def most_economical_trip(city_distance):
    most_economical_trip = None
    min_cost = float('inf')

    for transport in city_distance:
        cost= city_distance[transport][1]
        if cost<min_cost:
            min_cost=cost
            most_economical_trip = transport
    return most_economical_trip

city_distance = {
    "Самолёт": (2, 1000),
    "Поезд": (5, 500),
    "Машина": (8, 300),
}

def write_to_file(city_distance, file_name):
    with open(file_name, "w") as file:
        file.write("Средства передвижения и расстояния:\n")
        for transport, (time, cost) in city_distance.items():
            file.write(f"{transport} - Время: {time} часов, Стоимость: {cost} рублей\n")


file_name = "transport_info.txt"
plane = Plane("Boeing", 900, 3000)
train = Train("Высокоскоростной поезд", 250, 1000)
car = Car("Nissan", 100, 500)

print("Самый быстрый транспорт:", fastest_trip(city_distance))
print("Самый экономичный транспорт:", most_economical_trip(city_distance))

while True:
    print("\nОпции:")
    print("1. Добавить средство передвижения")
    print("2. Найти самый быстрый путь")
    print("3. Найти самый экономичный путь")
    print("4. Записать данные в файл")
    print("5. Выйти")

    choice = input("Введите Ваш выбор: ")

    if choice == '1':
        name = input("Введите имя транспортного средства: ")
        speed = float(input("Введите скорость (км/ч): "))
        cost = float(input("Ввести стоимость: "))
        transport = Transport(name, speed, cost)
        city_distance[name] = (speed, cost)
        print(f"{name} был добавлен к транспортным методам")
    elif choice == '2':
        print("Самый быстрый путь:", fastest_trip(city_distance))
    elif choice == '3':
        print("Самый экономичный путь:", most_economical_trip(city_distance))
    elif choice == '4':
        write_to_file(city_distance, file_name)
        print(f"Информация была записана в файл '{file_name}'")
    elif choice == '5':
        break
    else:
        print("Неверный ввод. Введите значение (1-4)")
