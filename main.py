# db_is_available = False
# print(db_is_available)
# print(type(db_is_available))

# db_is_available = True
# print(db_is_available)


# print(bool(10))
# print(bool("abc"))
# print(bool([]))
# print(bool([1, 3, 5]))
# print(bool(None))


# print(100 < 1000)
# print("Long string " > "Short string")
# print(5 == 5)


# int = 3.14
# float = 5

# print(float + int)

# bool = 5
# int = True


# int_num = 70
# str_val = ' STR NUM '

# # print(int_num * str_val)

# print(int_num.__mul__(str_val))  # NotImplemented

# print(str_val.__rmul__(int_num))


# ratings = [2.5, 3.0, 4.5, 5.0]

# print(min(ratings))
# print(max(ratings))
# print(sum(ratings))

# print(sum(ratings) / len(ratings))


# my = [1, 2, 3]
# your = [4, 5, 6]

# all_us = my + your
# print(all_us)


# my_cars = ['BMW', 'Audi']

# # copied_cars = my_cars.copy()
# copied_cars = list(my_cars)

# my_cars.append('Toyota')
# print(sorted(my_cars))


# my_nums = [10, 20, 30, 30, 50, 100]

# other_nums = list(my_nums)

# my_nums.append(200)
# other_nums.clear()

# print(id(my_nums))
# print(id(other_nums))

# print(my_nums, other_nums)


# my_nums = [10, 20, 30, 30, 50, 100]

# other_nums = len(my_nums)
# print(other_nums)


# D/Z:
# 1)
# my_list = [67, "Hello Friend", 3.14, False, [1, 2, 3]]
# del my_list[3]
# print(len(my_list))
# rev_list = my_list.reverse()

# sec_list = [1, True]
# both_list = my_list + sec_list
# print(both_list)
# print(len(both_list))


# 2)
# first_list = [1, 2, 3]
# second_list = [4, 5, 6]
# both_list = first_list + second_list
# #      or
# both_list = first_list.__add__(second_list)
# print(both_list)


# Slovniki(Dictionaries(dict))

# my_motorbike = {
#     "brand": "Honda",
#     "price": "2000",
#     "year": 2020,
#     "color": "red",
# }

# my_motorbike["price"] = 7000
# print(my_motorbike)


# my_motorbike = {
#     "brand": "Honda",
#     "price": "2000",
#     "year": 2020,
#     "color": "red",
# }

# my_motorbike["is_new"] = True
# print(my_motorbike)


# my_motorbike = {
#     "brand": "Honda",
#     "price": "2000",
#     "year": 2020,
#     "color": "red",
# }

# del my_motorbike["color"]
# print(my_motorbike)


# my_motorbike = {
#     "brand": "Honda",
#     "price": "2000",
#     "price_info": {
#         "currency": "USD",
#         "discount": 0.1,
#     },
#     "year": 2020,
#     "color": "red",
# }

# print(my_motorbike["price_info"]["currency"])
# print(my_motorbike["price_info"]["discount"])

# brand = "Honda"
# bike_price = "2000"
# year = 2026

# my_motorbike = {
#     "brand": brand,
#     "price": bike_price,
#     "year": year,
# }

# print(my_motorbike)


# brand = "Honda"
# bike_price = "2000"
# year = 2026

# my_motorbike = {
#     "brand": brand,
#     "price": bike_price,
#     "year": year,
# }

# print(len(my_motorbike))


# my_motorbike = {
#     "brand": "Honda",
#     "price": "2000",
#     "year": 2020,
# }

# print(my_motorbike.get("brand"))
# print(my_motorbike.get("year"))
# print(my_motorbike.get("model", "Model not found"))


# my_dict = {}
# print(my_dict.__doc__)


# my_disk = {}

# print(id(my_disk))
# print(type(my_disk))

# my_disk["brand"] = "Seagate"
# my_disk["capacity"] = "1TB"

# print(my_disk)
# print(id(my_disk))


# print(my_disk.__doc__)
# print(my_disk.items())
# print(list(my_disk.keys()))
# print(my_disk.popitem()) - better dont use it, because it removes the last item from the dictionary and returns it as a tuple. If the dictionary is empty, it raises a KeyError.

# print(my_disk.get("type"))

# new_disk = my_disk.copy()
# print(new_disk)


# my_list = [0, True, "abc"]
# my_dict = dict(my_list)
# print(my_dict)


# user_data = {}

# # 2. Запускаємо цикл на 3 ітерації
# for i in range(3):
#     print(f"--- Запис №{i+1} ---")

#     # Запитуємо назву ключа
#     key_name = input("Введіть назву ключа: ")

#     # Запитуємо значення для цього ключа
#     key_value = input(f"Введіть значення для '{key_name}': ")

#     # Додаємо в словник
#     user_data[key_name] = key_value

# # 3. Виводимо результат
# print("\nОсь що вийшло:")
# print(user_data)


# Кортежі(Tuples(tuple)):

# my_fruits = ("apple", "banana", "cherry")

# posts_ids = (101, 102, 103)

# user_input = (True, "Doe", 30)


# my_fruits = ("apple", "banana", "cherry")
# other_fruits = ("banana", "apple", "cherry")
# # False, because the order of elements is different
# print(my_fruits == other_fruits)


# posts_ids = (101, 102, 103)

# print(posts_ids[0])  # 101
# print(posts_ids[1])  # 102

# print(posts_ids[-1])  # 103


# posts_ids = (101, 102, 103)

# print(type(posts_ids))  # <class 'tuple'>
# # TypeError: 'tuple' object does not support item assignment
# posts_ids[0] = 100


# posts_ids = (101, 102, 103)

# print(type(posts_ids))  # <class 'tuple'>
# TypeError: 'tuple' object does not support item assignment
# del posts_ids[0]


# my_fruit = "apple"
# other_fruit = "banana"
# new_fruit = "cherry"

