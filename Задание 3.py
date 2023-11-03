class Room:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def calculate_wall_area(self):
        return 2 * (self.length + self.width) * self.height

class Door:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = self.calculate_area()

    def calculate_area(self):
        return self.width * self.height

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = self.calculate_area()

    def calculate_area(self):
        return self.width * self.height

def calculate_wallpaper_area(room, doors, windows):
    total_wall_area = room.calculate_wall_area()

    for door in doors:
        total_wall_area -= door.area

    for window in windows:
        total_wall_area -= window.area

    return total_wall_area

room_length = float(input("Введите длину комнаты (в метрах): "))
room_width = float(input("Введите ширину комнаты (в метрах): "))
room_height = float(input("Введите высоту комнаты (в метрах): "))

door_count = int(input("Введите количество дверей: "))
doors = []
for _ in range(door_count):
    door_width = float(input("Введите ширину двери (в метрах): "))
    door_height = float(input("Введите высоту двери (в метрах): "))
    doors.append(Door(door_width, door_height))

window_count = int(input("Введите количество окон: "))
windows = []
for _ in range(window_count):
    window_width = float(input("Введите ширину окна (в метрах): "))
    window_height = float(input("Введите высоту окна (в метрах): "))
    windows.append(Window(window_width, window_height))

room = Room(room_length, room_width, room_height)
wallpaper_area = calculate_wallpaper_area(room, doors, windows)

if (wallpaper_area > 0):
    print(f"Общая площадь стен для оклейки обоями: {wallpaper_area:.2f} квадратных метров.")
else:
    print("Введённые данные нелогичны")
