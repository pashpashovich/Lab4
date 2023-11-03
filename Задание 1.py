class MyList:
    def __init__(self):
        self.data = []

    def add_element(self, item1):
        self.data.append(item1)

    def remove_element(self, item1):
        if item1 in self.data:
            self.data.remove(item1)
        else:
            print(f"Элемент {item1} не найден в списке(")

    def get_element_by_index(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        else:
            print("Такого индекса нет в списке")

    def get_list_length(self):
        return len(self.data)

    def print_list(self):
        print(self.data)


my_list = MyList()

while True:
    print("Выберите действие:\n1.Добавить один элемент в список.\n2.Удалить элемент из списка\n3.Получить элемент по индексу\n4.Получить длину списка\n5.Вывести список на экран\n6.Выйти из программы")
    while True:
        try:
            choice = int(input())
            if 0 < choice < 7:
                break
            else:
                print("Неверный ввод... Повторите попытку")
        except ValueError:
            print("Неверный ввод... Повторите попытку")
    if choice == 1:
        try:
            item = int(input("Введите элемент для добавления: "))
            my_list.add_element(item)
            print("Элемент ", item, " добавлен в список")
        except ValueError:
            print("Неверный ввод... Введите целое число")
    elif choice == 2:
        try:
            my_list.print_list()
            item = int(input("Введите элемент для удаления: "))
            my_list.remove_element(item)
        except ValueError:
            print("Неверный ввод... Введите целое число")
    elif choice == 3:
        try:
            index = int(input("Введите индекс: "))
            result = my_list.get_element_by_index(index)
            if result is not None:
                print("Элемент под индексом", index, " is ", result)
        except ValueError:
            print("Неверный ввод... Введите целое число")
    elif choice == 4:
        print("Размер списка ", my_list.get_list_length())
    elif choice == 5:
        my_list.print_list()
    elif choice == 6:
        break