# all_fruits = (my_fruit, other_fruit, new_fruit)
# print(all_fruits)


# posts_ids = (101, 102, 103, 568)

# print(posts_ids[10])  # IndexError: tuple index out of range


# Tuples(Count and Index):

# posts_ids = (101, 102, 103, 568, 102)\

# print(posts_ids.count(102))  # 2
# print(posts_ids.count(568))  # 3


# posts_ids = (101, 102, 103, 568, 102)

# print(posts_ids.index(102))  # 1
# print(posts_ids.index(568))  # 3


# my_nums = (10, 20, 30, 30, 50, 100)

# my_list = list(my_nums)

# my_list.append(200)

# my_nums = tuple(my_list)

# print(my_nums)


# Наборы - set

# my_set = {1, 2, 3, 4, 5}#Набор - это неупорядоченная коллекция уникальных элементов. Он не поддерживает индексирование и не гарантирует порядок элементов. Наборы полезны для хранения уникальных значений и выполнения операций над множествами, таких как объединение, пересечение и разность.

# print(type(my_set))


# posts_ids = [101, 102, 103, 568]

# print(type(posts_ids.__getitem__(0)))  #p <class 'int'>
# print(posts_ids.__getitem__(0))  # 101


# my_set = {(1, 2, 3), 2, 5, 5}
# # print(my_set)  # {1, 2, 3, 5}
# # print(len(my_set))  # 4

# # del my_set[0]  # TypeError: 'set' object does not support item deletion

# print(my_set)


# my_set = set()  # Создание пустого набора

# print(my_set)  # {}
# print(type(my_set))  # <class 'set'> - это набор


# photo_sizes = {"1920x1080", "1280x720"}

# photo_sizes.add("3840x2160") # Добавляем новый элемент в набор
# print(photo_sizes)  # {'1920x1080', '1280x720', '3840x2160'}


# photo_sizes = {"1920x1080", "1280x720"}
# other_sizes = {"1280x720", "3840x2160"}

# all_sizes = photo_sizes.union(other_sizes)  # Объединение двух наборов
# print(all_sizes)  # {'1920x1080', '1280x720', '3840x2160'}


# photo_sizes = {"1920x1080", "1280x720"}
# other_sizes = {"1280x720", "3840x2160"}

# all_sizes = photo_sizes.intersection(other_sizes)  # Пересечение двух наборов
# print(all_sizes)  # {'1280x720'}


# my_set = {"abc", "def", "ghi", "f"}
# other_set = {"def", "f", "xyz"}

# print(my_set.intersection(other_set))  # Разность двух наборов
# print(other_set.intersection(my_set))  # Разность двух наборов
# print(my_set.intersection(["abc", "f"]))  # Разность набора и списка


# intersection == &
# union == |
# difference == -
# symmetric_difference == ^


# my_set = {"abc", "def", "ghi", "f"}
# other_set = {"def", "f", "xyz"}

# # Удаляет элемент "abc" из набора my_set. Если элемента нет, вызывает KeyError.
# my_set.remove("abc")
# print(my_set)  # {'def', 'ghi', 'f'}


# my_set = {"abc", "def", "ghi", "f"}

# copied_set = my_set.copy()  # Создает поверхностную копию набора my_set

# my_set.add("xyz")  # Добавляет элемент "xyz" в набор my_set
# copied_set.add("fake")  # Добавляет элемент "fake" в набор copied_set

# print(my_set & copied_set)  # {'abc', 'def', 'ghi', 'f'}

# print(my_set)  # {'abc', 'def', 'ghi', 'f', '
# print(copied_set)  # {'abc', 'def', 'ghi', 'f', 'fake'}


# a = {"abc", "def", "i", "f"}
# b = {"abc", "def", "g", "f"}


# # {'i', 'g'} - симметрическая разность двух наборов a и b, которая содержит элементы, которые присутствуют в одном из наборов, но не в обоих. В данном случае, элементы "i" и "g" присутствуют только в одном из наборов, поэтому они включены в результат.
# print(a.symmetric_difference(b))


# a = {1, 4, 6, 7}
# a.add(10)

# b = {4, 7, 3, 8, 2}


# # Находит общие элементы между наборами a и b
# common_elements = a.intersection(b)

# result_list = list(common_elements)  # Преобразует результат в список
# print(result_list)  # Выводит список общих элементов


# Range(Диапазон(range)):

# my_range = range(5)  # Создает диапазон от 0 до 4
# print(my_range)  # range(0, 5)
# print(type(my_range))  # <class 'range'>

# my_range = range(10, 20, 3)  # Создает диапазон от 10 до 19 с шагом 3
# print(my_range)  # range(10, 20, 3)
# print(list(my_range))  # [10, 13, 16, 19]


# my_range = range(10, 20, 3)

# for i in my_range:
#     print(i)  # Выводит числа 10, 13, 16, 19


# my_range = range(5)

# # print(my_range)
# # print(type(my_range))
# # print(my_range[-1])  # [0, 1, 2, 3, 4]

# for i in my_range:
#     print(i)  # Выводит числа 0, 1, 2, 3, 4


# for i in range(1, 10, 2):
#     print(i)  # Выводит числа 1, 3, 5, 7, 9


# # Выводит числа от 10 до 1 в обратном порядке
# print(list(range(10, 0, -1)))
# # Выводит числа от 10 до 1 в обратном порядке в виде кортежа
# print(tuple(range(10, 0, -1)))
# # Выводит числа от 10 до 1 в обратном порядке в виде набора
# print(set(range(10, 0, -1)))
# # Выводит числа от 10 до 1 в обратном порядке в виде словаря, где ключами являются индексы, а значениями - числа из диапазона
# print(dict(enumerate(range(10, 0, -1))))


# my_range = range(10, 20, 3)

# print(my_range.start) # 10
# print(my_range.stop) # 20
# print(my_range.step) # 3


# my_range = range(10, 30, 3)

