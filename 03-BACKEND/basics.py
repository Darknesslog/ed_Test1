
# по тз нужно было поработать с базовыми принципами программирования и problem-solving, так что вот

# basic operations

age = 18
if age >= 18:
    print("вы взрослый")
else:
    print("вы совершеннолетний?")

score = 75
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "D"
print("оценка:", grade)

age = 20
has_license = True
if age >= 18 and has_license:
    print("можно водить машину")

is_blocked = False
if not is_blocked:
    print("доступ разрешён")

value = 10
description = "большой" if value > 5 else "маленький"
print("value =>", value, "описание:", description)

value = 3
description = "большой" if value > 5 else "маленький"
print("value =>", value, "описание:", description)


# 123s

print("цикл от 0 до 4:")
for i in range(5):
    print("итерация", i)

fruits = ["яблоко", "банан", "апельсин"]
print("\nфрукты:")
for fruit in fruits:
    print("-", fruit)

person = {"имя": "иван", "возраст": 25}
print("\nданные человека:")
for key, value in person.items():
    print(key + ":", value)

count = 0
while count < 3:
    print("счёт:", count)
    count += 1

print("\nцикл с break и continue:")
for i in range(10):
    if i == 3:
        continue
    if i == 7:
        break
    print(i)


# funcs

def greet(name):
    return f"привет, {name}!"

print(greet("иван"))

def add(a, b):
    return a + b

result = add(5, 3)
print("5 + 3 =", result)

def create_greeting(name, greeting="привет"):
    return f"{greeting}, {name}!"

print(create_greeting("мария"))
print(create_greeting("пётр", "добрый день"))

def sum_numbers(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print("сумма:", sum_numbers(1, 2, 3, 4, 5))

def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(имя="иван", возраст=25, город="москва")

square = lambda x: x ** 2
print("квадрат 5:", square(5))

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print("квадраты:", squared)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("чётные числа:", even_numbers)


# lists

numbers = [3, 1, 4, 1, 5, 9]
numbers.append(2)
print("после append:", numbers)

numbers.remove(1)
print("после remove:", numbers)

numbers.sort()
print("отсортирован:", numbers)

doubled = [x * 2 for x in numbers]
print("удвоенные:", doubled)


# dicts

person = {
    "имя": "иван",
    "возраст": 25,
    "город": "москва",
}

person["профессия"] = "разработчик"

print("имя:", person["имя"])
print("имя (безопасно):", person.get("имя", "неизвестно"))

if "возраст" in person:
    print("ключ 'возраст' существует")

del person["город"]
print("после удаления:", person)

print("ключи:", list(person.keys()))
print("значения:", list(person.values()))


# exceptions

try:
    number = int("abc")
except ValueError:
    print("ошибка: неверное число")
except Exception as e:
    print("неизвестная ошибка:", e)
else:
    print("число успешно преобразовано:", number)
finally:
    print("finally всегда выполняется")


# ооп

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"я {self.name}, мне {self.age} лет"

    def is_adult(self):
        return self.age >= 18

p1 = Person("элекс", 17)
p2 = Person("мурия", 25)

print("p1.greet():", p1.greet())
print("p2.greet():", p2.greet())

print("p1.is_adult():", p1.is_adult())
print("p2.is_adult():", p2.is_adult())

class Counter:
    def __init__(self):
        self.value = 0

    def increment(self, step=1):
        self.value += step
        return self.value

    def reset(self):
        self.value = 0
        return self.value

c = Counter()
print("c.value нач.", c.value)
print("c.increment():", c.increment())
print("c.increment(5):", c.increment(5))
print("c.reset():", c.reset())


# caeser

def caesar_encode(text, shift):
    result = []
    for ch in text:
        if ch.isalpha():
            start = ord('A') if ch.isupper() else ord('a')
            offset = (ord(ch) - start + shift) % 26
            result.append(chr(start + offset))
        else:
            result.append(ch)
    return "".join(result)

def caesar_decode(text, shift):
    return caesar_encode(text, -shift)

original = "Hello, World! 123"
shift = 3

encoded = caesar_encode(original, shift)
decoded = caesar_decode(encoded, shift)

print("original:", original)
print("shift:", shift)
print("encoded:", encoded)
print("decoded:", decoded)
print("decoded == original:", decoded == original)


people = [
    Person("онна", 15),
    Person("пэрис", 20),
    Person("пика", 17),
    Person("сритрий", 30),
]

adults_loop = []
for p in people:
    if p.is_adult():
        adults_loop.append(p.name)
print("adults (цикл):", adults_loop)

adults_map_filter = [p.name for p in people if p.is_adult()]
print("adults (list comprehension):", adults_map_filter)

people_strings = list(map(lambda p: f"{p.name} ({p.age})", people))
print("people_strings:", people_strings)

adults_strings = list(
    map(lambda p: f"{p.name} ({p.age})",
        filter(lambda p: p.is_adult(), people))
)
print("adults_strings (map + filter):", adults_strings)


x = [1, 2, 3]
y = [1, 2, 3]
z = x

print("x =", x)
print("y =", y)
print("z =", z)

print("x == y:", x == y)
print("x is y:", x is y)
print("x is z:", x is z)


##EOF
