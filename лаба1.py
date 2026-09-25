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


class Athlete:
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height

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


class Subscription:
    def __init__(self, owner, days, price):
        self.owner = owner
        self.days = days
        self.price = price
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

        print(f"Ціна одного візиту: {self.price / self.visits:.0f} грн")


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


class Trainer:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty
        self.clients = []

    def add_client(self, athlete):
        self.clients.append(athlete)
        print(f"{self.name} бере в роботу: {athlete}")

    def plan(self, workout):
        print(f"План від тренера {self.name} ({self.specialty}):")

        for exercise, sets in workout.exercises.items():
            print(f"  {exercise} — {len(sets)} підходів")

    def show_clients(self):
        print(f"Клієнти тренера {self.name}: {', '.join(self.clients)}")


exercises = {
    "Жим лежачи": [(60, 8), (60, 7), (55, 10)],
    "Тяга верхнього блока": [(60, 10), (60, 10), (65, 8)],
    "Підйом гантелей": [(12, 12), (12, 10), (10, 12)]
}

name_of_sportsman = "Гоша"

workout = Workout(name_of_sportsman, exercises)

print(f"Тренування спортсмена: {workout.name}")
workout.calculate()
workout.strongest_exercise()

print()
athlete = Athlete(name_of_sportsman, 78.5, 182)
athlete.status()
athlete.gain(1.5)

print()
subscription = Subscription(name_of_sportsman, 30, 1200)
subscription.visit()
subscription.visit()
subscription.price_per_visit()

print()
bench = Equipment("Лава для жиму", 120)
bench.take(athlete.name)
bench.check_weight(60)
bench.check_weight(150)
bench.release()

print()
trainer = Trainer("Олег", "силові тренування")
trainer.add_client(athlete.name)
trainer.add_client("Марія")
trainer.plan(workout)
trainer.show_clients()