# # print(my_range.index(19))  # 3
# # print(my_range.index(29))  # 6

# print(my_range.count(10))  # 1
# print(my_range.count(11))  # 0


# D/Z:
# my_range = range(1, 10, 2)

# mu_dict = []

# for i in my_range:
#     mu_dict.append(i)

# print(mu_dict)  # [1, 3, 5, 7, 9]


# list,dict,set,tuple,range,str - это встроенные типы данных в Python, которые представляют собой коллекции элементов. Они имеют свои особенности и предназначены для различных целей.

# - list (список) - это изменяемая упорядоченная коллекция элементов, которая может содержать дубликаты. Списки поддерживают индексирование и позволяют изменять свои элементы.
# - dict (словарь) - это изменяемая неупорядоченная коллекция пар "ключ-значение". Словари позволяют быстро получать доступ к значениям по ключу и поддерживают уникальные ключи.
# - set (набор) - это изменяемая неупорядоченная коллекция уникальных элементов. Наборы поддерживают операции над множествами, такие как объединение, пересечение и разность.
# - tuple (кортеж) - это неизменяемая упорядоченная коллекция элементов, которая может содержать дубликаты. Кортежи поддерживают индексирование, но не позволяют изменять свои элементы.
# - range (диапазон) - это неизменяемая последовательность чисел, которая используется для генерации последовательностей чисел в циклах и других конструкциях. Диапазоны поддерживают индексирование и позволяют задавать начальное значение, конечное значение и шаг.
# - str (строка) - это неизменяемая последовательность символов, которая используется для хранения текстовых данных. Строки поддерживают индексирование и позволяют выполнять различные операции над


# Встроенная функция zip

# fruits = ["apple", "banana", "cherry"]
# prices = [1.5, 0.5, 2.0]
# fruit_prices = zip(fruits, prices)
# print(fruit_prices)  # <zip object at 0x7f8b8c8c8c8c>

# print(type(fruit_prices))  # <class 'zip'>

# fruit_prices_list = dict(fruit_prices)
# # [('apple', 1.5, True), ('banana', 0.5, True), ('cherry', 2.0, False)]
# print(fruit_prices_list)


# #D\Z:
# tovar = ["smartphone", "laptop", "tablet"]
# prices = [1000, 1500, 500]
# tovar_prices = zip(tovar, prices)
# tovar_prices_dict = dict(tovar_prices)
# print(tovar_prices_dict)  # {'smartphone': 1000, 'laptop': 1500, 'tablet': 500}


# ID

# first_num = 10
# second_num = first_num

# print(id(first_num))  # 140737488355328
# print(id(second_num))  # 140737488355328

# second_num += 5
# print(second_num)  # 15
# print(first_num)  # 10

# print(id(first_num))  # 140737488355328
# print(id(second_num))  # 140737488355360


# info = {
#     "name": "John",
#     "age": 30,
#     "city": [],
# }

# info_copy = info.copy()
# info_copy["city"].append("New York")

# print(info)  # {'name': 'John', 'age': 30, 'city': ['New York']}
# print(info_copy)  # {'name': 'John', 'age': 30, '


# deepcopy - это функция из модуля copy, которая создает глубокую копию объекта. В отличие от поверхностной копии, которая создает новый объект, но сохраняет ссылки на вложенные объекты, глубокая копия создает новый объект и рекурсивно копирует все вложенные объекты. Это означает, что изменения в глубокой копии не будут влиять на оригинальный объект и наоборот.


# Функции - это блоки кода, которые выполняют определенную задачу и могут быть вызваны по имени. Функции позволяют организовать код, повторно использовать его и улучшать читаемость. В Python функции определяются с помощью ключевого слова def, за которым следует имя функции и круглые скобки с параметрами (если есть). Тело функции должно быть отступлено. Функции могут возвращать значения с помощью оператора return.


# def sum(a, b):
#     c = a + b
#     print(c)


# a = 5
# b = 2

# sum(a, b)  # 7

# a = 10
# b = 1

# sum(a, b)  # 11


# def sum(a, b):
#     c = a + b
#     print(c)


# print(type(sum))  # <class 'function'>


# Из чего состоит функция: - это определение функции, которое начинается с ключевого слова def, за которым следует имя функции и круглые скобки с параметрами (если есть). Тело функции должно быть отступлено. Функция может содержать инструкции, которые выполняют определенные действия, и может возвращать значение с помощью оператора return.
# def function_name(parameters):
#     """docstring"""
#     # body of the function
#     return value


# def my_fn():
#     pass


# print(my_fn())  # None


# def my_fn(a, b):
#     a = a + 1
#     c = a + b
#     return c


# num_one = 10
# num_two = 5

# res = my_fn(num_one, num_two)
# print(res)  # 16
# print(num_one)  # 10


# def increase_person_age(person):
#     person["age"] += 1
#     return person


# person_one = {
#     "name": "Alice",
#     "age": 21,
# }

# new_person = increase_person_age(person_one)
# print(new_person["age"])  # 22
# print(person_one["age"])  # 22


# D\Z:

# def merge_lists_to_dict(a, b):
#     return dict(zip(a, b))


# result = merge_lists_to_dict(["m", "y"], [1, 2, 3, 4, 5])  # {'m': 1, 'y': 2}
# print(result)

# res_two = merge_lists_to_dict(["abc"], [1, 2, 3])  # {'abc': 1}
# print(res_two)

# res_two = merge_lists_to_dict(["abc"], [1, 2, 3])  # {'abc': 1}
# print(res_two)


# Ошибки аргументов:
# def my_fn(a, b):
#     return a + b

# print(my_fn(10))  # TypeError: my_fn() missing 1 required positional argument: 'b'


# def my_fn(a, b):
#     return a + b

# print(my_fn(10, 20, 30))  # TypeError: my_fn() takes 2 positional arguments but 3 were given


