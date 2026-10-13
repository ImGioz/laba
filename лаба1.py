class Person:
    def __init__(self, name, age, passport):
        self.name = name
        self._age = age
        self.__passport = passport

    def get_passport(self):
        return self.__passport

    def info(self):
        print(f"Людина: {self.name}, вік: {self._age}")

class Athlete(Person):
    def __init__(self, name, age, passport, weight, height):
        super().__init__(name, age, passport)
        self.weight = weight
        self.height = height

    def info(self):
        print(f"Спортсмен: {self.name}, вік: {self._age}, "
              f"вага: {self.weight:.1f} кг, зріст: {self.height:.0f} см")

    def bmi(self):
        return self.weight / (self.height / 100) ** 2

    def status(self):
        index = self.bmi()

        if index < 18.5:
            result = "недостатня вага"
        elif index < 25:
            result = "норма"
        else:
            result = "надлишкова вага"

        print(f"{self.name}: ІМТ {index:.1f} ({result})")

    def gain(self, kilograms):
        self.weight += kilograms
        print(f"Нова вага: {self.weight:.1f} кг")

    def show_access(self):
        print(f"public: {self.name}")
        print(f"protected: {self._age}")
        try:
            print(self.__passport)
        except AttributeError:
            print("private: немає доступу до __passport")
        print(f"private через метод: {self.get_passport()}")

class Trainer(Person):
    def __init__(self, name, age, passport, specialty):
        super().__init__(name, age, passport)
        self.specialty = specialty
        self.clients = []

    def info(self):
        print(f"Тренер: {self.name}, вік: {self._age}, "
              f"спеціалізація: {self.specialty}, клієнтів: {len(self.clients)}")

    def add_client(self, athlete):
        self.clients.append(athlete)
        print(f"{self.name} бере в роботу: {athlete}")

    def plan(self, workout):
        print(f"План від тренера {self.name} ({self.specialty}):")

        for exercise, sets in workout.exercises.items():
            print(f"  {exercise} — {len(sets)} підходів")

    def show_clients(self):
        print(f"Клієнти тренера {self.name}: {', '.join(self.clients)}")

class Subscription:
    def __init__(self, owner, days, price):
        self.owner = owner
        self.days = days
        self._price = price
        self.visits = 0

    def visit(self):
        if self.days == 0:
            print("Абонемент закінчився")
            return

        self.days -= 1
        self.visits += 1
        print(f"Візит №{self.visits}, залишилось днів: {self.days}")

    def price_per_visit(self):
        if self.visits == 0:
            print("Візитів ще не було")
            return

        print(f"Ціна одного візиту: {self._price / self.visits:.0f} грн")

class PremiumSubscription(Subscription):
    def __init__(self, owner, days, price, discount):
        super().__init__(owner, days, price)
        self.discount = discount

    def price_per_visit(self):
        if self.visits == 0:
            print("Візитів ще не було")
            return

        price = self._price * (1 - self.discount / 100)
        print(f"Ціна одного візиту зі знижкою: {price / self.visits:.0f} грн")

class Workout:
    def __init__(self, name, exercises):
        self.name = name
        self.exercises = exercises
        self.total_volume = 0.0

    def volume(self, sets):
        return sum(weight * reps for weight, reps in sets)

    def calculate(self):
        for exercise, sets in self.exercises.items():
            volume = self.volume(sets)
            self.total_volume += volume
            print(f"{exercise}: {volume:.0f} кг")

        print(f"Загальний об'єм: {self.total_volume:.0f} кг")

    def strongest_exercise(self):
        volumes = {
            exercise: self.volume(sets)
            for exercise, sets in self.exercises.items()
        }

        strongest = max(volumes, key=volumes.get)

        print(f"Найбільше навантаження: {strongest}")
        print(f"Об'єм: {volumes[strongest]:.0f} кг")

class Equipment:
    def __init__(self, title, max_weight):
        self.title = title
        self.max_weight = max_weight
        self.busy = False

    def take(self, athlete):
        if self.busy:
            print(f"{self.title} вже зайнятий")
            return

        self.busy = True
        print(f"{athlete} займає тренажер: {self.title}")

    def release(self):
        self.busy = False
        print(f"{self.title} вільний")

    def check_weight(self, weight):
        if weight > self.max_weight:
            print(f"Забагато: максимум {self.max_weight} кг")
        else:
            print(f"Вага {weight} кг підходить")

def section(title):
    print()
    print(f"========== {title} ==========")

section("Спортсмен")
name_of_sportsman = input("Ім'я спортсмена: ")
age = int(input("Вік: "))
passport = input("Номер паспорта: ")
weight = float(input("Вага (кг): "))
height = float(input("Зріст (см): "))
gain_kg = float(input("На скільки кг змінилась вага: "))

section("Тренування")
exercises = {}
count = int(input("Скільки вправ: "))
for i in range(count):
    print()
    title = input(f"Назва вправи {i + 1}: ")
    sets = []
    sets_count = int(input("Кількість підходів: "))
    for j in range(sets_count):
        w = float(input(f"  Підхід {j + 1}, вага: "))
        r = int(input(f"  Підхід {j + 1}, повторення: "))
        sets.append((w, r))
    exercises[title] = sets

section("Абонемент")
days = int(input("Днів в абонементі: "))
price = float(input("Ціна абонемента (грн): "))
discount = float(input("Знижка преміум-абонемента (%): "))
visits = int(input("Скільки візитів зробити: "))

section("Тренажер")
equipment_title = input("Назва тренажера: ")
max_weight = float(input("Максимальна вага тренажера (кг): "))
weight_1 = float(input("Перша вага для перевірки: "))
weight_2 = float(input("Друга вага для перевірки: "))

section("Тренер")
trainer_name = input("Ім'я тренера: ")
trainer_age = int(input("Вік тренера: "))
trainer_passport = input("Паспорт тренера: ")
specialty = input("Спеціалізація тренера: ")
second_client = input("Ім'я ще одного клієнта: ")

print()
print("#" * 50)
print("#" + "РЕЗУЛЬТАТИ".center(48) + "#")
print("#" * 50)

section("Спортсмен")
athlete = Athlete(name_of_sportsman, age, passport, weight, height)
athlete.status()
athlete.gain(gain_kg)

section("Тренування")
workout = Workout(name_of_sportsman, exercises)
print(f"Тренування спортсмена: {workout.name}")
workout.calculate()
workout.strongest_exercise()

section("Абонемент")
subscription = PremiumSubscription(name_of_sportsman, days, price, discount)
for _ in range(visits):
    subscription.visit()
subscription.price_per_visit()

section("Тренажер")
bench = Equipment(equipment_title, max_weight)
bench.take(athlete.name)
bench.check_weight(weight_1)
bench.check_weight(weight_2)
bench.release()

section("Тренер")
trainer = Trainer(trainer_name, trainer_age, trainer_passport, specialty)
trainer.add_client(athlete.name)
trainer.add_client(second_client)
trainer.plan(workout)
trainer.show_clients()

section("Поліморфізм")
people = [Person(name_of_sportsman, age, passport), athlete, trainer]
for person in people:
    person.info()

regular = Subscription(name_of_sportsman, days, price)
regular.visits = subscription.visits
for sub in [regular, subscription]:
    sub.price_per_visit()

section("Інкапсуляція")
athlete.show_access()
