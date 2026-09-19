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

    def info(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height
        print (f"\n\nІм'я: {self.name},\nВага: {self.weight} кг,\nЗріст: {self.height} см\n\n\n")

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

    def lose(self, kilograms):
        self.weight -= kilograms
        print(f"Нова вага: {self.weight:.1f} кг")

class Abonement:
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
            print(f"  {exercise} - {len(sets)} підходів")

    def show_clients(self):
        print(f"Клієнти тренера {self.name}: {', '.join(self.clients)}")



exercises = {
    "Жим лежачи": [(60, 8), (60, 7), (55, 10)],
    "Тяга верхнього блока": [(60, 10), (60, 10), (65, 8)],
    "Підйом гантелей": [(12, 12), (12, 10), (10, 12)]
}

workout = Workout("Гоша", exercises)

print(f"Тренування спортсмена: {workout.name}")
workout.calculate()
workout.strongest_exercise()

print()
athlete = Athlete("Гоша", 78.5, 182)
athlete.info(athlete.name, athlete.weight, athlete.height)
athlete.status()
athlete.lose(0.5)
athlete.status()
athlete.gain(1.5)


print()
subscription = Abonement("Гоша", 30, 1200)
subscription.visit()
subscription.visit()
subscription.price_per_visit()


print()
trainer = Trainer("Григорій", "силові тренування")
trainer.add_client(athlete.name)
trainer.add_client("Гоша")
trainer.plan(workout)
trainer.show_clients()