# *args - это синтаксис в Python, который позволяет функции принимать переменное количество позиционных аргументов. Когда функция определена с *args, она может принимать любое количество аргументов, которые будут упакованы в кортеж. Внутри функции *args можно использовать как обычный кортеж, обращаясь к его элементам по индексу или используя функции, такие как len() и sum().


# def sum_nums(*args):
#     print(args)  # (10, 20, 30)
#     print(type(args))  # <class 'tuple'>

#     print(args[0])  # 10
#     return sum(args)


# print(sum_nums(10, 20, 30))  # 60


# def get_posts_info(name, posts_qty):
#     info = f"{name} has {posts_qty} posts."
#     return info


# print(get_posts_info("Alice", 5))  # Alice has 5 posts.


# def get_posts_info(name, posts_qty):
#     info = f"{name} has {posts_qty} posts."
#     return info


# print(get_posts_info(name="Alice", posts_qty=5))  # Alice has 5 posts.


# def get_posts_info(**person):
#     info = f"{person['name']} has {person['posts_qty']} posts."
#     return info


# print(get_posts_info(name="Alice", posts_qty=5))  # Alice has 5 posts.


# def get_posts_info(**person):
#     print(person)  # {'name': 'Alice', 'posts_qty': 5}
#     info = f"{person['name']} has {person['posts_qty']} posts."
#     return info


# # Alice has 5 posts.
# print(get_posts_info(name="Alice", posts_qty=5))


# D\Z:


# def merge_lists_to_dict(list_a, list_b):
#     return dict(zip(list_a, list_b))


# result = merge_lists_to_dict(["m", "y"], [1, 2, 3, 4, 5])  # {'m': 1, 'y': 2}
# print(result)

# res_two = merge_lists_to_dict(["abc"], [1, 2, 3])  # {'abc': 1}
# print(res_two)

# res_three = merge_lists_to_dict(
#     list_a=[3, 2, 1], list_b=[1, 2, 3])  # {3: 1, 2: 2, 1: 3}
# print(res_three)


# def update_car_info(**car):
#     car["is_available"] = True
#     return car


# my_car = update_car_info(brand="Toyota", model="Camry", price=20000)
# print(my_car)  # {'brand': 'Toyota', 'model': 'Camry',


# def mult_by_factor(value, multiplier=1):
#     return value * multiplier


# print(mult_by_factor(10, 2))  # 20
# print(mult_by_factor(5))  # 10


# from datetime import date


# def get_weekly():
#     return date.today().strftime("%A")


# def create_new_post(post, weekly=get_weekly()):
#     post_copy = post.copy()
#     post_copy["created_on_weekday"] = weekly
#     return post_copy


# initial_post = {
#     "id": 243,
#     "author": "Bogdan"
# }

# post_with_weekday = create_new_post(initial_post)
# # {'id': 243, 'author': 'Bogdan', 'created_on_weekday': 'Monday'}
# print(post_with_weekday)


# #date.today().strftime("%A") - найти документацию по этому методу и объяснить, что он делает.


# Callback функции - это функции, которые передаются в другую функцию в качестве аргумента и вызываются внутри этой функции для выполнения определенной задачи. Они позволяют создавать более гибкие и расширяемые программы, так как позволяют пользователю определять, что должно происходить при определенных событиях или условиях. Callback функции часто используются в асинхронном программировании, обработке событий и при работе с API.


# def other_fn():
#     print("Hello from other_fn!")
#     pass


# def fn_with_callback(callback_fn):
#     callback_fn()


# fn_with_callback(other_fn)  # Hello from other_fn!


# def print_num_info(num):
#     if (num % 2) == 0:
#         print("Entered number is even!")
#     else:
#         print("Entered number is odd!")


# def print_square(num):
#     print(f"The square of the entered number is: {num * num}")


# def process_number(num, callback_fn):
#     callback_fn(num)


# entered_num = int(input("Enter a number: "))
# process_number(entered_num, print_num_info)
# process_number(entered_num, print_square)


# Правила работы с функциями:
# 1. Функция должна выполнять одну конкретную задачу.
# 2. Функция должна иметь понятное и описательное имя.
# 3. Функция должна быть короткой и лаконичной.
# 4. Функция должна принимать аргументы, которые необходимы для выполнения задачи, и не должна полагаться на глобальные переменные.
# 5. Функция должна возвращать результат, если это необходимо, и не должна изменять входные данные без явного указания.
# 6. Функция должна быть документирована с помощью docstring, чтобы объяснить, что она делает, какие аргументы принимает и что возвращает.


# def mult_by_factor(value, mult=1):
#     """Умножает значение на заданный множитель."""
#     return value * mult


# print(mult_by_factor(5))  # 5
# print(mult_by_factor.__doc__)  # Умножает значение на заданный множитель.


# a = 10


# def my_fn():
#     a = True
#     b = 15
#     print(a)  # True
#     print(b)  # 15


# my_fn()

# print(a)  # 10
# print(b)  # NameError: name 'b' is not defined


# a = 5


# def my_fn():
#     def inner_fn():
#         print(a)  # 5
#     inner_fn()


# my_fn()


# def my_fn():
#     global a
#     a = 10


# my_fn()
# print(a)  # 10


# c = 5


# def my_fn(a, b):
#     print(c)  # 5
#     print(a, b)  # 10 15


# print(dir())  # None


# Оператори и  операнди:
# b = 5


# a = 5
# b = a

# c = a + b  # Оператор +, операнды a и b

# print(a is b)  # True
# print(c is a)  # False


# a = [1, 2, 3]
# b = [1, 2, 3]

# print(a == b)  # True

# print(a.__eq__(b))  # True

# print(a.__eq__) # <method-wrapper '__eq__' of list object at 0x7f8b8c8c8c8c>

# print(id(a) == id(b))  # False

# print(id(a))  # 140737488355328
# print(hex(id(a)))  # 0x7f8b8c8c8c8c


# print(dir(list))


# - my_number
# + my_number
# not is_activated

# Бинарные операторы и инфиксная нотация:
# a = 5
# a + 10
# a +- 2
# a += 3
# a == 8
# a and b
# a = True
# a + b
# a += 5
# a or b
# a > b


# my_num = 10

# print(+my_num)  # 10

# my_bool = False
# print(+my_bool)  # True


# Приоритетность операторов:
# a + b * c / d - e
# a + ((b * c)) / (d - e)
# (((a + b) * c) / d) - e


# D/Z:


# my_set1 = {1, 2, 3, 4, 5}
# my_set2 = {1, 2, 3, 4, 5}

# print(id(my_set1) == id(my_set2))  # False

# print(my_set1 == my_set2)  # or __eq__ True
# print(my_set1 is my_set2)  # False

# print(10 in my_set2)  # True
# print(1 in my_set1)  # True

# print(67 not in my_set1)  # True
# print(2 not in my_set2)  # False


# Ложный значения в Python - это значения, которые при приведении к булевому типу (bool) оцениваются как False. К ложным значениям относятся:
# int 0
# float 0.0
# bool False
# complex 0j
# NoneType None
# dict {}
# set set()
# list []
# str ""

# print(bool(0))  # False
# print(not not {})


# my_list = [1, 2, 3]

# if len(my_list) > 0:
#     print("List is not empty!")


# Логические операторы и операторы короткого замыкания:

# not,and,or

# and:
# Выражение 1 and Выражение 2
# Если Выражение 1 ложно, возвращается его значение. Иначе возвращается значение Выражения 2.
# Если выражение 1 истинно, возвращается его значение. Иначе возвращается значение Выражения 2.

# Цепочка операторов and и or:
# a and b and c and d
# a or b or c or d
# a or b and c or d


# my_list = [1, 2]

# other_list = ["a", "b"]

# print(len(my_list) < 0 or other_list)


# my_list = [1, 2]

# my_dict = {}

# print(my_list and my_dict)


# my_list = [1, 2]

# my_list and print("List is not empty!")


# my_dict1 = {"key": "value"}
# my_dict2 = {"key": "value"}

# my_dict1, my_dict2 and print("Both dictionaries are not empty!")  # True


# # 1. Створюємо два однакові словники
# dict1 = {"key": "value"}
# dict2 = {"key": "value"}

# # 2. Перевіряємо умови:
# #    а) вони однакові (dict1 == dict2)
# #    б) вони не порожні (and dict1)
# if dict1 == dict2 and dict1:
#     print("Both dictionaries are not empty!")


# Оператор расспаковки словаррей:

# button = {
#     "width": "200",
#     "text": "By now"
# }

# red_button = {
#     **button,
#     "color": "red",
# }

# print(red_button)  # {'width': '200', 'text': 'By now', 'color': 'red'}
# print(button)  # {'width': '200', 'text': 'By now'}


# button_info = {
#     "width": "200",
#     "text": "By now"
# }

# button_style = {
#     "price": "2000",
#     "model": "B300",
#     "name": "kirill",
#     "color": "red",
# }

# buttom = button_info | button_style

# # {'width': '200', 'text': 'By now', 'color': 'red'}
# print(buttom)  # {'width': '200', 'text': 'By now'}


# button_info = {
#     "width": "200",
#     "text": "By now"
# }

# button_style = {
#     "price": "2000",
#     "model": "B300",
#     "name": "kirill",
#     "color": "red",
# }

# buttom = {**button_info, **button_style}

# # {'width': '200', 'text': 'By now', 'color': 'red'}
# print(buttom)  # {'width': '200', 'text': 'By now'}


# del - это оператор в Python, который используется для удаления объектов. Он может удалять переменные, элементы из списков, ключи из словарей и даже целые объекты. Когда объект удаляется с помощью del, он становится недоступным и освобождает память, которую он занимал. Однако, если на объект все еще есть ссылки, он не будет удален до тех пор, пока все ссылки не будут удалены.


# Удаляет ключ "key" из словаря my_dict. Если ключа нет, вызывает KeyError.
# del my_dict["key"]


# my_dict = {"a": True, "b": False}
# # Удаляет ключ "another_key" из словаря my_dict. Если ключа нет, вызывает KeyError.
# del my_dict["a"]
# # Удаляет ключ "key" из словаря my_dict. Если ключа нет, вызывает KeyError.
# my_dict.__delitem__("b")

# print(my_dict)  # {}

# print(my_dict.__delitem__)


# my_list = [1, 2, 3, 4, 5]

# del my_list[0]  # Удаляет элемент с индексом 0 из списка my_list

# my_list.__delitem__(0)  # Удаляет элемент с индексом 0 из списка my_list

# print(my_list)  # [2, 3, 4, 5]


# Оператор + для соединения строк:

# "Hello " + "Python"  # Конкатенация строк, результат: "Hello Python"


# hello = "Hello "
# world = "World"

# # Конкатенация строк, результат: "Hello World"
# greeting = f"{hello}{world}!"
# print(greeting.title())  # Hello World


# Лямбда функции:

# lambda arguments: expression

# def mult(a ,b): - обычная функция
#     return a * b


# lambda a,b: a * b - лямбда функция


# def mult(a, b):
#     return a * b


# def mult(a, b): return a * b


# print(mult(10, 5))  # 50


# Обработка ошибок:

# print(10 / 0)  # ZeroDivisionError: division by zero


# try:
#     # Код, который может вызвать ошибку(выполнение блока кода)
#     pass
# except ErrorType:
#     # Код, который выполняется при возникновении ошибки (ErrorType - это тип ошибки, которую мы хотим обработать)
#     pass


# try:
#     print("10" / 0)  # ZeroDivisionError: division by zero

# except ZeroDivisionError as e:
#     print("You can't divide by zero!")  # You can't divide by zero!
#     print(type(e))  # <class 'ZeroDivisionError'>
#     # print(dir(e))
#     # print(e.__str__())  # division by zero
#     print(e)
# except TypeError as e:
#     print("Type error occurred!")  # Type error occurred!
#     print(e)
# else:
#     print("No errors occurred!")  # No errors occurred!

# print("Program continues...")  # Program continues...


# finally - это блок кода, который выполняется после блока try и всех блоков except, независимо от того, была ли ошибка или нет. Он используется для выполнения действий, которые должны быть выполнены в любом случае, например, закрытие файлов, освобождение ресурсов или выполнение других завершающих операций. Блок finally гарантирует, что определенный код будет выполнен, даже если в блоке try возникнет исключение.

# try:
#     print(10 / 5)
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# else:
#     print("There was no errors!")

# finally:
#     print("Program continues...")


# isinstance - это встроенная функция в Python, которая используется для проверки, является ли объект экземпляром определенного класса или кортежа классов. Она принимает два аргумента: объект, который нужно проверить, и класс или кортеж классов, с которым нужно сравнить объект. Функция возвращает True, если объект является экземпляром указанного класса или кортежа классов, и False в противном случае.
# Exception - это базовый класс для всех встроенных исключений в Python. Он служит основой для создания пользовательских исключений и обработки ошибок. Когда возникает ошибка, Python создает объект исключения, который содержит информацию о типе ошибки и ее сообщении. Исключения могут быть перехвачены и обработаны с помощью блоков try-except, что позволяет программе продолжать выполнение даже при возникновении ошибок.
# object - это базовый класс для всех объектов в Python. Все классы и типы данных в Python являются наследниками класса object. Это означает, что все объекты в Python имеют общие методы и атрибуты, которые определены в классе object. Например, все объекты имеют метод __str__(), который возвращает строковое представление объекта, и метод __eq__(), который используется для сравнения объектов на равенство. Класс object также предоставляет базовую функциональность для создания новых классов и объектов в Python.

# try:
#     print(10 / 0)  # ZeroDivisionError: division by zero
# except ZeroDivisionError as e:
#     print(isinstance(e, ZeroDivisionError))  # True
#     print(isinstance(e, Exception))  # True
#     print(e)
# except TypeError as e:
#     print(e)

# print("Program continues...")


# try:
#     print(10 / 0)  # ZeroDivisionError: division by zero
# except:
#     print("An error occurred!")  # An error occurred!


# def divide(a, b):
#     if b == 0:
#         raise TypeError("Second argument cannot be zero!")
#     return a / b


# def check_admin(user_id):
#     if user_id != 123:
#         raise PermissionError(
#             "You don't have permission to access this resource!")


# try:
#     check_admin(456)
# except PermissionError as e:
#     # You don't have permission to access this resource!
#     print(f"Bot said:{e}")


# try:
#     print(10 / 0)  # ZeroDivisionError: division by zero
# except ZeroDivisionError:
#     print("Хтось намагався поділити на нуль. Фіксую...")
#     raise  # Помилка летить далі


# def divide(a, b):
#     if b == 0:
#         raise ValueError("Second argument cannot be zero!")
#     return a / b


# try:
#     divide(10, 0)  # TypeError: Second argument cannot be zero!
# except ZeroDivisionError as e:
#     print(e)
# except ValueError as e:
#     print(e)  # Second argument cannot be zero!


# print("Program continues...")


# D/Z:

# bad code:
# def image_info(user_data: dict):
#     the_dict = f"Image {user_data['image_title']} has id {user_data['image_id']}."
#     return the_dict


# image_data = {
#     "image_title": "Sunset",
#     "image_id": 12345
# }


# try:
#     print(image_info(image_data))
#     raise KeyError("Missing key in user_data!")
# except KeyError as e:
#     print(f"Missing key in user_data: {e}")

#     else:
#         print("No errors occurred!")

# finally:
#     print("Program continues...")


# good code:
# def image_info(dict):
#     if ("image_id" not in dict) or ("image_title" not in dict):
#         raise KeyError("Missing key in user_data!")
#     the_dict = f"Image {dict['image_title']} has id {dict['image_id']}."
#     return the_dict


# image_data = {
#     "image_title": "Sunset",
#     "image_id": 12345
# }


# try:
#     print(image_info(image_data))

# except KeyError as e:
#     print(f"Missing key in user_data: {e}")
# except TypeError as e:
#     print(e)

# else:
#     print("No errors occurred!")

# finally:
#     print("Program continues...")


# Расспаковка списков и кортежей:

# list and tuple - это упорядоченные последовательности  элементов

# Длинный вариант(плохой):

# my_list = ["apple", "banana", "lime"]

# my_apple = my_list[0]
# my_bannana = my_list[1]
# my_lime = my_list[2]

# print(my_apple)  # apple
# print(my_bannana)  # banana
# print(my_lime)  # lime


# #Хорошый вариант:

# my_fruits = ["apple", "banana", "lime"]

# my_apple, my_bannana, my_lime = my_fruits

# print(my_apple)  # apple
# print(my_bannana)  # banana
# print(my_lime)  # lime


# my_list = [1,2,3]

# first, secound, third = my_list

# print(first)  # 1
# print(secound)  # 2
# print(third)  # 3


# my_fruits = ("apple", "banana", "lime")
# print(type(my_fruits))  # <class 'tuple'>

# my_apple, my_bannana, my_lime = my_fruits

# print(my_apple)  # apple
# print(my_bannana)  # banana
# print(my_lime)  # lime


# my_fruits = ["apple", "bannana", "lime"]

# my_apple, *remaining_fruits = my_fruits

# print(my_apple)  # apple
# print(remaining_fruits)  # ['bannana', 'lime']

# print(type(remaining_fruits))  # <class 'list'>


# Рассспаковка словарей:

# user_profile = {
#     "name": "Danya",
#     "comments_qty": 16
# }


# def user_info(name, comments_qty=0):
#     if not comments_qty:
#         return f"{name} has no comments."

#     return f"{name} has {comments_qty} comments."


# # Danya has 16 comments.
# print(user_info(**user_profile))

# or

# print(user_info(name=user_profile["name"], comments_qty=user_profile["comments_qty"]))


# user_profile = {
#     "name": "Danya",
#     "comments_qty": 16
# }


# def user_info(name, comments_qty=0):
#     if not comments_qty:
#         return f"{name} has no comments."

#     return f"{name} has {comments_qty} comments."


# name, comments_qty = user_profile
# # Danya has 16 comments.
# print(name)
# print(comments_qty)

# print(user_info(**user_profile))


# Расспаковка списка в позицийные аргументы функции:\


# user_data = ["Danya", 16]


# def user_info(name, comments_qty=0):
#     if not comments_qty:
#         return f"{name} has no comments."

#     return f"{name} has {comments_qty} comments."


# print(user_info(*user_data))  # Danya has 16 comments.


# the_list = [
#     {"name": "Danya", "comments_qty": 16},
#     {"name": "Alice", "comments_qty": 0},
#     {"name": "Bob", "comments_qty": 8}
# ]


# the_dict1 = the_list[0]
# the_dict2 = the_list[1]
# the_dict3 = the_list[2]


# def func(name, comments_qty=0):
#     if not comments_qty:
#         return f"{name} has no comments."

#     return f"{name} has {comments_qty} comments."


# print(func(**the_dict1))  # Danya has 16 comments.
# print(func(**the_dict2))  # Alice has no comments.
# print(func(**the_dict3))  # Bob has 8 comments.

# OR

# the_list = [
#     {"name": "Danya", "comments_qty": 16},
#     {"name": "Alice", "comments_qty": 0},
#     {"name": "Bob", "comments_qty": 8}
# ]


# def func(name, comments_qty=0):
#     if not comments_qty:
#         return f"{name} has no comments."

#     return f"{name} has {comments_qty} comments."


# for user_data in the_list:
#     print(func(**user_data))


# #Unusable code:
# #

# from openai import OpenAI

# client = OpenAI()

# user_promt = input("Prompt: ")

# response = client.responses.create(
#     input=user_promt,
#     model="gpt-5"
# )

# print(response.output_text)


# Условные конструкции:

# if
# if...else
# if...elif

# Тернарный оператор - это условное выражение, которое позволяет выбрать одно из двух значений в зависимости от условия. Он имеет следующую синтаксис: value_if_true if condition else value_if_false. Если условие истинно, возвращается value_if_true, иначе возвращается value_if_false.

# Ложные значения в Python:
# dict {}
# list []
# set set()
# str ""
# range range(0)

# int 0
# float 0.0
# bool False
# complex 0j
# NoneType None

# if Условие:
#     # Блок кода, который выполняется, если условие истинно
#     pass


# my_number = 10

# if my_number > 0:
#     print("Number is greater than 0!")  # Number is greater than 0!


# person_info = {
#     "age": 20
# }

# if not person_info.get("name"):
#     print("Имя отсутствует!")  # Имя отсутствует!


# .get() - это метод словаря в Python, который используется для получения значения по ключу. Он принимает два аргумента: ключ, который нужно найти, и значение по умолчанию, которое возвращается, если ключ не найден. Если ключ существует в словаре, метод .get() возвращает его значение. Если ключ не существует, он возвращает значение по умолчанию (или None, если значение по умолчанию не указано). Метод .get() полезен для предотвращения ошибок KeyError при попытке доступа к несуществующему ключу в словаре.


# print(not 0)  # True


# if 10 > 2:
#     print(True)  # True

# if 10 > 2:
#     print(True)  # True

# if 10 > 2:
#     print(True)  # True

# if 10 > 2:
#     print(True)  # True

# isinstance - это функция которая проверяет тип данных.Принимает два значения экземпляр и тип данных(например int,str)
# num_one = 10
# num_two = 5.3

# if ((num_one > 0) and (num_two > 0) and (isinstance(num_one, int)) and (isinstance(num_two, int))):
#     # Both numbers are positive and of correct types!
#     print("Both numbers are positive and of correct types!")


# if Условие:
#     # Блок кода, который выполняется, если Условие1 истинно
#     pass
# else:
#     # Блок кода, который выполняется, если Условие1 ложно
#     pass


# my_number = 21.5

# if type(my_number) is int:
#     print("Number is an integer!")
# else:
#     print("Number is not an integer!")  # Number is not an integer!


# my_phone = {
#     "price": 1000,
# }

# if my_phone.get("brand"):
#     print("Phone's brand is", my_phone["brand"])
# else:
#     print("Brand is not specified!")  # Brand is not specified!


# if Условие_1:
#     # Блок кода, который выполняется, если Условие_1 истинно
#     pass
# elif Условие_2:
#     # Блок кода, который выполняется, если Условие_1 ложно и Условие_2 истинно
#     pass
# else:
#     # Блок кода, который выполняется, если Условие_1 и Условие_2 ложны
#     pass


# my_number = -10

# if my_number > 0:
#     print(my_number, "Number is positive!")
# elif my_number < 0:
#     print(my_number, "Number is negative!")  # -10 Number is negative!
# else:
#     print(my_number, "Number is Zero!")


# if в функциях:


# def nums_info(a, b):
#     if (type(a) is not int) or (type(b) is not int):
#         return "Один из аргементов не целое число!"
#     if a >= b:
#         return f"{a} больше или равно {b}!"
#     return f"{a} меньше {b}!"


# print(nums_info(True, 10))  # Один из аргементов не целое число!
# print(nums_info(10, 2))  # 10 больше или равно 5!
# print(nums_info(5, 10))  # 5 меньше 10!


# def nums_info(a, b):
#     if (type(a) is not int) or (type(b) is not int):
#         info = "Один из аргементов не целое число!"
#     elif a >= b:
#         info = f"{a} больше или равно {b}!"
#     else:
#         info = f"{a} меньше {b}!"
#     return info


# print(nums_info(True, 10))  # Один из аргементов не целое число!
# print(nums_info(10, 2))  # 10 больше или равно 5!
# print(nums_info(5, 10))  # 5 меньше 10!


# D/Z:

# def route_info(the_dict):
#     if ("distance" in the_dict) and (isinstance(the_dict["distance"], int)):
#         info = f"Distance to your disination is {the_dict['distance']}"
#     elif ("speed" in the_dict) and ("time" in the_dict) and isinstance(the_dict["speed"], int) and isinstance(the_dict["time"], int):
#         info = f"Distance to your destination is {the_dict['speed'] * the_dict['time']}"
#     else:
#         info = "No distance info is available!"
#     return info


# print(route_info({"distance": 100}))  # Distance to your disination is 100
# # Distance to your destination is 100
# print(route_info({"speed": 50, "time": 2}))
# print(route_info({"My_name": "John"}))  # No distance info is available!


# Теренарный оператор:

# Выражение_1 if Условие else Выражение_2


# send_img(img) if img.get["is_porcessed"] else process_and_send_img(img)

# temp = +24

# weather = "hot" if temp > 18 else "cold"
# print(weather)


# my_img = ("1920", "1080")

# print(f"{my_img[0]}x{my_img[1]}") if len(
#     my_img) == 2 else print("Incorrect image formatting!")


# D/Z:

# 1)
# my_img = ("1920", "1080")

# if len(my_img) == 2:
#     print(f"{my_img[0]}x{my_img[1]}")
# else:
#     print("Incorrect image formatting!")


# 2)

# lenth = "Hello body! Im glad to see ypu broh! Whassup? I hope you are doing well!"

# info = "The string is long!" if len(lenth) > 79 else "The string is short!"
# print(info)  # The string is long!


# Цыклы:

# i = 10
# print(i)  # 10
# i *= 2

# print(i)  # 20
# i *= 2

# print(i)  # 40
# i *= 2


# my_fruits = ["apple", "banana", "lime"]

# print(my_fruits[0])  # apple
# print(my_fruits[1])  # banana
# print(my_fruits[2])  # lime


# my_object = {
#     "x": 10,
#     "y": True,
#     "z": "abc"
# }

# print(my_object["x"])  # 10
# print(my_object["y"])  # True
# print(my_object["z"])  # abc


# Цыкл for in:

# for Элемент in Последовательность:
#     # Блок кода, который выполняется для каждого элемента в последовательности
#     pass


# my_list = [True, 10, "abc", {}]

# for element in my_list:
#     print(element)


# my_object = {
#     "x": 10,
#     "y": True,
#     "z": "abc"
# }

# for i in my_object:
#     print(i, my_object[i])  # x y z


# for i in [10, "Hello world!", False]:
#     print(type(i))
#     print(i)  # 10 20 30


# for i in (10, "Hello world!", False):
#     print(type(i))
#     print(i)  # 10 20 30

# my_dict = {"id": 324,
#            "title": "My post",
#            "is_published": True
# }

# for key in my_dict:
#     print(type(key))
#     print(key)  # 10 20 30
#     print(my_dict[key])  # 324


# for in для словарей и метод items():

# my_object = {
#     "x": 10,
#     "y": True,
# }

# for item in my_object.items():
#     key, value = item
#     print(key, value)  # x 10 y True


# my_dict = {"id": 324,
#            "title": "My post",
#            }

# for key, value in my_dict.items():
#     print(f"The key: {key}, The value: {value}")


# Цыкл for in для строк:

# my_name = "Daniel"

# for i in my_name:
#     print(i)

# Цыкл for in для диапазонов(range):

# for num in range(5):
#     print(num)

# for odd_num in range(3, 10, 2):
#     print(odd_num)


# D/Z:

# Zadanie 1

# def dict_to_list(the_dict):
#     for key, value in the_dict.items():
#         if isinstance(value, int):
#             return f"The key: {key}, The value: {value * 2}"
#         else:
#             return f"The key: {key}, The value: {value}"


# print(dict_to_list(the_dict={
#     "price": 2000,
#     "brand": "Mazda"
# }))


# def dict_to_list(the_dict):

#     result_list = []

#     for key, value in the_dict.items():
#         if isinstance(value, int):
#             value *= 2
#         result_list.append((key, value))

#     return result_list


# my_data = {
#     "price": 2000,
#     "brand": "Mazda"
# }

# print(dict_to_list(my_data))
# # [('price', 4000), ('brand', 'Mazda')]


# Zadanie 2

# def filter_list(the_list, value_type):

#     new_list = []

#     for i in the_list:
#         if type(i) is value_type:
#             new_list.append(i)

#     return new_list


# print(filter_list([35, True, "abc", 10], int))
# print(filter_list([35, True, "abc", 10], str))
# print(filter_list([35, True, "abc", 10], bool))


# print(isinstance(True, bool))  # True
# print(isinstance(True, int))  # True
# print(isinstance(True, object))  # True
# print(int.__subclasses__())  # [<class 'bool'>]


# Сортировка списков с помощью функции filter():

# Обычная функция:
# def filter_list(list_to_filter, value_type):
#     def check_element_type(element):
#         return isinstance(element, value_type)

#     return list(filter(check_element_type, list_to_filter))


# res = (filter_list([1, 10, "abc", 5.5, False], int))
# print(res)  # <filter object at 0x7f8b8c8c8c8c>


# Лямбда функция:

# def filter_list(list_to_filter, value_type):
#     return list(filter(lambda element: type(element) is value_type,
#                        list_to_filter))


# res = (filter_list([1, 10, "abc", 5.5, False], int))
# print(res)  # <filter object at 0x7f8b8c8c8c8c>


# Цыкл while:

# while Условие:
# Блок кода выполняемый на каждой итерации
